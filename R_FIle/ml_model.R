library(gapminder)
library(dplyr)
library(tidyverse)
library(babynames)
model1<-lm(lifeExp ~ gdpPercap, data = gapminder)
preds1<-predict(model1,newdata=gapminder)
sum((gapminder$lifeExp-preds1)**2)

plot(gapminder$lifeExp,preds1)

model2<-lm(lifeExp ~ log(gdpPercap), data = gapminder)
preds2<-predict(model2,newdata=gapminder)
sum((gapminder$lifeExp-preds2)**2)

plot(gapminder$lifeExp,preds2)

model3<-lm(lifeExp ~ log(gdpPercap) + continent, data = gapminder)
preds3<-predict(model3,newdata=gapminder)
sum((gapminder$lifeExp-preds3)**2)


model_ti<-glm(Survived ~ Sex + Age + Pclass, family = "binomial",data = Titanic)