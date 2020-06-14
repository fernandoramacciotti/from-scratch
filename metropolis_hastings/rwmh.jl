
using Distributions, Random

function rwmh(p; n = 1000, x0 = 0, σ = 1, burnin = 200)
    # p is the target likelihood
    # n is the number of iterations
    # x0 is the initial guess (can be multidimensional)
    # sd is the sd for random step
    # burnin initial samples to discard
    
    # get dimension
    dim = length(x0)
    # chain matrix
    chain = Array{Float64}(undef, n, dim)
    chain[1, :] .= x0
    # acceptance vector
    accepted = zeros(n)
    # comparison vector (sampled from U(0, 1))
    u = rand(n)
    # random step (sampled from N(0, σ))
    eps = rand(Normal(0, σ), n, dim)

    # loop
    for iter = 2:n
        # Step 1
        # candidate from random step
        candidate = chain[iter - 1, :] + eps[iter, :]

        # Step 2
        # Probability of acceptance alpha
        log_α = log.(p(candidate)) - log.(p(chain[iter - 1, :]))
        rho = min.(1, exp.(log_α))[1]

        # Step 3
        # Accept/Reject
        if u[iter] <= rho # accept
            chain[iter, :] = candidate
            accepted[iter] = 1
        else # reject
            chain[iter, :] = chain[iter - 1, :]
        end
    end
    # done, return chain and acceptance vector, removing burnin phase
    return Dict("chain" => chain[(burnin + 1):n, :], 
                "accepted" => accepted[(burnin + 1):n, :])
end

# example ---------------------------------------------------------------------
using Gadfly
Random.seed!(20)

# univariate
# target will be Beta(2, 4)
p(x) = pdf.(Beta(2, 4), x)
n = 5000
σ = 3
burnin = 500
# mh
res = rwmh(p, n = n, σ = σ, burnin = burnin)
# assess
mean(res["accepted"]) # 0.08
mean(res["chain"])    # 0.33 (true value = 1/3)
std(res["chain"])     # 0.17 (true value = .178)

# plot
plot(layer(p, 0, 1, color = [colorant"red"]),
     layer(x = res["chain"], Geom.histogram(bincount = 30, density = true)))


# multivariate
# target will be Normal([2, 4], [2 0.5; 0.5 1])
μ = [2., 4.]
Σ = [2. 0.5; 0.5 1.]
p(x) = pdf(MultivariateNormal(μ, Σ), x)
n = 5000
σ = 3
x0 = [0, 0]
burnin = 500
# mh
res = rwmh(p, n = n, x0 = x0, σ = σ, burnin = burnin)
# assess
mean(res["accepted"])     # 0.19
mean(res["chain"][:, 1])  # 2.07 (true value = 2)
mean(res["chain"][:, 2])  # 4.08 (true value = 4)
var(res["chain"][:, 1])   # 2.09 (true value = 2)
var(res["chain"][:, 2])   # 1.04 (true value = 1)
cor(res["chain"][:, 1], res["chain"][:, 2]) # 0.36 (true value = 0.5)
