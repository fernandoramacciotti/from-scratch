# from-scratch

Implementations of algorithms from scratch, with little as aid from packages as possible. The goal is to understand how the algorithms/models work under the hood.

# Algorithms

* **Statistics and Machine Learning**
    * [Logistic Regression](./logistic_regression/logistic_regression.py): Logistic Regression with gradient descent
    * [Boosting](./bosting/vanilla_boosting.py): A vanilla implementation of gradient boosting

* **MCMC Samplers**
    * [Metropolis-Hastings](./metropolis_hastings/mh.R): Metropolis-Hastings algorithm with symmetrical proposal distribution
    * **Random-Walk Metropolis-Hastings**[[R](./metropolis_hastings/rwmh.R) | [Julia](./metropolis_hastings/rwmh.jl)]: Standard Random-Walk Metropolis Hastings, generalized to be multidimensional.