# The Effect of Weather Conditions on OPS in Major League Baseball during the 2021 Season (04/01 - 10/04)
### Brian Ozawa Burns, Nicholas Elich
Jul 2022

We were curious to understand the impact of various weather conditions on OPS (On Base Percentage plus Slugging Percentage) in the Major League Baseball season of 2021. To do this, we pulled data from Weatherbit.io at the 30 ballpark locations across the United States and Canada. From there, we compiled a data file containing OPS, Temperature, Precipitation, Wind Speed, Humidity, Pressure, Cloud Coverage, and UV (a less likely influence on OPS). Using this data, we constructed three models - a Multiple Linear Regression, Lasso Regression, and Random Forest - which all outputted error values of about 0.2. Based on our findings, we concluded that most weather conditions tested had little to no impact on OPS in the 2021 MLB season. The one variable that did, however, was temperature which, according to our Multiple Linear Regression model, had a t-statistic of 1.973 and a corresponding p-value of 
0.049. Using a significance level of 0.05, we were able to conclude that temperature had an effect on OPS in the 2021 MLB season.

```
We would like to thank Ken Jee for his instructional resources online here:
https://www.youtube.com/c/KenJee1
In addition, we would like to recognize Fangraphs.com for their freely available sets of data
which we could not have done the project without:
https://www.fangraphs.com/
```

Below are some images of our findings:  

<img width="484" alt="Screen Shot 2022-09-03 at 5 35 45 PM" src="https://user-images.githubusercontent.com/73633726/188292993-6d2db90e-a354-4715-b836-bf41db9ff0ba.png">


Error graph:  

<img width="692" alt="Screen Shot 2022-09-03 at 5 35 03 PM" src="https://user-images.githubusercontent.com/73633726/188293001-d8fff99f-51de-430d-a07d-33239c9cf426.png">
