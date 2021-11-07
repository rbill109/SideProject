setwd('C:/RStudy/데이터마이닝_최영근/project/최종 프로포절/codes')
options(scipen = 100)

library(dplyr)
library(ggplot2)
library(gridExtra)
library(caret)

f1<-function(cm){
  f1 = 
    2*cm$byClass[[2]]*cm$byClass[[4]]/(cm$byClass[[2]]+cm$byClass[[4]])
  return(f1)
}

# 
flights<-read.csv('flights.csv')
str(flights)

round(colSums(is.na(flights))/nrow(flights)*100,2)

head(flights, 1)

#### pre-processing
## 필요없는 변수 제거
flights_raw<-flights[,-c(1,6,14,16,19,26:31)]
names(flights_raw)

## 1차 파생변수 생성
flights_raw$DEP_15<-as.factor(ifelse(flights_raw$DEPARTURE_DELAY>=15,"1","0")) 
flights_raw$ARR_15<-as.factor(ifelse(flights_raw$ARRIVAL_DELAY>=15,"1","0"))
flights_raw$R_DEPARTURE_DELAY<-flights_raw$DEPARTURE_DELAY+flights_raw$TAXI_OUT
flights_raw$R_DEP_15<-as.factor(ifelse(flights_raw$R_DEPARTURE_DELAY>15,"1","0"))

## 결측치 처리 
# 회항/결항 항공편은 제거
subset(flights_raw, (is.na(TAXI_OUT))&(CANCELLED=="0")) # TAXI_OUT이 NA인 항공편은 모두 결항

subset(flights_raw, (is.na(TAXI_IN))&(CANCELLED=="0")) 
subset(flights_raw, (is.na(TAXI_IN))&(DIVERTED=="0"))
subset(flights_raw, (is.na(TAXI_IN))&(CANCELLED=="0")&(DIVERTED=="0")) # TAXI_IN이 NA인 항공편은 회항 혹은 결항

flights_na<-flights_raw[!is.na(flights_raw$TAXI_OUT),]
flights_na<-flights_raw[!is.na(flights_raw$TAXI_IN),]
colSums(is.na(flights_na))

subset(flights_na, (is.na(ARRIVAL_DELAY))&(CANCELLED=="0"))
subset(flights_na, (is.na(ARRIVAL_DELAY))&(DIVERTED=="0")) # ARRIVAL_DELAY가 NA인 항공편은 모두 회항
flights_na<-flights_raw[!is.na(flights_raw$ARRIVAL_DELAY),]

round(colSums(is.na(flights_na))/nrow(flights_na)*100,2)

flights_na<-flights_na[,-c(19:20)]

## 탑승객 수가 많은 상위 5개 공항만 샘플링
busy_port<-c('ATL','LAX','ORD','DFW','JFK')

d<-read.csv('L_AIRPORT_ID.csv_') %>% arrange(Description)
airports<-read.csv('airports.csv')
busy_p<-subset(airports, IATA_CODE %in% busy_port)
j=1
for (i in substr(busy_p$AIRPORT,1,20)){
  print(d[grep(i,d$Description),'Code'])
  j = j+1
}
busy_code<-c(10397,11057,11292,11298,12478)

for (i in c(1:11)){
  flights_na$ORIGIN_AIRPORT[flights_na$ORIGIN_AIRPORT==busy_code[i]] = busy_port[i]
  flights_na$DESTINATION_AIRPORT[flights_na$DESTINATION_AIRPORT==busy_code[i]] = busy_port[i]
}


# ATL 방향 고정
flights_busy<-
  flights_na[(flights_na$ORIGIN_AIRPORT=='ATL')|(flights_na$DESTINATION_AIRPORT=='ATL'),]

flights_s<-
  flights_busy[(flights_busy$ORIGIN_AIRPORT %in% busy_port)&
                 (flights_busy$DESTINATION_AIRPORT %in% busy_port),]

#### EDA 및 변수 정리
round(colSums(is.na(flights_s))/nrow(flights_s)*100,2)


## 수치형 변수
g1<-ggplot(flights_s) + 
  geom_boxplot(aes(y=TAXI_OUT)) + coord_flip()
g2<-ggplot(flights_s) + 
  geom_boxplot(aes(y=TAXI_IN)) + coord_flip()
