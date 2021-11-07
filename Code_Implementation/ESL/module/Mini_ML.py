# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 2020

@author: yumin cho
"""

import pandas as pd
import numpy as np
import sys
import math
from collections import Counter
from scipy.optimize import minimize, fmin_tnc
import seaborn as sns
from matplotlib import pyplot as plt

class Stat_Model:
    def __init__(self):
        # load data
        file_name1 = input("Enter the name of train data file\n: ")
        file_name2 = input("Enter the name of test data file\n: ")
        sep = " " if int(input("Select the data coding format(1 = 'a b c', 2 = 'a, b, c')\n: ")) ==1 else ","
        header = None if input("Does the data have column header?(y/n)\n: ") == "n" else 0 
        train_data = pd.read_csv(file_name1, sep=sep, header=header)
        test_data = pd.read_csv(file_name2, sep=sep, header=header)
        
        # Split data
        print(train_data.head(3))
        Y_opt = int(input("Select the the way you enter the Y variable(1 = 'column position', 2 = 'column name')\n: "))
        if Y_opt == 1:
            Y_pos = int(input("Enter the column position of the response variable(if the first column is the response variable enter 1)\n: "))-1
            Y_col1 = train_data.columns.tolist()[Y_pos]
            Y_col2 = test_data.columns.tolist()[Y_pos]
        else:
            Y_col1 = input("Enter the column name of the response variable\n: ")
            if Y_col1.isalpha()==False:
                Y_col1 = int(Y_col1)
            Y_col2 = Y_col1
        
        self.X_train, self.Y_train = train_data.loc[:,train_data.columns!=Y_col1], train_data.loc[:,Y_col1]
        self.X_test, self.Y_test = test_data.loc[:,test_data.columns!=Y_col2], test_data.loc[:,Y_col2]
        
        # Set up
        self.p = self.X_train.shape[1] 
        self.n_tr = self.X_train.shape[0]
        self.n_tst = self.X_test.shape[0]
        
        # Select Model
        self.run_opt = int(input("Select the way you run the model(1 = 'regression', 2 = 'classification)\n: "))
        if self.run_opt == 1:
            self.linear_regression()
            self.show_data_reg()
        else:        
            self.k = len(self.Y_train.unique())
            if self.k > 2:
                self.run_opt2 = int(input("Select the method for classification(1 = 'Linear Regression of an Indicator', 2 = 'LDA', 3 = 'QDA')\n: "))
            else:
                self.run_opt2 = int(input("Select the method for classification(1 = 'Linear Regression of an Indicator', 2 = 'LDA', 3 = 'QDA', 4 = 'Logistic Regression')\n: "))
            if self.run_opt2 == 1:
                self.linear_regression_with_indicator()
                self.show_data_cls()
                
            elif self.run_opt2 == 2:
                self.linear_discriminant_analysis()
                self.show_data_cls()
            elif self.run_opt2 == 3:
                self.quadratic_discriminant_analysis()
                self.show_data_cls()
            else:
                self.logistic_regression()
                self.show_data_cls()
           
                    
    ### Model         
    ## 1) Linear Regression         
    def add_constant(self,X):
        X0 = np.ones((X.shape[0],1))
        return np.concatenate((X0, np.array(X)),axis=1)
    
    def get_coefficient(self,X,Y):
        return (np.linalg.inv(X.T@X))@X.T@np.array(Y)
    
    def linear_regression(self):
        # add constant
        self.X_tr = self.add_constant(self.X_train)
        self.X_tst = self.add_constant(self.X_test)
       
        # estimate coefficients
        self.beta = self.get_coefficient(self.X_tr,self.Y_train)
        
        # predict Y
        self.Y_tr_hat = np.dot(self.X_tr, self.beta)
        self.Y_tst_hat = np.dot(self.X_tst, self.beta)
        
    ## 2) Linear Regression of an Indicator
    def get_dummies(self,Y):
        n = Y.shape[0]
        k = len(Y.unique())
        Y_dummy = pd.DataFrame(np.zeros((n, k))).astype('int')
        i = 0
        for y in Y:
            Y_dummy.iloc[i,y-1] = 1
            i += 1
        Y_dummy.columns = [i for i in range(1,k+1)]
        return Y_dummy
    
    def get_Y_hat_for_lri(self,X,Y_dummy):
        n = X.shape[0]
        df_Y_hat = pd.DataFrame(np.zeros((n,self.k)),
                                   columns=[i for i in range(1,self.k+1)])
        for i in range(1,self.k+1):
            df_Y_hat[i-0] = X@self.get_coefficient(self.X_tr,Y_dummy[i])
        return np.argmax(np.array(df_Y_hat), axis=1) + 1
    
    def linear_regression_with_indicator(self):
        # Indicator Y
        Y_dummy = self.get_dummies(self.Y_train)
        
        # add constant
        self.X_tr = self.add_constant(self.X_train)
        self.X_tst = self.add_constant(self.X_test)
        
        # estimate coefficients & predict Y
        self.Y_tr_hat = self.get_Y_hat_for_lri(self.X_tr,Y_dummy)
        self.Y_tst_hat = self.get_Y_hat_for_lri(self.X_tst,Y_dummy)
        
    ## 3) LDA & QDA   
    def lda_func(self,x0):
        Y_class = self.k
        X_col = self.p
        X_train= self.X_train
        Y_train= self.Y_train
        mean_vector = []
        for i in range(1,Y_class+1):
            mean_vector.append(np.array(X_train.iloc[Y_train[Y_train==i].index,:].mean()))
        S_p = np.zeros((X_col,X_col))
        for cl in [i for i in range(1,Y_class+1)]:
            mtx = np.zeros((X_col,X_col))
            for i in X_train.iloc[Y_train[Y_train==cl].index,:].values:
                x_i = i.reshape(X_col,1)
                mu = mean_vector[cl-1].reshape(X_col,1)
                mtx += (x_i - mu)@(x_i - mu).T
            S_p += mtx
        pooled_cov = S_p/(len(X_train)-Y_class)
        
        d_list = []
        for i in range(0,Y_class):
            d_x = mean_vector[i].T@np.linalg.inv(pooled_cov)@x0-0.5*mean_vector[i].T@np.linalg.inv(pooled_cov)@mean_vector[i]+math.log(1/Y_class)
            d_list.append(d_x)
        return np.argmax(np.array(d_list))+1
    
    def qda_func(self,x0):
        Y_class = self.k
        X_col = self.p
        X_train= self.X_train
        Y_train= self.Y_train
        mean_vector = []
        for i in range(1,Y_class+1):
            mean_vector.append(np.array(X_train.iloc[Y_train[Y_train==i].index,:].mean()))
        d_list = [] 
        for cl in [i for i in range(1,Y_class+1)]:
            mtx = np.zeros((X_col,X_col))
            for i in X_train.iloc[Y_train[Y_train==cl].index,:].values:
                x_i = i.reshape(X_col,1)
                mu = mean_vector[cl-1].reshape(X_col,1)
                mtx += (x_i - mu)@(x_i - mu).T
            S_k = mtx/len(X_train.iloc[Y_train[Y_train==cl].index,:])
            d_x = -0.5*math.log(np.linalg.det(S_k))-0.5*(x0-mean_vector[cl-1]).T@np.linalg.inv(S_k)@(x0-mean_vector[cl-1])+math.log(1/Y_class)
            d_list.append(d_x)
        return np.argmax(np.array(d_list))+1
    

    def linear_discriminant_analysis(self):
        # Resubstitution
        Y_tr_hat = []
        for i in range(0,len(self.X_train)):
                Y_tr_hat.append(self.lda_func(self.X_train.iloc[i,:]))
        self.Y_tr_hat = Y_tr_hat
        # Test
        Y_tst_hat = []
        for i in range(0,len(self.X_test)):
                Y_tst_hat.append(self.lda_func(self.X_test.iloc[i,:]))
        self.Y_tst_hat = Y_tst_hat

    def quadratic_discriminant_analysis(self): 
        # Resubstitution
        Y_tr_hat = []
        for i in range(0,len(self.X_train)):
                Y_tr_hat.append(self.qda_func(self.X_train.iloc[i,:]))
        self.Y_tr_hat = Y_tr_hat
        # Test
        Y_tst_hat = []
        for i in range(0,len(self.X_test)):
                Y_tst_hat.append(self.qda_func(self.X_test.iloc[i,:]))
        self.Y_tst_hat = Y_tst_hat

    ## 4) Logistic Regression
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))

    def hypothesis(self,theta,x):
        z = x@theta
        h = self.sigmoid(z)
        return h

    def cost_function(self,theta,x,y):
        h = self.hypothesis(theta,x)
        m = x.shape[0]
        tot_cost = -(1/m)*np.sum(y*np.log(h) + (1-y)*np.log(1-h)) + 1e-7
        return tot_cost
    
    def gradient(self,theta, x, y):
        m = x.shape[0]
        h = self.hypothesis(theta, x)
        gradient = (1/m)*(x.T@(h-y))
        return gradient

    def fit(self,theta,x,y):
        opt = fmin_tnc(func=self.cost_function,x0 = theta,fprime=self.gradient,args=(x,y.flatten()))
        return opt[0]

    def predict(self,params,x):
        theta = params[:, np.newaxis]
        return self.hypothesis(theta, x)

    def logistic_regression(self):
        # Y has only two classes
        ths = 0.5
        # Y
        if self.Y_train.unique().min() != 0:
            self.Y_train = self.Y_train - self.Y_train.unique().min()
        if self.Y_test.unique().min() != 0:
            self.Y_test = self.Y_test - self.Y_test.unique().min()    

        self.Y_tr = self.Y_train[:, np.newaxis]
        self.Y_tst = self.Y_test[:, np.newaxis]

        # add constant
        self.X_tr = self.add_constant(self.X_train)
        self.X_tst = self.add_constant(self.X_test)

        # initialize theta
        theta = np.zeros((self.X_tr.shape[1],1))
        self.params = self.fit(theta, self.X_tr, self.Y_tr)

        # Resubstitution
        self.Y_tr_prob = self.predict(self.params,self.X_tr)
        self.Y_tr_hat = (self.Y_tr_prob >= ths).astype(int).flatten()
        # Test
        self.Y_tst_prob = self.predict(self.params,self.X_tst)
        self.Y_tst_hat = (self.Y_tst_prob >= ths).astype(int).flatten()


    ### Evaluation for regression
    def model_summary(self):
        n = self.n_tr
        y = self.Y_train
        
        # SST
        deviation = y - np.mean(y) # np.dot(y, np.ones(n))/n
        SST = np.dot(deviation.T, deviation)
        
        # SSE
        residual = y - self.Y_tr_hat
        SSE = np.dot(residual.T, residual) # np.sum(residual**2)
        
        # R_squared
        self.R2_tr = 1 - (SSE/SST)
        
        # MSE
        self.mse_tr = SSE / (n-self.p-1)
    
    def prediction_performace(self):
        n = self.n_tst
        y = self.Y_test
        y_hat = self.Y_tst_hat
        residual = y - y_hat

        # R_squared
        self.R2_tst = np.corrcoef(y, y_hat)[0][1]**2
        # MAE
        self.mae = np.mean(np.abs(residual))
        # MAPE
        self.mape =  np.mean(np.abs(residual/y))*100
        # RMSE
        SSE = np.dot(residual.T, residual)
        self.rmse = np.sqrt(SSE/n) 


    ### Evaluation for Classification
    def lift_table(self,data,col):
        # sorting
        df = data[[col,'y']].sort_values(col,ascending=False,ignore_index=True)
        # discretization 
        bins = pd.qcut(df[col].index,10, labels=False)
        d_list = []
        csum = 0
        for i in Counter(bins).values():
            csum += i
            d_list.append(csum)
        df_lift = df[['y']].groupby(bins).sum()
        df_lift.columns = [col]
        baseline = df_lift.sum()/len(data)
        df_lift['cum'] = df_lift.cumsum()
        df_lift['pct_Cap_Res'] = df_lift['cum']/df_lift[col].sum()
        
        df_lift['pct_Res'] = np.array(df_lift['cum'])/np.array(d_list)
        df_lift['lift'] = df_lift['pct_Res']/baseline.values
        del df_lift['cum']
        return df_lift

    def draw_lift_chart(self,prob,Y):
        # dataframe
        data = pd.DataFrame(prob)
        data.columns=['prob']
        data['y'] = Y
        # lift table
        lift_table = self.lift_table(data,'prob')
        # cumulative captured response
        df_ccr = pd.DataFrame({'d': [i for i in range(1,11)],'ccr': lift_table['pct_Cap_Res']})
        # lift chart
        df_zero = pd.DataFrame({'d':[0],'ccr':[0]})
        df_plot = pd.concat([df_zero,df_ccr])
        df_plot.reset_index(inplace=True)
        del df_plot['index']
        ax = sns.lineplot(x="d",y="ccr",marker="o",data=df_plot)
        ax.set(title="Lift chart",xlabel="Decile", xticks=[i for i in range(0,11)], ylabel="% cumulative captured response")
        plt.show()
        return df_plot

    def accuracy_ratio(self,df_plot,col):
        ar=0
        for i in range(0,len(df_plot)-1):
            sub_ar = (df_plot.loc[i,col]+df_plot.loc[i+1,col])/2
            ar += sub_ar
        return round((ar-5)/4.5,4)

    def classfication_evaluation(self):
        if self.run_opt2 != 4:
            # confustion matrix
            self.cf_tr = pd.crosstab(self.Y_train,np.array(self.Y_tr_hat), 
                                    rownames=['Actual Class'], colnames=['Predicted Class']) 
            self.cf_tst = pd.crosstab(self.Y_test,np.array(self.Y_tst_hat), 
                                    rownames=['Actual Class'], colnames=['Predicted Class']) 
            # accuracy
            self.acc_tr = np.trace(np.array(self.cf_tr))/self.n_tr
            self.acc_tst = np.trace(np.array(self.cf_tst))/self.n_tst

        else:
            # lift chart
            self.df_plot_tr = self.draw_lift_chart(self.Y_tr_prob,self.Y_tr)
            self.df_plot_tst = self.draw_lift_chart(self.Y_tst_prob,self.Y_tst)
            # accuracy ratio
            self.ar_tr = self.accuracy_ratio(self.df_plot_tr,'ccr')
            self.ar_tst = self.accuracy_ratio(self.df_plot_tst,'ccr')


    ### Show data
    def show_data_reg(self):
        self.model_summary()
        self.prediction_performace()
        
        sys.stdout = open(input("Enter the output file name to export: "),'w')
        print("Coefficients\n-------------")
        print(f"Constant: {round(self.beta[0],3)}")
        for i in range(1,self.p+1):
            print(f"Beta{i}:",round(self.beta[i],4))
        print("")
        print("Model Summary\n-------------")
        print(f"R-square = {round(self.R2_tr,4)}")
        print(f"MSE = {round(self.mse_tr,3)}")
        print("")
        print("Prediction Performance\n-------------")
        print(f"Predictive R-square = {round(self.R2_tst,4)}")
        print(f"MAE = {round(self.mae,3)}")
        print(f"MAPE = {round(self.mape,3)}")
        print(f"RMSE = {round(self.rmse,3)}")
    
    def show_data_cls(self):
        self.classfication_evaluation()
        if self.run_opt2 != 4:
            sys.stdout = open(input("Enter the output file name to export: "),'w')
            print(f"ID, Actual class, Resub pred\n-----------------------------")
            for i in range(0,self.n_tr):
                print(i+1,self.Y_train[i],self.Y_tr_hat[i],sep=",")
            print("")
            print(f"Confusion Matrix (Resubstitution)\n----------------------------------")
            print(self.cf_tr)
            print("")
            print(f"Model Summary (Resubstitution)\n----------------------------------")
            print(f"Overall accuracy = {round(self.acc_tr,3)}")  
            print("") 
            print(f"ID, Actual class, Test pred\n-----------------------------")
            for i in range(0,self.n_tst):
                print(i+1,self.Y_test[i],self.Y_tst_hat[i],sep=",")
            print("")
            print(f"Confusion Matrix (Test)\n----------------------------------")
            print(self.cf_tst)
            print("")
            print(f"Model Summary (Test)\n----------------------------------")
            print(f"Overall accuracy = {round(self.acc_tst,3)}")  
        else:
            sys.stdout = open(input("Enter the output file name to export: "),'w')
            print(f"ID, Actual class, Pred Prob (if logistic regression is chosen)\n-----------------------------")
            for i in range(0,self.n_tr):
                print(i+1,self.Y_train[i],round(self.Y_tr_prob.flatten()[i],3),sep=",")
            print("")
            print(f"Model Summary (Resubstitution)\n----------------------------------")
            print(f"Accuracy Ratio = {round(self.ar_tr,3)}")  
            print("") 
            print(f"ID, Actual class, Pred Prob (if logistic regression is chosen)\n-----------------------------")
            for i in range(0,self.n_tst):
                print(i+1,self.Y_test[i],round(self.Y_tst_prob.flatten()[i],3),sep=",")
            print("")
            print(f"Model Summary (Test)\n----------------------------------")
            print(f"Accuracy Ratio = {round(self.ar_tst,3)}")  
        
    