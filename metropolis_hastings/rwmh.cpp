#include <iostream>
#include <random>
#include <algorithm>
#include <vector>

// pure C++ Random-Walk Metropolis-Hastings

// Uniform(0, 1)
double runif()
{
    return (float)std::rand() / RAND_MAX;
}

// target log-likelihood
double log_likelihood(double x)
{
    // (un-nomralized) univariate Normal(mu, sd) - just to illustrate
    double mu = 2;
    double sd = 3;
    return -1 * std::pow(x - mu, 2) / (2 * std::pow(sd, 2));
}

// Random-Walk Metropolis-Hastings
std::vector<double> rwmh(int n, double x0, double v, int burnin)
{
    // n number of iterations
    // x0 initial guess
    // v sd of random-step
    // burnin initial samples to discard

    // random device class instance, source of 'true' randomness for initializing random seed
    std::random_device rd;

    // Mersenne twister PRNG, initialized with seed from previous random device instance
    std::mt19937 gen(rd());

    // init vars
    double candidate;
    double u;
    double log_alpha;
    double alpha;
    std::normal_distribution<double> random_step(0.0, v);

    // initialize results
    std::vector<double> chain(n);
    std::vector<int> accepted(n, 0);
    std::vector<double> final_chain(n - burnin);    // to remove burnin
    std::vector<int> final_accepted(n - burnin, 0); // to remove burnin

    // initial guess
    chain[0] = x0;
    accepted[0] = 1;
    if (burnin == 0)
    {
        final_chain[0] = x0;
        final_accepted[0] = 1;
    }

    // loop
    for (int i = 1; i < n; i++)
    {
        // Step 1
        // candidate with random-step
        candidate = chain[i - 1] + random_step(gen);

        // Step 2
        // probability of acceptance alpha
        log_alpha = log_likelihood(candidate) - log_likelihood(chain[i - 1]);
        alpha = std::exp(log_alpha);

        // Step 3
        // Accept/Reject
        u = runif();
        if (u <= alpha)
        {
            // accept
            chain[i] = candidate;
            accepted[i] = 1;
            // removing burnin
            if (i >= burnin)
            {
                final_chain[i - burnin] = candidate;
                final_accepted[i - burnin] = 1;
            }
        }
        else
        {
            //reject
            chain[i] = chain[i - 1];
            if (i >= burnin)
            {
                final_chain[i - burnin] = chain[i - 1];
            }
        }
    }
    // print acceptance ratio
    double acc_ratio = accumulate(final_accepted.begin(), final_accepted.end(), 0.0) / final_accepted.size();
    std::cout << "Acceptance ratio = " << acc_ratio << "\n";

    return final_chain;
}

int main()
{
    // define target likelihood

    // number of iterations
    int n = 5000;
    int burnin = 500;
    double x0 = 0.0;
    double v = 4.0;

    // rwmh
    std::vector<double> chain = rwmh(n, x0, v, burnin);

    // print results
    double sum = std::accumulate(chain.begin(), chain.end(), 0.0);
    double mean = sum / chain.size();

    double sq_sum = std::inner_product(chain.begin(), chain.end(), chain.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / chain.size() - mean * mean);

    std::cout << "Mean = " << mean << "\n";
    std::cout << "Stdev = " << stdev << "\n";

    return 0;
}
