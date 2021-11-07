library(RMySQL) 
library(dplyr)
library(ggplot2)
library(reshape2)
library(gridExtra)
library(stringr)
library(rlang)
options(scipen=100)

con = dbConnect(MySQL(), host='203.252.196.68',
                dbname='sql1614681', user='db1614681', pass='stat1234')


all_price = dbGetQuery(con, statement="SELECT * FROM all_price ;")
all_detail = dbGetQuery(con, statement="SELECT * FROM all_details ;")
all_top = dbGetQuery(con, statement="SELECT * FROM all_top ;")

dbDisconnect(con)

#### all_price ####
str(all_price)
all_price$FINAL_PRICE<-as.numeric(all_price$FINAL_PRICE)
all_price$DISCOUNT_RATE<-as.numeric(all_price$DISCOUNT_RATE)

# 가격 범주화
summary(all_price$FINAL_PRICE)
table(all_price$FINAL_PRICE)
all_price['PRICE']<-ifelse(all_price$FINAL_PRICE==0,'Free',
                           ifelse(all_price$FINAL_PRICE<10000,'less than 1',
                                  ifelse(all_price$FINAL_PRICE<20000,'1',
                                         ifelse(all_price$FINAL_PRICE<30000,'2',
                                                ifelse(all_price$FINAL_PRICE<40000,'3',
                                                       ifelse(all_price$FINAL_PRICE<50000,'4','more than 5'))))))
table(all_price$PRICE)
all_price$PRICE<-factor(all_price$PRICE,levels=c('Free','less than 1','1','2','3','4','more than 5'))


# 할인율 범주화
summary(all_price$DISCOUNT_RATE)
table(all_price$DISCOUNT_RATE)
all_price['DISCOUNT']<-ifelse(all_price$DISCOUNT_RATE==0,'No discount',
                              ifelse(all_price$DISCOUNT_RATE<30,'1~29%',
                                     ifelse(all_price$DISCOUNT_RATE<50,'30~49%',
                                            ifelse(all_price$DISCOUNT_RATE<70,'50~69%',
                                                   ifelse(all_price$DISCOUNT_RATE<90,'70~89%','90%~')))))
all_price$DISCOUNT<-factor(all_price$DISCOUNT,levels=c('No discount','1~29%','30~49%','50~69%','70~89%','90%~'))
table(all_price$DISCOUNT)


#### all_detail ####
# 장르 1개씩만 추출
all_detail['GENRE']<-apply(all_detail['GENRE'],1,
                           function(x) {ifelse(unlist(strsplit(x,','))[1]=='Free to Play',
                                               unlist(strsplit(x,','))[2],
                                               unlist(strsplit(x,','))[1])})
head(all_detail)

# 평가 범주 정리
table(all_detail$RATINGS)
all_detail$RATINGS<-
  ifelse(all_detail$RATINGS %in% c('1 user reviews','3 user reviews','NA'),
         'Less than 3 reviews',
         all_detail$RATINGS)
all_detail$RATINGS<-factor(all_detail$RATINGS,
                           levels=c('Overwhelmingly Positive','Very Positive','Mostly Positive',
                                    'Mixed','Mostly Negative','Less than 3 reviews'))
# 발매일 범주 정리
table(all_detail$RELEASE_DATE)
all_detail$RELEASE_DATE<-
  apply(all_detail['RELEASE_DATE'], 1, 
        function(x){ifelse(x=='Coming Soon','After 2019',unlist(strsplit(x,', '))[2])}
  )
all_detail$RELEASE_DATE<-ifelse(all_detail$RELEASE_DATE<="2012","Before 2013",all_detail$RELEASE_DATE)
all_detail$RELEASE_DATE<-gsub('2020','After 2019',all_detail$RELEASE_DATE)
all_detail$RELEASE_DATE<-factor(all_detail$RELEASE_DATE,
                                levels=c("Before 2013","2013","2014","2015","2016","2017","2018","2019","After 2019"))
                           

#### all_price, all_detail 시각화 ####
# barchart 함수
plot_bar<-function(data,x,fill=NULL,color="Set3",desc=T){
  x <- enquo(x)
  fill <- enquo(fill)
  ggplot(data)+
    geom_bar(aes(x=!!x, fill=!!fill),color='white') +
    coord_flip() + 
    ggtitle(ifelse(quo_is_null(fill),
                   sprintf("%s",quo_name(x)),
                   sprintf("%s by %s",quo_name(x) ,quo_name(fill))
                   ))+                                                    
    theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
          legend.position = "none") +
    theme(legend.position = 'right') +
    scale_fill_brewer(palette = color,direction = ifelse(desc==T,-1,0))
}


# 시각화
str(all_price)
str(all_detail)

