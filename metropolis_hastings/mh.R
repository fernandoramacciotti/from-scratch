metropolis_hastings_symmetric <- function(p, q, n) {
    # symmetric proposal distribution
    # p target density
    # q proposed density
    # N number of iterations

    # chain vector
    chain <- rep(NA, n)
    # accpetance vector
    accepted <- rep(1, n)
    # initial guess
    chain[1] <- q(1) # 1 sample from Q (could be anything though)
    # loop
    for (i in 2:n) {
        # Step 1
        # candidate, sampled from Q
        x.prop <- q(1)
        
        # Step 2
        # acceptance ratio alpha (log for numerical stability)
        log.alpha <- log(p(x.prop)) - log(p(chain[i-1]))
        rho <- min(1, exp(log.alpha)) # cap at 1

        # Step 3
        # accept or reject
        u <- runif(1)
        if (u <= rho) {
            chain[i] <- x.prop # accept
        } else {
            chain[i] <- chain[i-1] # reject
            accepted[i] <- 0
        }
    }
    return(list(chain=chain, accepted=accepted))
}

# example ---------------------------------------------------

library(ggplot2)

# target density f is Beta(2.7, 6.3)
# proposed q is U[0,1]

set.seed(20)
n <- 5e3
alpha <- 2.7
beta <- 6.3
p <- function(x) dbeta(x, shape1 = alpha, shape2 = beta)
q <- function(k) runif(k) # proposed distribution 
results <- metropolis_hastings(p, q, n)

acc_ratio <- mean(results$accepted) # acceptance ratio
dens <- p(results$chain) # calculating the target distribution for the generated chain

df <- data.frame(x = results$chain, dens = dens)

# plotting

ggplot(data = df, aes(x = x)) + 
  geom_histogram(aes(y = ..density..)) +
  geom_line(aes(y = dens), colour = 'red')
