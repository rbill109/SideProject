#----1 - (a)----
true_f = function(x){
  return(sin(2*pi*x))
}
set.seed(2021)
nsamp = 1000
x = (1:nsamp-0.5)/nsamp
error = rnorm(nsamp,0,0.1)
z = true_f(x) + error
plot(x,z,xlab="X",ylab="Z",main="histogram of x and z")

#----1 - (f)----
library(randomcoloR)
ReLU <- function(x){
  return(pmax(0,x))
}

# fitting
p = 500
l_range = c(0,0.01,0.1,1,10,50,100,1000)
l = length(l_range)
X = t(sapply(x,function(i) ReLU(i-(1:p-0.5)/p)))
X_prime = cbind(rep(1,nsamp),X)
yhat = matrix(NA,nsamp,l)
for(i in 1:l){
  theta = solve(diag(l_range[i],p+1)+t(X_prime) %*% X_prime) %*% t(X_prime) %*% z
  yhat[,i] = X_prime %*% theta
}

# plot
col = randomColor(length(l_range), luminosity="bright")
plot(x, true_f(x), type="l", lwd=14, col="gray", main="true function vs y_pred")
for(i in 1:length(l_range)){
  if(i==1){
    lines(x, yhat[,i], lwd=1, col=1)
  }
  else{
    lines(x, yhat[,i], lwd=2, col=col[i])
  }
}
legend("topright",c("true_f",paste("¥ë=",l_range)),col=c("gray",1,col[2:l]),cex=0.8,lwd=c(10,rep(3,l)))