plot_bar(all_price[all_price$PRICE!='Free',],PRICE,DISCOUNT,color='PuBu')
plot_bar(all_price[all_price$PRICE!='Free',],PRICE,TYPE)

plot_bar(all_price[all_price$DISCOUNT!='No discount',],DISCOUNT,PRICE)
g1<-plot_bar(all_price,TYPE,PRICE,color='RdPu',desc=F)
g2<-plot_bar(all_price,TYPE,DISCOUNT,color='PuBu')
grid.arrange(g1,g2)


plot_bar(all_detail,GENRE,TYPE)
plot_bar(all_detail[all_detail$RATINGS!="Less than 3 reviews",],RELEASE_DATE,TYPE)
g1<-plot_bar(all_detail[all_detail$RATINGS!="Less than 3 reviews",],TYPE,RATINGS)
g2<-plot_bar(all_detail[all_detail$RATINGS!="Less than 3 reviews",],RATINGS,BUNDLE,color='Pastel1',desc=F)
g3<-plot_bar(all_detail[all_detail$RATINGS!="Less than 3 reviews",],GENRE,RATINGS)
grid.arrange(g3,g1)


# 검색 태그 시각화
library(wordcloud2)
library(htmlwidgets)
library(htmltools)
library(jsonlite)
library(yaml)
library(base64enc)

tag_vec_l = c()
tag_list = strsplit(all_detail[all_detail$TYPE=='longrun',]$POPULAR_TAGS,',')
for (i in c(1:length(tag_list))){
  tag_lis = str_trim(tag_list[[i]],'both')
  for (i in tag_lis){
    tag_vec_l<-c(tag_vec_l,i)
  }
}

tag_vec_r = c()
tag_list = strsplit(all_detail[all_detail$TYPE=='rising',]$POPULAR_TAGS,',')
for (i in c(1:length(tag_list))){
  tag_lis = str_trim(tag_list[[i]],'both')
  for (i in tag_lis){
    tag_vec_r<-c(tag_vec_r,i)
  }
}

tag_vec_t = c()
tag_list = strsplit(all_detail[all_detail$TYPE=='topseller',]$POPULAR_TAGS,',')
for (i in c(1:length(tag_list))){
  tag_lis = str_trim(tag_list[[i]],'both')
  for (i in tag_lis){
    tag_vec_t<-c(tag_vec_t,i)
  }
}

tag_vec = c()
tag_list = strsplit(all_detail$POPULAR_TAGS,',')
for (i in c(1:length(tag_list))){
  tag_lis = str_trim(tag_list[[i]],'both')
  for (i in tag_lis){
    tag_vec<-c(tag_vec,i)
  }
}

error_count<-table(tag_vec_r)
wordcloud2(error_count,rotateRatio = 0)


all_tag<-data.frame(tag=tag_vec,n=1) %>% 
  group_by(tag) %>% 
  summarise(n=n()) %>%
  mutate(bin=ifelse(n<6,'1~5',
                     ifelse(n<11,'6~10',
                            ifelse(n<40,'11~39',
                                   ifelse(n<70, '40~69', '70~'))))) %>% 
  arrange(desc(n))

table(all_tag$bin)

ggplot(subset(all_tag,n>20))+
  geom_col(aes(x=reorder(tag,n),y=n,fill=bin)) +
  coord_flip()+
  ggtitle("Popular Tag") +  
  labs(x="Popular tag",y='count')+
  theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
        legend.position = "none") +
  theme(legend.position = 'right')+
  scale_fill_brewer(palette = "RdYlBu", direction = -1)


#### all_top 시각화 ####
# 병합
all_top$DAY<-as.numeric(all_top$DAY)
all_top$TIME<-as.numeric(all_top$TIME)
all_top$CUR_USER<-as.numeric(all_top$CUR_USER)
all_top$PEAK_TODAY<-as.numeric(all_top$PEAK_TODAY)
all_top$RANK<-as.numeric(all_top$RANK)

names(all_top)
names(all_price)
names(all_detail)

all_top_p<-merge(all_top[,-c(1,8)], all_price[,c(2,9,10,7,6)], key='TITLE')
names(all_top_p)
unique(all_top_p$TITLE)

all_top_d<-merge(all_top[,-c(1,8)],all_detail[,-c(1,9)], key='TITLE')
names(all_top_d)
unique(all_top_d$TITLE)

# 빈도 수가 312인 게임만 추출(55개->48개)
sort(all_top_p$TITLE %>% table())
length(unique(all_top_p$TITLE))
name<-names(sort(all_top_p$TITLE %>% table()))[8:55] 

all_top_p<-all_top_p[all_top_p$TITLE %in% name,]
all_top_d<-all_top_d[all_top_d$TITLE %in% name,]

# 중복 제거
all_top_d<-all_top_d[!duplicated(all_top_d[,c('DAY','TIME','TITLE')]),]

str(all_top_p)
str(all_top_d)


