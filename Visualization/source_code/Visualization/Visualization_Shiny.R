library(shiny)
library(shinydashboard)
library(RMySQL) 
library(dplyr)
library(ggplot2)
library(reshape2)
library(gridExtra)
library(stringr)
library(rlang)


ui = dashboardPage(
    dashboardHeader(title = "Steam Stat"
    ),
    dashboardSidebar(
        sidebarSearchForm(textId="searchText",
                          buttonId="searchButton",
                          label="Search..."),
        menuItem("Dashboard", tabName="Dashboard",
                 icon=icon("dashboard")),
        menuItem("Charts", icon=icon("bar-chart-o"),
                 menuSubItem("bar chart", tabName="subitem1"),
                 menuSubItem("line chart", tabName="subitem2"))
    ),
    dashboardBody(
        tabBox(
            title="Charts",
            selected="",
            id="tabset1", height="900px", width="900px",
            
            tabPanel("Top100 by Day",
                     radioButtons(inputId = "g1_x",
                                  label = "Select the X axis",
                                  list("DAY", "TIME"),
                                  "DAY"),
                     radioButtons(inputId = "g1_y",
                                  label = "Select the Y axis",
                                  list("CUR_USER","RANK"),
                                  "CUR_USER"),
                     
                     actionButton(inputId="action",
                                  label="Apply"),
                     
                     splitLayout(
                         plotOutput(outputId = "g1"),
                         plotOutput(outputId = "g2")),
                     
                     splitLayout( 
                         plotOutput(outputId = "g3"),
                         plotOutput(outputId = "g4"))
                     
            ),
            
            tabPanel("Top100 by Time",
                     numericInput(inputId = "g_day", label = "Select the Day", value=17),
                     radioButtons(inputId = "g_y",
                                  label = "Select the Y axis",
                                  list("CUR_USER","RANK"),
                                  "CUR_USER"),
                     
                     actionButton(inputId="action",
                                  label="Apply"),
                     
                     splitLayout(
                         plotOutput(outputId = "g_1"),
                         plotOutput(outputId = "g_2")),
                     
                     splitLayout( 
                         plotOutput(outputId = "g_3"),
                         plotOutput(outputId = "g_4"))
                     
            ),
            
            tabPanel("Steam Users",
                     fluidPage(
                         numericInput(inputId = "gg_day", label = "Select the Day", value=17),
                         selectInput(inputId="gg_group",
                                     "1. Select the variable for group by:",
                                     choices=c("PRICE", "DISCOUNT", "TYPE"),
                                     selectize=FALSE),
                         actionButton(inputId="action",
                                      label="Apply"),
                         splitLayout(
                             plotOutput(outputId = "gg1"),
                             plotOutput(outputId = "gg2"))
                        
                     )
            ),
            
            tabPanel("Bar chart",
                     fluidPage(
                         fluidRow(
                         column(width=4,
                                selectInput(inputId = "b1_x",
                                            label = "Select the X axis",
                                            choices=c("PRICE", "DISCOUNT", "TYPE"),
                                            selectize=FALSE),
                                selectInput(inputId = "b1_group",
                                            label = "Select the group",
                                            choices=c("PRICE", "DISCOUNT", "TYPE"),
                                            selectize=FALSE) ,
                                selectInput(inputId = "b1_color",
                                            label = "Select the color",
                                            choices=c("PuBu", "RdPu", "Set3", "Pastel1"),
                                            selectize=FALSE),
                                plotOutput(outputId = "b1")),
                         ),
                         
                         fluidRow(
                             column(width=4,
                                    selectInput(inputId = "b2_x",
                                                label = "Select the X axis",
                                                choices=c("TYPE", "GENRE", 
                                                          "RATINGS", "RELEASE_DATE","BUNDLE"),
                                                selected=1, selectize=FALSE),
                                    selectInput(inputId = "b2_group",
                                                label = "Select the group",
                                                choices=c("TYPE", "GENRE", 
                                                          "RATINGS", "RELEASE_DATE","BUNDLE"),
                                                selected=2, selectize=FALSE) ,
                                    selectInput(inputId = "b2_color",
                                                label = "Select the color",
                                                choices=c("PuBu", "RdPu", "Set3", "Pastel1"),
                                                selectize=FALSE),
                                    plotOutput(outputId = "b2"))
                         ))
            )
        )
    )
)



