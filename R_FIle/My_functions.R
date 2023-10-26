find_large<-function(input_year){
  Largest_EXP<-gapminder %>% filter(year==input_year) %>% 
    select(country,lifeExp) %>% filter(lifeExp==max(lifeExp))
  Largest_EXP
}
add_F_column<-function(temps){
  temps %>% mutate(fahr=celsius*1.78+32)
}
range_cities <- function (temps) {
  increase( (temps %>% group_by(city) %>%
               summarize (mean_temp = mean (celsius)))$mean_temp)
}
aa<-function(gapminder){
  gapminder %>% group_by(country) %>% arrange(-year) %>% 
    summarize(latestlifeExp=firstelement(lifeExp),
              eariestlifeExp=lastelement(lifeExp),
              earliestyea=min(year),
              latestyear=max(year)) %>% mutate(avglife=(latestlifeExp-eariestlifeExp)/(earliestyea-latestyear))
           
}
latelifeExp<-function(g){
  g %>% arrange(-year)[1,'lifeExp']
}
firstelement<-function(col){
  col[1]
}
lastelement<-function(col){
  col[length(col)]
}