grid.arrange(g1,g2)

ggplot(flights_s) + 
  geom_boxplot(aes(y=DISTANCE)) + coord_flip()

ggplot(flights_s) + 
  geom_boxplot(aes(y=AIR_TIME)) + coord_flip()

## 범주형 변수
str(flights_s)

# MONTH, DAY_OF_WEEK, AIRLINE
flights_s$DAY_OF_WEEK<-as.factor(flights_s$DAY_OF_WEEK)

table(flights_s$AIRLINE)
flights_s$AIRLINE<-as.factor(as.character(flights_s$AIRLINE))

p1<-ggplot(flights_s) +
  geom_bar(aes(x=MONTH,fill=ARR_15),position="fill") + coord_flip()
p2<-ggplot(flights_s) +
  geom_bar(aes(x=DAY_OF_WEEK,fill=ARR_15),position="fill") + coord_flip()
p3<-ggplot(flights_s) +
  geom_bar(aes(x=AIRLINE,fill=ARR_15),position="fill") + coord_flip()
grid.arrange(p1, p3, p2)

# TAIL_NUMBER
flights_s$TAIL_NUMBER<-as.factor(as.character(flights_s$TAIL_NUMBER))
table(flights_s$TAIL_NUMBER)[1]

# AIRPORT
p1<-ggplot(flights_s) +
  geom_bar(aes(x=ORIGIN_AIRPORT,fill=ARR_15),position="fill") + coord_flip()
p2<-ggplot(flights_s) +
  geom_bar(aes(x=DESTINATION_AIRPORT,fill=ARR_15),position="fill") + coord_flip()
grid.arrange(p1, p2)

flights_s$ORIGIN_AIRPORT<-as.factor(as.character(flights_s$ORIGIN_AIRPORT))
flights_s$DESTINATION_AIRPORT<-as.factor(as.character(flights_s$DESTINATION_AIRPORT))
table(flights_s$ORIGIN_AIRPORT);table(flights_s$DESTINATION_AIRPORT)

#### 파생변수 생성
# ORDER
flights_s<-flights_s %>% 
  arrange(MONTH, DAY, TAIL_NUMBER)

tib_tail<-flights_s %>% 
  group_by(MONTH, DAY, TAIL_NUMBER) %>% 
  summarise(n=n())
table(tib_tail$n)

j=1
n=0
for (i in c(1:nrow(flights_s))){
  if(flights_s$TAIL_NUMBER[i]==tib_tail$TAIL_NUMBER[j]){
    n=n+1
    flights_s$ORDER[i]<-n
  }
  else{
    flights_s$ORDER[i]<-1
    j=j+1
    n=1
  }
}
table(flights_s$ORDER)
flights_s$ORDER<-as.factor(flights_s$ORDER)

# FIRST
flights_s$FIRST<-as.factor(ifelse(flights_s$ORDER==1,"1","0"))
table(flights_s$FIRST)

save(flights_s,file="C:/RStudy/데이터마이닝_최영근/project/최종 프로포절/codes/flights_s.rda")


#### 
load('flights_s.rda')

str(flights_s)
names(flights_s)
flight<-flights_s[,-c(2,13,15,17:18)]
str(flight)
names(flight)

#### 상관분석
library(corrplot)
corrplot(cor(flight[,c(7:13,16)]),diag=FALSE,addCoef.col = "black",method="number")

#### 데이터셋 분할 및 클래스 불균형 조정
table(flight$ARR_15)

library(ROSE)
library(DMwR)  
table(flight$MONTH)

train_data<-flight[flight$MONTH<=9,]
test_data<-flight[flight$MONTH>=10,]

over_df <- 
  ovun.sample(ARR_15 ~ ., 
              data = train_data, 
              method = "over", 
              N = table(train_data$DEP_15)[1]*2)$data
under_df <- 
  ovun.sample(ARR_15 ~ ., 
              data = train_data, 
              method = "under", 
              N = table(train_data$DEP_15)[2]*2)$data
both_df <- 
  ovun.sample(ARR_15 ~ ., 
              data = train_data, 
              method = "both", 
              N = dim(train_data)[1]*2)$data

rose_df <- ROSE(ARR_15 ~ ., data = train_data)$data 