# 정렬
all_top_p<-arrange(all_top_p, DAY,TIME, RANK)
all_top_d<-arrange(all_top_d, DAY,TIME, RANK)


# 그룹화한 시계열 그래프 함수
plot_user<-function(data, day=F, by=DAY, group, log=F){
  group <- enquo(group)
  by <- enquo(by)
  
  if(day!=F){
    df<-data[data$DAY==day,] %>% 
      group_by(!!by,!!group) %>%
      summarise(USER=mean(CUR_USER))
    ran<-c(0:24)
  }
  else{
    df<-data %>% 
      group_by(!!by,!!group) %>%
      summarise(USER=mean(CUR_USER))
    ran<-c(min(df[,1]):max(df[,1]))
  }
  
  
  if(log==T) df$USER = log(df$USER)
  
  g<-ggplot(df)+
    geom_line(aes(x=!!by,y=USER, color = !!group))+
    scale_x_continuous(breaks = ran,labels = ran)+
    geom_point(aes(x=!!by,y=USER, color = !!group))+
    ggtitle(ifelse(day!=F,
                   sprintf("2019-11-%s \n Current user by %s", quo_name(day), quo_name(group)),
                   sprintf("2019-11-17 ~ 2019-11-29 \n Current user by %s", quo_name(group))))+
    theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
          legend.position = "none")+
    theme(legend.position = 'top')
  
  return(g)
}


# main
g1<-plot_user(data=all_top_p, by=DAY, group=TYPE,log=T)
g2<-plot_user(data=all_top_p, day=24, by=TIME, group=TYPE,log=T)
grid.arrange(g1, g2, ncol=2)  

g1<-plot_user(data=all_top_d, by=DAY, group=GENRE,log=T)
g2<-plot_user(data=all_top_d, day=24, by=TIME, group=GENRE,log=T)
grid.arrange(g1, g2, ncol=2)  

g1<-plot_user(data=all_top_d, by=DAY, group=RATINGS,log=T)
g2<-plot_user(data=all_top_d, day=24, by=TIME, group=RATINGS,log=T)
grid.arrange(g1, g2, ncol=2)  
g1<-plot_user(data=all_top_p, by=DAY, group=PRICE, log=T)
g2<-plot_user(data=all_top_p, by=TIME, group=PRICE, log=T) 
grid.arrange(g1, g2, ncol=2)


plot_user(data=all_top_d, by=TIME, group=GENRE, log=T)
g2<-plot_user(data=all_top_d, by=TIME,group=RATINGS, log=T) 
g1<-plot_user(data=all_top_d, by=DAY,group=RATINGS, log=T) 
grid.arrange(g1, g2, ncol=2)


# 개별 게임 시각화
df_rank<-all_top_p %>% 
  group_by(TITLE) %>% 
  summarise(RANK = mean(RANK)) %>% 
  arrange(RANK) 
title_list<-df_rank$TITLE
title_list[1:2]
ran=c(17:29)

g1<-all_top_p %>% 
  group_by(DAY,TITLE) %>% 
  summarise(USER=mean(CUR_USER)) %>% 
  filter(TITLE %in% df_rank[1:3,]$TITLE) %>% 
  ggplot() +
  geom_line(aes(x=DAY,y=USER,color=TITLE))+
  geom_point(aes(x=DAY,y=USER,color=TITLE))+
  scale_x_continuous(breaks = ran,labels = ran)

g2<-all_top_p %>% 
  group_by(DAY,TITLE) %>% 
  summarise(USER=mean(CUR_USER)) %>% 
  filter(TITLE %in% df_rank[4:20,]$TITLE) %>% 
  ggplot() +
  geom_line(aes(x=DAY,y=USER,color=TITLE))+
  geom_point(aes(x=DAY,y=USER,color=TITLE))+
  scale_x_continuous(breaks = ran,labels = ran)

g3<-all_top_p %>% 
  group_by(DAY,TITLE) %>% 
  summarise(USER=mean(CUR_USER)) %>% 
  filter(TITLE %in% df_rank[21:37,]$TITLE) %>% 
  ggplot() +
  geom_line(aes(x=DAY,y=USER,color=TITLE))+
  geom_point(aes(x=DAY,y=USER,color=TITLE))+
  scale_x_continuous(breaks = ran,labels = ran)


g4<-all_top_p %>% 
  group_by(DAY,TITLE) %>% 
  summarise(USER=mean(CUR_USER)) %>% 
  filter(TITLE %in% df_rank[38:48,]$TITLE) %>% 
  ggplot() +
  geom_line(aes(x=DAY,y=USER,color=TITLE))+
  geom_point(aes(x=DAY,y=USER,color=TITLE))+
  scale_x_continuous(breaks = ran,labels = ran)

grid.arrange(g1,g2,g3,g4,ncol=2)
