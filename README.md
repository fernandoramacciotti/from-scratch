# from-scratch

Implementations of algorithms from scratch, with little as aid from packages as possible. The goal is to understand how the algorithms/models work under the hood.

# Algorithms

* **Operations Research**
    * [Kruskal](./operations_research/kruskal.py): Kruskal algorithm to find minimum spanning tree in a graph
    * [Dijkstra](./operations_research/dijkstra.py): Dijkstra algorithm to find minimum path in a graph
    * [Floyd-Warshall](./operations_research/floyd_warshall.py): Floyd-Warshall algorithm to find minimum path in a graph
    * [Ford-Fulkerson](./operations_research/ford_fulkerson.py): Ford-Fulkerson algorithm to find maximum network flow
    * [Critical Path Method](./operations_research/critical_path_method.py): Critical Path Method (CPM) algorithm to find a critical schedule for a project

* **Statistics and Machine Learning**
    * [Logistic Regression](./logistic_regression/logistic_regression.py): Logistic Regression with gradient descent
    * [Boosting](./bosting/vanilla_boosting.py): A vanilla implementation of gradient boosting

* **MCMC Samplers**
    * [Metropolis-Hastings](./metropolis_hastings/mh.R): Metropolis-Hastings algorithm with symmetrical proposal distribution
    * **Random-Walk Metropolis-Hastings** [[R](./metropolis_hastings/rwmh.R) | [Julia](./metropolis_hastings/rwmh.jl) | [C++](./metropolis_hastings/rwmh.cpp)]: Standard Random-Walk Metropolis Hastings, generalized to be multidimensional.