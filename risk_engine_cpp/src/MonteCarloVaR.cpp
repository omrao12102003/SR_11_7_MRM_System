#include "MonteCarloVaR.hpp"
#include <algorithm>
#include <numeric>
#include <random>
#include <cmath>
#include <stdexcept>

MonteCarloVaR::MonteCarloVaR(unsigned int num_paths) 
    : num_paths_(num_paths) {
    generator_.seed(42);
}

double MonteCarloVaR::calculate(const std::vector<double>& pnl_series, 
                               double confidence_level) const {
    if (pnl_series.empty()) {
        throw std::runtime_error("Empty P&L series");
    }
    
    double mean = std::accumulate(pnl_series.begin(), pnl_series.end(), 0.0) 
                / pnl_series.size();
    double variance = 0.0;
    for (double pnl : pnl_series) {
        variance += (pnl - mean) * (pnl - mean);
    }
    variance /= (pnl_series.size() - 1);
    double stddev = std::sqrt(variance);
    
    std::vector<double> simulations;
    simulations.reserve(num_paths_);
    std::normal_distribution<double> dist(mean, stddev);
    
    for (unsigned int i = 0; i < num_paths_; ++i) {
        simulations.push_back(dist(generator_));
    }
    
    std::sort(simulations.begin(), simulations.end());
    double alpha = 1.0 - confidence_level;
    size_t index = static_cast<size_t>(alpha * simulations.size());
    
    return -simulations[index];
}
