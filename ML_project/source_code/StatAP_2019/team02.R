setwd("C:/Rstudy/통계분석실습_노호석/data/")
temp = read.csv("train.csv", header = T)

options(scipen=100)
library(ROSE)
library(dplyr)
library(ggplot2)
library(caret)
library(gridExtra)
library(vip)
library(ranger)
library(plotROC)
library(pROC)
f1<-function(cm){
  f1 = 
    2*cm$byClass[[2]]*cm$byClass[[4]]/(cm$byClass[[2]]+cm$byClass[[4]])
  return(f1)
}
#### 전처리 ####
#-------- 결측치 처리 --------
colSums(is.na(temp))
### outcome: 융자 상태(1 = 미납, 0 = 완납)
prop.table(table(is.na(temp$outcome)))*100 
# outcome이 NA인 행은 제거
train_data <- subset(temp, !is.na(outcome))

# 어떤 열에 결측치가 있는지 확인 
colSums(is.na(train_data)) # "NewExist"

### NewExist: 신생사업 여부(1 = 기존사업, 2 = 신생사업)
table(is.na(train_data$NewExist))
train_data<-na.omit(train_data)
prop.table(table(train_data$NewExist))*100 
# 0은 description상 범주에 없는 레벨이나 제거 X


#-------- 데이터타입 변경 --------
# numeric to factor
train_data$outcome <- as.factor(train_data$outcome)
train_data$NewExist <- as.factor(train_data$NewExist)
# UrbanRural: (1 =  도시, 2 = 시골, 0 =  undefined)
train_data$UrbanRural <- as.factor(train_data$UrbanRural)

# factor to numeric & remove '$'
# GrAppv: 총 융자금
train_data$GrAppv <- as.numeric(gsub("[\\$,]", "", train_data$GrAppv))    
# SBA_Appv: SBA 융자금(GrAppv에서 약 75% 부담)
train_data$SBA_Appv <- as.numeric(gsub("[\\$,]", "", train_data$SBA_Appv)) 
# DisbursementGross : 실제 총 지불금액
train_data$DisbursementGross <- as.numeric(gsub("[\\$,]", "", train_data$DisbursementGross))

# factor to date 
Sys.setlocale("LC_TIME","English") 
# format(Sys.Date(),"%Y-%B-%d-%A")
# ApprovalDate: 대출만기일
train_data$ApprovalDate <- as.Date(as.character(train_data$ApprovalDate),"%d-%b-%y")

### DisbursementDate: 지급일 
# 값이 아예 입력되지 않은 경우(space bar)가 존재함
table(train_data$DisbursementDate)[1]
train_data$DisbursementDate <- as.Date(as.character(train_data$DisbursementDate),"%d-%b-%y")
sum(is.na(train_data$DisbursementDate))
# type conversion으로 NA가 생김
train_data <- subset(train_data, !is.na(DisbursementDate))

# RevLineCr: 회전한도대출 여부(Y = Yes, N = No)
table(train_data$RevLineCr)
train_data$RevLineCr<-as.character(train_data$RevLineCr)
train_data$RevLineCr<-ifelse(train_data$RevLineCr %in% c("Y","N","0"),train_data$RevLineCr, "0")
train_data$RevLineCr<-as.factor(train_data$RevLineCr)

# LowDoc: LowDoc 대출 가능 여부(Y = Yes, N = No)
table(train_data$LowDoc)
train_data$LowDoc<-as.character(train_data$LowDoc)
train_data$LowDoc<-ifelse(train_data$LowDoc %in% c("Y","N","0"),train_data$LowDoc, "0")
train_data$LowDoc<-as.factor(train_data$LowDoc)

# ApprovalFY : 회계연도
# FY 1997 = 1996/10/1 ~ 1997/09/30
table(train_data$ApprovalFY) # 1976A가 있음(1976의 오타로 보임)
train_data$ApprovalFY <- gsub("1976A","1976",train_data$ApprovalFY)
train_data$ApprovalFY<-as.factor(train_data$ApprovalFY)


#### 파생변수 생성 ####
# NAICS2: NAICS에서 2자리만 추출
train_data$NAICS2 <- substr(train_data$NAICS, 1, 2)

train_data$NAICS2<-gsub("32","31",train_data$NAICS2)
train_data$NAICS2<-gsub("33","31",train_data$NAICS2)
train_data$NAICS2<-gsub("45","44",train_data$NAICS2)
train_data$NAICS2<-gsub("49","48",train_data$NAICS2)
train_data$NAICS2<-as.factor(train_data$NAICS2)

# Real Estate: Term이 240개월 이상이면 부동산담보대출로 간주
train_data$RealEstate<-ifelse(train_data$Term>=240, "1", "0")
train_data$RealEstate<-as.factor(train_data$RealEstate)

# Portion: GrAppv 대비 SBA_Appv의 비율
train_data$Portion<-round((train_data$SBA_Appv/train_data$GrAppv), 3)

# Financrisis: 경제 대공황 시기에 포함되는지의 여부
train_data$Financrisis<-
  ifelse((train_data$DisbursementDate>="2007-12-01")&(train_data$DisbursementDate<="2009-06-30"),"1","0")
train_data$Financrisis<-as.factor(train_data$Financrisis)

# industry: 위험에 따른 산업군 분류
train_data$industry <- ifelse(train_data$NAICS2 %in% c("11","12","22","51","55","61","62"), "low", 
                   ifelse(train_data$NAICS2 %in% c("42","44","48"), "high", "moderate"))
train_data$industry<-as.factor(train_data$industry)

str(train_data)


#### EDA ####
# DisbursementGross
ggplot(train_data) +
  geom_boxplot(aes(x=outcome, y=DisbursementGross)) + coord_flip()
