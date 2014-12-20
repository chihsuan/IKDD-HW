data<-read.table(url("http://www.datagarage.io/api/5488687d9cbc60e12d300ba5"))


o<-seq(2, 4000, by=2)
d_c<-as.character(data[o, ])
p_m<-sapply(strsplit(d_c[], ""), function(d_c) which(d_c == ":"))
data<-data.frame(X=as.double(substr(d_c,p_m[2,]+1, 38)), Y=as.double(substr(d_c,p_m[1,]+1, 17)))

x <- data[,1]
y <- data[,2]

fit.linear <- lm(y ~ poly(x, 23, raw=TRUE))
#fit.loess <- loess(y ~ x, data=data, span=0.8)

x_new = data.frame(x=seq(min(x),max(x),len=200))

plot(data)
lines(x_new$x ,predict(fit.linear, x_new), col="blue", lwd=2)
#lines(x_new$x, predict(fit.loess, x_new), col="green", lwd=2)

y.linear <- predict(fit.linear, data.frame(x))
#y.loess <- predict(fit.loess, data.frame(x))

lin_rmes <- sqrt( mean( (y-y.linear)^2 , na.rm = TRUE ) )
#loe_rmes <- sqrt( mean( (y-y.loess)^2 , na.rm = TRUE ) )
write.csv(data.frame(y=y.linear), file='y_predicted.csv', row.names=FALSE)



