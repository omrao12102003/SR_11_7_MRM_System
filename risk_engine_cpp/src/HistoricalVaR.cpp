#include "HistoricalVaR.hpp"
#include <algorithm>
#include <stdexcept>

double HistoricalVaR::calculate(const std::vector<double>& pnl_series, 
                               double confidence_level) const {
    if (pnl_series.empty()) {
        throw std::runtime_error("Empty P&L series");
    }
    
    // SR 11-7: Full revaluation historical method
    std::vector<double> losses = pnl_series;
    std::sort(losses.begin(), losses.end());  // ascending
    
    // Empirical quantile: Q_(1-alpha)
    double alpha = 1.0 - confidence_level;
    size_t index = static_cast<size_t>(alpha * losses.size());
    
    if (index >= losses.size()) {
        index = losses.size() - 1;
    }
    
    return -losses[index];  // VaR = -loss (positive risk number)
}