ggplot(train_data) +
  geom_boxplot(aes(x=outcome, y=log(DisbursementGross))) + coord_flip()


# NAICS2, indutry
ggplot(train_data) +
  geom_bar(aes(x=NAICS2,fill=outcome),position='fill')

ggplot(train_data) +
  geom_bar(aes(x=industry,fill=outcome),position='fill')

# NewExist, UrbanRural
p1<-ggplot(train_data)+
  geom_bar(aes(x=NewExist, fill=outcome), position="fill") + coord_flip()
p2<-ggplot(train_data)+
  geom_bar(aes(x=UrbanRural, fill=outcome), position="fill") + coord_flip()
grid.arrange(p1, p2, nrow=2)

# RevLineCr and LowDoc
p1<-ggplot(train_data)+
  geom_bar(aes(x=RevLineCr, fill=outcome), position="fill") + coord_flip()
p2<-ggplot(train_data)+
  geom_bar(aes(x=LowDoc, fill=outcome), position="fill") + coord_flip()
grid.arrange(p1, p2, nrow=2)

# RealEstate and Financrisis
p1<-ggplot(train_data)+
  geom_bar(aes(x=RealEstate, fill=outcome), position="fill") + coord_flip()
p2<-ggplot(train_data)+
  geom_bar(aes(x=Financrisis, fill=outcome), position="fill") + coord_flip()
grid.arrange(p1, p2, nrow=2)


#### Imbalanced class ####
set.seed(1234)
train.index <- sample(c(1:NROW(train_data)),NROW(train_data)*0.9)
train.data<-train_data[train.index,]
valid.data<-train_data[-train.index,]

over_df <- 
  ovun.sample(outcome ~ ., 
              data = train.data, 
              method = "over", 
              N = table(train.data$outcome)[[1]]*2)$data
under_df <- 
  ovun.sample(outcome ~ ., 
              data = train.data, 
              method = "under", 
              N = table(train.data$outcome)[[2]]*2)$data
both_df <- 
  ovun.sample(outcome ~ ., 
              data = train.data, 
              method = "both", 
              N = dim(train.data)[1]*2)$data

train.rose<-train.data
train.rose$DisbursementDate<-as.factor(as.character(train.rose$DisbursementDate))
train.rose$ApprovalDate<-as.factor(as.character(train.rose$ApprovalDate))
train.rose$ApprovalFY<-as.factor(train.rose$ApprovalFY)
train.rose$NAICS2<-as.factor(train.rose$NAICS2)
rose_df <- ROSE(outcome ~ ., data = train.rose)$data 

d=dim(train.data)[2]

rf <- ranger(
  formula = outcome ~ ., 
  data = na.omit(train.data), 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')

rf_1 <-ranger(
  formula = outcome ~ ., 
  data = over_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')


rf_2 <- ranger(
  formula = outcome ~ ., 
  data = under_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')


rf_3 <- ranger(
  formula = outcome ~ ., 
  data = both_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')


rf_4 <-ranger(
  formula = outcome ~ ., 
  data = rose_df, 
  mtry = sqrt(d), 
  num.trees = 1000, 
  seed = 10, 
  respect.unordered.factors = 'order',
  classification=TRUE, 
  importance = 'impurity')


prob_pred_rf<-predict(rf,data=na.omit(valid.data), type="response")$predictions
prob_pred_rf_1<-predict(rf_1,data=na.omit(valid.data), type="response")$predictions
prob_pred_rf_2<-predict(rf_2,data=na.omit(valid.data), type="response")$predictions
prob_pred_rf_3<-predict(rf_3,data=na.omit(valid.data), type="response")$predictions
prob_pred_rf_3<-predict(rf_4,data=na.omit(valid.data), type="response")$predictions

cf = confusionMatrix(na.omit(valid.data)$outcome, prob_pred_rf);f1(cf)
cf_1 = confusionMatrix(na.omit(valid.data)$outcome, prob_pred_rf_1);f1(cf_1)
cf_2 = confusionMatrix(na.omit(valid.data)$outcome, prob_pred_rf_2);f1(cf_2)
cf_3= confusionMatrix(na.omit(valid.data)$outcome, prob_pred_rf_3);f1(cf_3)
cf_4= confusionMatrix(na.omit(valid.data)$outcome, prob_pred_rf_4);f1(cf_4)


#### fitting model ####
load('test_refined.rda') # Kaggle에 올라온 test.csv를 전처리

mdl_rf = ranger(outcome ~ . -Id -DisbursementDate -industry -LowDoc -NewExist -ApprovalDate,
                  data=over_df, mtry = 6, num.trees = 1000, 
                  seed = 10, respect.unordered.factors = 'order',
                  classification=TRUE, importance = 'impurity')

yhat_rf = predict(mdl_rf, data=test, type="response")$predictions
mdl_rf$prediction.error

head(importance(mdl_rf))
vip(mdl_rf, num_features=25)  


#### Leaderboard ####
test.data<-read.csv('answer_key.csv') # 스노보드에 올라온 정답 데이터셋의 real values
pri_idx<-row.names(test.data[test.data$Usage=='Private',])
pub_idx<-row.names(test.data[test.data$Usage!='Private',])
yhat<-read.csv('final.csv') # Kaggle에서 최종 채택된 모델의 predicted values

cf_rf_pub = confusionMatrix(as.factor(test.data[pub_idx,'outcome']), as.factor(yhat[pub_idx,'outcome']));f1(cf_rf_pub)
cf_rf_pri = confusionMatrix(as.factor(test.data[pri_idx,'outcome']), as.factor(yhat[pri_idx,'outcome']));f1(cf_rf_pri)
confusionMatrix(as.factor(test.data[pub_idx,'outcome']), as.factor(yhat[pub_idx,'outcome']))$byClass[['Specificity']]

                