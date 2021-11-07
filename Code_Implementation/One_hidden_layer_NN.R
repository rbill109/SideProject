library(mvtnorm)
library(tictoc)

#----1 - (b)----
# Generate samples
sigmoid <- function(X){
  return(1/(1+exp(-X)))
}

NN_model <- function(x1, x2){
  y = sigmoid(sigmoid(-2*sigmoid(x1+x2+0.5)-1.5)-sigmoid(sigmoid(x1+x2+0.5)+2.5)-1)
  return(y)
}

make_toy_sample <- function(n, seed=1234){
  set.seed(seed)
  samp = matrix(NA,n,2)
  # Draw x from 2-dimensional standard normal dist
  mu <- rep(0,2)
  sigma <- diag(2)
  x_samp <- rmvnorm(n, mu, sigma)
  
  # Draw y from defined NN model
  y_samp <- NN_model(x_samp[,1], x_samp[,2])
  
  # Draw z from normal dist
  z_samp <- rnorm(n, y_samp, 0.001)
  samp[,1] <- y_samp
  samp[,2] <- z_samp
  return(samp)
}

samp <- make_toy_sample(1e4)
hist(samp[,1], nclass=100)
hist(samp[,2], nclass=100)
plot(samp[,1],samp[,2],xlab="Y",ylab="Z",main="histogram of y and z")

#----1 - (d)----
## function
sigmoid <- function(X){
  return(1/(1+exp(-X)))
}

sigmoid_derivative <- function(p){
  return(p*(1-p))
}

cal_cost <- function(NN) {
  return(0.5*(sum((NN$y-NN$z)**2)))
} 

make_params <- function(NN){
  params = list(w11 = NN$w1[1],
                w12 = NN$w1[2],
                b1 = NN$b1,
                w21 = NN$w2[1],
                w22 = NN$w2[2],
                b21 = NN$b2[1],
                b22 = NN$b2[2],
                w31 = NN$w3[1],
                w32 = NN$w3[2],
                b3 = NN$b3)
  return(params)
}
forward <- function(NN){
  # w, b = weights and biases
  w1 = NN$w1
  b1 = NN$b1
  w21 = NN$w2[1]
  w22 = NN$w2[2]
  b21 = NN$b2[,1]
  b22 = NN$b2[,2]
  w3 = NN$w3
  b3 = NN$b3
  
  # feedfoward
  NN$z1 = sigmoid(NN$X%*%NN$w1-rep(NN$b1,n)) # n x 1
  NN$z21 = sigmoid(NN$z1%*%NN$w2[1]-matrix(NN$b2[1],n)) # n x 1
  NN$z22 = sigmoid(NN$z1%*%NN$w2[2]-matrix(NN$b2[2],n)) # n x 1
  NN$y = sigmoid(cbind(NN$z21,NN$z22)%*%NN$w3-matrix(NN$b3,n)) # n x 1
  return(NN)
}


backprop <- function(NN, lr=0.001){
  # d = deltas
  d3 = (NN$y-NN$z)*sigmoid_derivative(NN$y) # n x 1
  NN$w3[1] = NN$w3[1] - lr * t(d3) %*% NN$z21 
  NN$w3[2] = NN$w3[2] - lr * t(d3) %*% NN$z22
  NN$b3 = NN$b3 - lr * t(d3) %*% matrix(-1,n)
  
  d21 = d3 * sigmoid_derivative(NN$z21) * NN$w3[1] # n x 1
  d22 = d3 *sigmoid_derivative(NN$z22) * NN$w3[2] # n x 1
  NN$w2[1] = NN$w2[1] - lr * t(d21) %*% NN$z1
  NN$w2[2] = NN$w2[2] - lr * t(d22) %*% NN$z1
  NN$b2[1] = NN$b2[1] - lr * t(d21) %*% matrix(-1,n)
  NN$b2[2] = NN$b2[2] - lr * t(d22) %*% matrix(-1,n)
  
  d1 = sigmoid_derivative(NN$z1) * NN$w2[1] * d21 +
    sigmoid_derivative(NN$z1) * NN$w2[2] * d22
  
  
  NN$w1[1] = NN$w1[1] - lr * t(d1) %*% NN$X[,1]
  NN$w1[2] = NN$w1[2] - lr * t(d1) %*% NN$X[,2]
  NN$b1 = NN$b1 - lr * t(d1) %*% matrix(-1,n)
  return(NN)
}

## main
# Input data
set.seed(1234)
n = 1e4
mu <- rep(0,2)
sigma <- diag(2)
X <- rmvnorm(n, mu, sigma)
y <- matrix(rep(0,n))
z <- rnorm(n, y, 0.0001)

NN = list(
  X = X,
  # # Initialize weights and biases
  # layer1
  w1 = matrix(rnorm(ncol(X))),
  b1 =  matrix(rnorm(1)),
  # layer2
  w2 =  matrix(rnorm(ncol(X))),
  b2 = matrix(rnorm(1*ncol(X)),ncol=ncol(X)),
  # layer3
  w3 = matrix(rnorm(ncol(X))),
  b3 = matrix(rnorm(1)),
  # target
  z = z,
  # output
  y = y
)

NN_t = list(
  X = X,
  # # Initialize weights and biases
  # layer1
  w1 = matrix(c(1,1)+rnorm(2, 0, 1e-2)),
  b1 =  matrix(-0.5)+rnorm(1, 0, 1e-2),
  # layer2
  w2 =  matrix(c(-2,1)+rnorm(2, 0, 1e-2)),
  b2 = matrix(c(1.5,-2.5)+rnorm(2, 0, 1e-2),ncol=ncol(X)),
  # layer3
  w3 = matrix(c(1,-1)+rnorm(2, 0, 1e-2)),
  b3 = matrix(1)+rnorm(1, 0, 1e-2),
  # target
  z = z,
  # output
  y = y
)

# train
epoch = 5e4
train <- function(epoch, NN, epsilon=1e-2, verbose = TRUE){
  result = list(
    loss = matrix(c(1:epoch),ncol=2,nrow=epoch),
    params = c(NN$w1, NN$w2, NN$w3, NN$b1, NN$b2, NN$b3)
  )
  for(i in c(1:epoch)){
    NN <- forward(NN)
    NN <- backprop(NN)
    result$loss[i,2] = cal_cost(NN)
    result$params = make_params(NN)
    if(verbose==TRUE){
      if(i %% 500 == 0){
        print(matrix(result$loss[i,],1,dimnames = list(1,c("Epoch", "Cost"))))
      }
    }
    if(result$loss[i,2] < epsilon){
      break
    }
  }
  print(i)
  return(result)
}
result <- train(epoch, NN_t)

# plot
df_loss = data.frame(epoch=result$loss[1:12938,1],loss=result$loss[1:12938,2])
plot(df_loss, type="l", main="Loss function")
print(result$params)
print(make_params(NN_t))