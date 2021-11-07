library(RMySQL) 
library(dplyr)
options(scipen=100)

con = dbConnect(MySQL(), host='203.252.196.68',
                dbname='sql1614681', user='db1614681', pass='stat1234')

all_price = dbGetQuery(con, statement="SELECT * FROM all_price ;")
all_detail = dbGetQuery(con, statement="SELECT * FROM all_details ;")
top100 = dbGetQuery(con, statement="SELECT * FROM cpt_top100 ;")


dbDisconnect(con)


#### top100 ####
# RANK 추가
top100['RANK']<-rep(c(1:100),nrow(top100)/100)
top100 %>% head(10)

# all_price 게임만 추출
top100_p<-subset(top100, TITLE %in% unique(all_price$TITLE))

# TIME_OF_CRAWL 2개 컬럼으로 분리
top100_p['DATE'] = apply(top100_p['TIME_OF_CRAWL'],1,
                         function(x) {unlist(strsplit(x,' '))[1]})
top100_p['TIME'] = apply(top100_p['TIME_OF_CRAWL'],1,
                         function(x) {unlist(strsplit(x,' '))[2]})

# PRICE_ID 생성
cpt100<-merge(top100_p[,c('DATE','TIME','TITLE','RANK','CUR_USER','PEAK_TODAY')],all_price[,c('TITLE','ID')],key='TITLE')

all_top<-subset(cpt100, (DATE>="2019-11-17")&(DATE<="2019-11-29")) 
all_top<-arrange(all_top, DATE,TIME,RANK)
names(all_top)<-c("TITLE","DATE","TIME","RANK","CUR_USER","PEAK_TODAY","PRICE_ID")

# DAY 생성, TIME 변경 
all_top['DAY'] = apply(all_top['DATE'],1,
                       function(x) {unlist(strsplit(x,'-'))[3]})
all_top['TIME'] = apply(all_top['TIME'],1,
                        function(x) {unlist(strsplit(x,':'))[1]})
all_top<-all_top[,c('DAY','TIME','TITLE','RANK','CUR_USER','PEAK_TODAY','PRICE_ID')]

all_top$PEAK_TODAY<-as.numeric(all_top$PEAK_TODAY)
all_top$CUR_USER<-as.numeric(all_top$CUR_USER)
all_top$TIME<-as.numeric(all_top$TIME)
all_top$DAY<-as.numeric(all_top$DAY)

# 저장
all_top$RANK<-as.character(all_top$RANK)
all_top$PRICE_ID<-as.character(all_top$PRICE_ID)

con = dbConnect(MySQL(), host='203.252.196.68',
                dbname='sql1614681', user='db1614681', pass='stat1234')

dbWriteTable(con, "all_top",
             all_top,
             overwrite = F, append = T,
             row.names = F)
dbDisconnect(con)





