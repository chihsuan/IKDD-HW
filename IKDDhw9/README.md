Homework9
=======
## Statistics with R
 
R is a powerful tool for data analysis, but its learning curve is steeper than other tools. Here we try to provide a small case for practice. About this HW, there are only two variables, called X & Y.  You can easily draw X - Y plot in R to quickly see the relation of them. In fact, X & Y come from a known model. This HW needs you to “GUESS”  that model. One way to evaluate the underlying model is to create a proper fitting curve for pairs of X & Y. So, the job in this HW is to find a proper fitting curve. We will use “RMSE” to measure goodness of your “GUESS” to the model. You have to feedback your R code, predicted Y-value, and graph of fitting curve.

Remember that a jagged fitting curve may imply over-fitting, and will usually not obtain a good predict model. Believe that you will learn basic R skills via this small case.  

## Dataset

Data is put on: http://www.datagarage.io/datasets/ktchuang/Zg9uEiBf0L/ZuNjSOc4dL

## Download

You can use the below command in R to download data.

```r
data<-read.table(url("http://www.datagarage.io/api/5488687d9cbc60e12d300ba5"))
( Data pre-processing:
o<-seq(2, 4000, by=2)
d_c<-as.character(data[o, ])
p_m<-sapply(strsplit(d_c[], ""), function(d_c) which(d_c == ":"))
data<-data.frame(X=as.double(substr(d_c,p_m[2,]+1, 38)), Y=as.double(substr(d_c,p_m[1,]+1, 17)))
plot(data)
)
```