server = function(input, output) {
    con = dbConnect(MySQL(), host='203.252.196.68',
                    dbname='sql1614681', user='db1614681', pass='stat1234')
    
    all_price= reactive({
        input$action
        con = dbConnect(MySQL(), host='203.252.196.68',
                        dbname='sql1614681', user='db1614681', pass='stat1234')
        res = dbGetQuery(con, statement="SELECT * FROM all_price ;")        
        dbDisconnect(con)
        
        # type conversion
        res$FINAL_PRICE<-as.numeric(res$FINAL_PRICE)
        res$DISCOUNT_RATE<-as.numeric(res$DISCOUNT_RATE)
        
        # PRICE
        res['PRICE']<-ifelse(res$FINAL_PRICE==0,'Free',
                             ifelse(res$FINAL_PRICE<10000,'less than 1',
                                    ifelse(res$FINAL_PRICE<20000,'1',
                                           ifelse(res$FINAL_PRICE<30000,'2',
                                                  ifelse(res$FINAL_PRICE<40000,'3',
                                                         ifelse(res$FINAL_PRICE<50000,'4','more than 5'))))))
        res$PRICE<-factor(res$PRICE,levels=c('Free','less than 1','1','2','3','4','more than 5'))
        
        # DISCOUNT
        res['DISCOUNT']<-ifelse(res$DISCOUNT_RATE==0,'No discount',
                                ifelse(res$DISCOUNT_RATE<30,'1~29%',
                                       ifelse(res$DISCOUNT_RATE<50,'30~49%',
                                              ifelse(res$DISCOUNT_RATE<70,'50~69%',
                                                     ifelse(res$DISCOUNT_RATE<90,'70~89%','90%~')))))
        res$DISCOUNT<-factor(res$DISCOUNT,levels=c('No discount','1~29%','30~49%','50~69%','70~89%','90%~'))
        return(res)
    })
    
    all_detail= reactive({
        input$action
        con = dbConnect(MySQL(), host='203.252.196.68',
                        dbname='sql1614681', user='db1614681', pass='stat1234')
        res = dbGetQuery(con, "SELECT * FROM all_details;")        
        dbDisconnect(con)
        
        # GENRE
        res['GENRE']<-apply(res['GENRE'],1,function(x) {unlist(strsplit(x,','))[1]})
        
        # RATINGS
        res$RATINGS<-
            ifelse(res$RATINGS %in% c('1 user reviews','3 user reviews','NA'),
                   'Less than 3 reviews',
                   res$RATINGS)
        res$RATINGS<-factor(res$RATINGS,
                            levels=c('Overwhelmingly Positive','Very Positive','Mostly Positive',
                                     'Mixed','Mostly Negative','Less than 3 reviews'))
        
        # RELEASE_DATE
        res$RELEASE_DATE<-
            apply(res['RELEASE_DATE'], 1, 
                  function(x){ifelse(x=='Coming Soon','After 2019',unlist(strsplit(x,', '))[2])}
            )
        res$RELEASE_DATE<-ifelse(res$RELEASE_DATE<="2012","Before 2013",res$RELEASE_DATE)
        res$RELEASE_DATE<-gsub('2020','After 2019',res$RELEASE_DATE)
        return(res)
    })
    
    all_top= reactive({
        input$action
        con = dbConnect(MySQL(), host='203.252.196.68',
                        dbname='sql1614681', user='db1614681', pass='stat1234')
        res = dbGetQuery(con, statement="SELECT * FROM all_top ;")        
        dbDisconnect(con)
        
        # type conversion
        res$DAY<-as.numeric(res$DAY)
        res$TIME<-as.numeric(res$TIME)
        res$CUR_USER<-as.numeric(res$CUR_USER)
        res$PEAK_TODAY<-as.numeric(res$PEAK_TODAY)
        res$RANK<-as.numeric(res$RANK)
        return(res)
    })
    
    all_top_p= reactive({
        input$action
        res = merge(all_top()[,-c(1,8)], all_price()[,c(2,9,10,7,6)], key='TITLE')
        name<-names(sort(res$TITLE %>% table()))[8:55] 
        res<-res[res$TITLE %in% name,]
        res<-arrange(res,DAY,TIME, RANK)
        return(res)
    })
    
    all_top_d= reactive({
        input$action
        res = merge(all_top()[,-c(1,8)],all_detail()[,-c(1,9)], key='TITLE')
        name<-names(sort(res$TITLE %>% table()))[8:55] 
        res<-res[all_top_d$TITLE %in% name,]
        res<-res[!duplicated(res[,c('DAY','TIME','TITLE')]),]
        res<-arrange(res,DAY,TIME, RANK)
        return(res)
    })
    
    df_rank=reactive({
        input$action
        res<-all_top_p() %>% 
            group_by(TITLE) %>% 
            summarise(RANK = mean(RANK)) %>% 
            arrange(RANK) 
        return(res)
    })
    
    # Top100 by Day
    output$g1 = renderPlot({
        all_top_p()%>%
            group_by(!!as.name(input$g1_x),TITLE) %>%
            summarise(USER=mean(!!as.name(input$g1_y))) %>%
            filter(TITLE %in% df_rank()[1:3,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))+
            geom_point(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g2 = renderPlot({
        all_top_p() %>%
            group_by(!!as.name(input$g1_x),TITLE) %>%
            summarise(USER=mean(!!as.name(input$g1_y))) %>%
            filter(TITLE %in% df_rank()[4:20,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))+
            geom_point(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g3 = renderPlot({
        all_top_p() %>%
            group_by(!!as.name(input$g1_x),TITLE) %>%
            summarise(USER=mean(!!as.name(input$g1_y))) %>%
            filter(TITLE %in% df_rank()[21:37,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))+
            geom_point(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g4 = renderPlot({
        all_top_p() %>%
            group_by(!!as.name(input$g1_x),TITLE) %>%
            summarise(USER=mean(!!as.name(input$g1_y))) %>%
            filter(TITLE %in% df_rank()[38:48,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))+
            geom_point(aes(x=!!as.name(input$g1_x),y=USER,color=TITLE))
    },height = 400,width = 800)
    
    # Top100 by Time
    output$g_1 = renderPlot({
        all_top_p()[all_top_p()$DAY==input$g_day,] %>%
            group_by(TIME,TITLE) %>%
            summarise(USER=mean(!!as.name(input$g_y))) %>%
            filter(TITLE %in% df_rank()[1:3,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=TIME,y=USER,color=TITLE))+
            geom_point(aes(x=TIME,y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g_2 = renderPlot({
        all_top_p()[all_top_p()$DAY==input$g_day,] %>%
            group_by(TIME,TITLE) %>%
            summarise(USER=mean(!!as.name(input$g_y))) %>%
            filter(TITLE %in% df_rank()[4:20,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=TIME,y=USER,color=TITLE))+
            geom_point(aes(x=TIME,y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g_3 = renderPlot({
        all_top_p()[all_top_p()$DAY==input$g_day,] %>%
            group_by(TIME,TITLE) %>%
            summarise(USER=mean(!!as.name(input$g_y))) %>%
            filter(TITLE %in% df_rank()[21:37,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=TIME,y=USER,color=TITLE))+
            geom_point(aes(x=TIME,y=USER,color=TITLE))
    },height = 400,width = 800)
    
    output$g_4 = renderPlot({
        all_top_p()[all_top_p()$DAY==input$g_day,] %>%
            group_by(TIME,TITLE) %>%
            summarise(USER=mean(!!as.name(input$g_y))) %>%
            filter(TITLE %in% df_rank()[38:48,]$TITLE) %>%
            ggplot() +
            geom_line(aes(x=TIME,y=USER,color=TITLE))+
            geom_point(aes(x=TIME,y=USER,color=TITLE))
    },height = 400,width = 800)
    
    # Steam Users
    output$gg1 = renderPlot({
        all_top_p()[all_top_p()$DAY==input$gg_day,] %>% 
            group_by(TIME,!!as.name(input$gg_group)) %>%
            summarise(USER=mean(CUR_USER)) %>% 
            ggplot()+
            geom_line(aes(x=TIME,y=USER, color = !!as.name(input$gg_group)))+
            geom_point(aes(x=TIME,y=USER, color = !!as.name(input$gg_group)))+
            ggtitle(sprintf("2019-11-%s \n Current user by %s", input$gg_day, input$gg_group))+
            theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
                  legend.position = "none")+
            theme(legend.position = 'top')
    },height = 400,width = 800)
    
    output$gg2 = renderPlot({
        all_top_p() %>% 
            group_by(DAY,!!as.name(input$gg_group)) %>%
            summarise(USER=mean(CUR_USER)) %>% 
            ggplot()+
            geom_line(aes(x=DAY,y=USER, color = !!as.name(input$gg_group)))+
            geom_point(aes(x=DAY,y=USER, color = !!as.name(input$gg_group)))+
            ggtitle(sprintf("2019-11-17 ~ 2019-11-29 \n Current user by %s", input$gg_group))+
            theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
                  legend.position = "none")+
            theme(legend.position = 'top')
    },height = 400,width = 800)
    
    # bar chart
    output$b1 = renderPlot({
        input$action
        ggplot(all_price())+
            geom_bar(aes(x=!!as.name(input$b1_x), fill=!!as.name(input$b1_group)),color='white') +
            coord_flip() + 
            ggtitle(sprintf("%s by %s",input$b1_x ,input$b1_group))+                                                    
            theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
                  legend.position = "none") +
            theme(legend.position = 'right') +
            scale_fill_brewer(palette = input$b1_color,direction = -1)
    },height = 400,width = 800)
    
    output$b2 = renderPlot({
        input$action
        ggplot(all_detail())+
            geom_bar(aes(x=!!as.name(input$b2_x), fill=!!as.name(input$b2_group)),color='white') +
            coord_flip() + 
            ggtitle(sprintf("%s by %s",input$b2_x ,input$b2_group))+                                                    
            theme(plot.title=element_text(face = "bold", hjust = 0.5, size = 15),
                  legend.position = "none") +
            theme(legend.position = 'right') +
            scale_fill_brewer(palette = input$b2_color,direction = -1)
    },height = 400,width = 800)
    
    
    
}

shinyApp(ui = ui, server = server)