smote_df <- SMOTE(ARR_15 ~ ., data = train_data)

d = dim(train_data)[2]
rf <- ranger(
  formula = ARR_15 ~ . -MONTH , 
  data = na.omit(train_data), 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_1 <-ranger(
  formula = ARR_15 ~ . -MONTH, 
  data = over_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_2 <- ranger(
  formula = ARR_15 ~ . -MONTH, 
  data = under_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_3 <- ranger(
  formula = ARR_15 ~ . -MONTH, 
  data = both_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_4 <-ranger(
  formula = ARR_15 ~ . -MONTH, 
  data = rose_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_5 <-ranger(
  formula = ARR_15 ~ . -MONTH, 
  data = smote_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

prob_pred_rf<-predict(rf,data=test_data, type="response")$predictions
prob_pred_rf_1<-predict(rf_1,data=test_data, type="response")$predictions
prob_pred_rf_2<-predict(rf_2,data=test_data, type="response")$predictions
prob_pred_rf_3<-predict(rf_3,data=test_data, type="response")$predictions
prob_pred_rf_4<-predict(rf_4,data=test_data, type="response")$predictions
prob_pred_rf_5<-predict(rf_5,data=test_data, type="response")$predictions

cf = confusionMatrix(test_data$ARR_15, prob_pred_rf);f1(cf)
cf_1 = confusionMatrix(test_data$ARR_15, prob_pred_rf_1);f1(cf_1)
cf_2 = confusionMatrix(test_data$ARR_15, prob_pred_rf_2);f1(cf_2)
cf_3= confusionMatrix(test_data$ARR_15, prob_pred_rf_3);f1(cf_3)
cf_4= confusionMatrix(test_data$ARR_15, prob_pred_rf_4);f1(cf_4)
cf_5= confusionMatrix(test_data$ARR_15, prob_pred_rf_5);f1(cf_5)
tibble(over=f1(cf_1),under=f1(cf_2),both=f1(cf_3),rose=f1(cf_4),smote=f1(cf_5)) %>% View()

# MONTH 제거
names(over_df)
df.train = over_df[,-1]
names(df.train)
str(df.train)

#### 모형 선정
# Random Forest(ranger) 
d = dim(df.train)[2]
rf_t <-ranger(
  formula = ARR_15 ~ . -TAIL_NUMBER -FIRST, 
  data = df.train, 
  mtry = 2, 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

f1(confusionMatrix(test_data$ARR_15, predict(rf_t,data=test_data, type="response")$predictions))
rf_t$prediction.error
library(vip)
vip(rf_t, num_features=25)



## Single Tree(C50) 
library(C50)
cv<-function(cf){
  ind<-sample(rep(1:5,nrow(df.train)*0.1))
  error<-rep(0,5)
  for(i in 1:5){    
    test<-df.train[ind==i,]
    train<-df.train[ind!=i,]
    target<-df.train$ARR_15[ind==i]

    model<-C50::C5.0(ARR_15 ~ ., data=df.train, control=C5.0Control(CF=cf))
    pred<-predict(model, newdata=test, type="class")
    table<-table(target, as.factor(pred))
    error[i]<-1-sum(sum(table)-diag(table))/sum(table)  
    print(i)
  }
  return(mean(error))
}
cfvec<-as.data.frame(seq(from=0, to=1, length.out=10))
errorvec<-apply(cfvec,1,cv) # 5-fold cross-validation 10번 반복
opt.cf<-cfvec[which.min(errorvec),]

fit<-C5.0(ARR_15 ~ .,data=df.train, 
          control=C5.0Control(CF=opt.cf, minCases=200), winnow=T, trials=10)
cf_tree<-confusionMatrix(test_data$ARR_15, predict(fit, test_data[,-15], type = "class"))
f1(cf_tree) 



## Bagging(ipred) 
library(ipred)
library(rpart)
set.seed(1234)
bag.model<-ipred::bagging(ARR_15 ~ .,data=df.train, 
                          nbagg=100, 
                          control = rpart.control(minsplit = 2, cp = 0),
                          coob=TRUE) # OOB sample
bag.model$err # OOB err: 0.02899631
cf_bag<-confusionMatrix(test_data$ARR_15, predict(bag.model,test_data[,-15]))
f1(cf_bag) 


## Boosting(adabag) 
library(adabag)
set.seed(1234)
boost <- boosting(ARR_15 ~ .,data=df.train, 
                  nbagg = 100, 
                  mfinal = 5, # 반복횟수
                  control = rpart.control(minsplit = 2, cp = 0))
pred <- predict(boost, test_data, type = "class")
cf_bst<-confusionMatrix(as.factor(pred$class), test_data$ARR_15)
f1(cf_bst)


## Boosting(xgboost) 
# one-hot encoding
library(vtreat)
treatplan<-vtreat::designTreatmentsZ(df.train, setdiff(names(df.train), "ARR_15"), verbose = FALSE)
new_vars <- treatplan %>% 
  magrittr::use_series(scoreFrame) %>%    	
  dplyr::filter(code %in% c("clean", "lev")) %>%
  magrittr::use_series(varName)  

# train, test set에 적용
enc_train <- vtreat::prepare(treatplan, df.train, varRestriction = new_vars)
enc_test <- vtreat::prepare(treatplan, test_data, varRestriction = new_vars)

features_train <- as.matrix(enc_train)
features_test <- as.matrix(enc_test)

# fixed hyperparameter
library(xgboost)
b<-as.numeric(df.train$ARR_15) - 1

# hyperparameter tunning
library(ParamHelpers)
library(mlr)
getParamSet("classif.xgboost")

xg_set <- makeLearner("classif.xgboost", predict.type = "response")
trainTask<-makeClassifTask(data = cbind(enc_train,df.train['ARR_15']), target = "ARR_15")
set_cv <- makeResampleDesc("CV",iters = 5L) # 5-fold cross validation
xg_ps <- makeParamSet(
  makeIntegerParam("nrounds",lower=300,upper=600),
  makeIntegerParam("max_depth",lower=1,upper=10),
  makeNumericParam("lambda",lower=0,upper=1),
  makeNumericParam("eta", lower = 0.01, upper = 0.2),
  makeNumericParam("subsample", lower = 0.5, upper = 1),
  makeNumericParam("min_child_weight",lower=1,upper=5),
  makeNumericParam("colsample_bytree",lower = 0.5,upper = 1)
)
rancontrol <- makeTuneControlRandom(maxit = 5L) # search function

xg_tune <- tuneParams(learner = xg_set, 
                      task = trainTask, 
                      resampling = set_cv,
                      measures = mlr::f1,
                      par.set = xg_ps, 
                      control = rancontrol)
xg_tune$x

model <- xgboost(data = features_train, label = b, nrounds=585, max_depth=6, lambda=0.307932, eta=0.1521247, 
                 subsample=0.9082532, min_child_weight=2.846892, colsample_bytree=0.9480581,objective = "binary:logistic")

pred <- predict(model, features_test)

# best threshold 
thres_vec <- seq(0.05, 0.95, by=0.01)
acc_vec <- c()

for (thres in thres_vec){
  pred_class <- ifelse(pred>=thres, "1", "0")
  cm <- table(test_data$ARR_15, pred_class)
  acc <- 0
  acc <- acc + sum(diag(cm))/sum(cm)
  acc_vec <- c(acc_vec, acc)
}

thres_opt <- thres_vec[acc_vec == max(acc_vec)]

pred_class<-ifelse(pred>=thres_opt,1,0)
cf_xgb<-confusionMatrix(test_data$ARR_15, as.factor(pred_class))
f1(cf_xgb)

xgbImp1<-xgb.importance(model=model)
xgbImp1 <- xgbImp1 %>% mutate(rank = dense_rank(desc(Gain)))
xgbImp1 %>% View()
ggplot(data=xgbImp1[which(xgbImp1$rank <= 50),], aes(x = reorder(Feature, -Gain), y = Gain)) +
  geom_bar(stat="identity") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(title = "XG Boosted Feature Importance(Top 50)", x = "Features", y = "Information Gain") + coord_flip()

## SVM
library(e1071)
svm_model <- svm(ARR_15 ~., df.train)
svm.predictions <- predict(svm_model, test_data[,-15])
cf_svm<-confusionMatrix(data=svm.predictions, reference = test_data$ARR_15, positive="1")
f1(cf_svm)
