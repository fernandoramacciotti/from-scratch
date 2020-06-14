rwmh <-  function(p, n = 1e3, x0 = 0, sd = 1) {
  # random walk metroplis-hastings
  # p target density
  # n number of iterations
  # x0 initial guess (can be multidimensional)
  # sd innovation variance (random walk variance)
  
  # dimesion
  dim <- length(x0)
  # chain vector
  chain <- matrix(NA, n, dim)
  # accpetance vector
  accepted <- rep(1, n)
  # initial guess
  chain[1, ] <- x0
  # vector to compare for accept/reject
  u <- runif(n)
  # noise for random walk
  eps <- matrix(rnorm(n * dim, mean = 0, sd = sd), n, dim)
  # loop
  for (i in 2:n) {
    # Step 1
    # candidate, random walk, innovation variance
    x.prop <- chain[i-1,] + eps[i,]
    
    # Step 2
    # acceptance ratio alpha (log for numerical stability)
    log.alpha <- log(p(x.prop)) - log(p(chain[i-1]))
    rho <- min(1, exp(log.alpha)) # cap at 1
    
    # Step 3
    # accept or reject
    if (u[i] <= rho) {
      chain[i,] <- x.prop # accept
    } else {
      chain[i,] <- chain[i-1,] # reject
      accepted[i] <- 0
    }
  }
  return(list(chain=chain, accepted=accepted))
}
