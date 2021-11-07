library(mvtnorm)
library(tictoc)

#----function----
# Generate samples
logit <- function(X){
  return(1/(1+exp(-X)))
}


make_toy_sample <- function(n, p, seed=1234){
  set.seed(1234)
  samp = matrix(NA,n,p+1)
  # Draw x from p-dimensional standard normal dist
  mu <- rep(0,p)
  sigma <- diag(p)
  x_samp <- rmvnorm(n, mu, sigma)
  
  # Draw y from logistic regression model given x
  theta = matrix(rep(1, p), 1)
  prob = logit(x_samp%*%t(theta))
  samp[,p+1] <- sapply(prob, function(x) rbinom(1, 1, x))
  samp[,1:p] <- x_samp
  return(samp)
}


# Gradient Descent
GradDescent <- function(X, Y, alpha=1e-2, epsilon=1e-2, verbose=TRUE){
  tic("Running time")
  print("Start!")
  i = 0
  n = nrow(X)
  p = ncol(X)
  theta <- matrix(rep(0, p), 1, dimnames = list(1,  paste("beta", seq(1,p),sep=" ")))
  distance = 1
  while(distance > epsilon){
    h = logit(X%*%t(theta))
    gradient = (t(X)%*%(h-Y))
    cost = -(1/n)*sum(Y*log(h)+(1-Y)*log(1-h))
    theta_next = theta - alpha * t(gradient)
    if(verbose==TRUE){
      if(i %% 500 == 0){
        print(matrix(c(i, cost), 1 ,dimnames=list(1,c("Epoch", "Cost"))))
        print(round(theta_next,3))
      }
    }
    distance = sqrt(sum((theta-theta_next)**2))
    theta = theta_next
    i = i + 1
  }
  print("End...")
  time = toc()
  print(paste0(i," iterations"))
  print("---------------------------------")
  result = list(theta = theta, iter = i, time = time$toc-time$tic)
  return(result)
}


# Newton's method
NewtonMethod <- function(X, Y, epsilon=1e-2, verbose=TRUE){
  tic("Running time")
  print("Start!")
  i = 0
  n = nrow(X)
  p = ncol(X)
  theta <- matrix(rep(0, p), 1, dimnames = list(1,  paste("beta", seq(1,p),sep=" ")))
  distance = 1
  while(distance > epsilon){
    h = logit(X%*%t(theta))
    Hessian = t(X) %*% sweep(X, 1, h * (1 - h), "*")
    gradient = (t(X)%*%(h-Y))
    cost = -(1/n)*sum(Y*log(h)+(1-Y)*log(1-h))
    theta_next = theta - t(solve(Hessian) %*% gradient)
    if(verbose==TRUE){
      if(i %% 500 == 0){
        print(matrix(c(i, cost), 1 ,dimnames=list(1,c("Epoch", "Cost"))))
        print(round(theta_next,3))
      }
    }
    distance = sqrt(sum((theta-theta_next)**2))
    theta = theta_next
    i = i + 1
  }
  print("End...")
  time = toc()
  print(paste0(i," iterations"))
  print("---------------------------------")
  result = list(theta = theta, iter = i, time = time$toc-time$tic)
  return(result)
}


# Execute the algorithm
main <- function(method, n, p, verbose=TRUE){
  print("making toy sample...")
  samp <- make_toy_sample(n, p)
  x_samp <- samp[,1:p]
  y_samp <- samp[,p+1]
  print(paste0(n," samples and ",p,"-dimensional"))
  if(method=="gd") {
    result <- GradDescent(x_samp, y_samp, alpha=1e-2, epsilon=1e-2, verbose=verbose)
  }
  else if(method=="nwt"){
    result <- NewtonMethod(x_samp, y_samp, epsilon=1e-2, verbose=verbose)
  }
  return(result)
}


# Plot the result
PlotResult <- function(method, n_range, p_range, ylabel, result){
  title = list(gd = "Gradient Descent Method", 
               nwt = "Newton's Method")
  # ylabel = list(result_iter = "number of iteraions", result_time = "total running time")
  len_n = length(n_range)
  len_p = length(p_range)
  matplot(result, type="l", lty=c(1:len_p), col=c(1:len_p), xaxt="n", 
          xlab = "number of samples",
          main = paste0(title[[method]],"\n",ylabel))
  legend("topleft", legend=p_range, lty=c(1:len_p), col=c(1:len_p))
  axis(1, at = 1:len_n, labels=n_range)
}

Evaluate <- function(method, n_range, p_range, verbose=TRUE){
  # execute
  len_n = length(n_range)
  len_p = length(p_range)
  result_iter = result_time = matrix(NA, len_n, len_p)
  for(j in 1:len_p){
    p = p_range[j]
    for(i in 1:len_n){
      n = n_range[i]
      if((n < 10*p)&(method=="nwt")){
        result_iter[i, j] <- 0
        result_time[i, j] <- 0
      }
      else{
        result = main(method, n, p, verbose=verbose)
        result_iter[i, j] <- result$iter
        result_time[i, j] <- result$time
      }
    }
  }
  # plot
  par(mfrow=c(1,2), mar=c(4, 3, 3, 1), oma=c(0.5, 0.5, 2, 0.5))
  PlotResult(method, n_range, p_range, "number of iterations", result_iter)
  PlotResult(method, n_range, p_range, "total running time", result_time)
  
  return(result_iter)
}



#----main----
# result_gd <- main("gd", 1000, 3)
# result_nwt <- main("nwt", 1000, 3)

n_range = seq(100, 1500, by=50)
p_range = c(10, 20, 50, 70)
result_gd_all <- Evaluate("gd", n_range, p_range, verbose=FALSE)
result_nwt_all <- Evaluate("nwt", n_range, p_range, verbose=FALSE)


n_range = seq(100, 5000, by=100)
p_range = c(10, 20, 50, 70)
result_nwt_all <- Evaluate("nwt", n_range, p_range, verbose=FALSE)