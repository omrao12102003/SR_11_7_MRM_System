#pragma once
#include "VaRModel.hpp"
#include <vector>

// SR 11-7 Model 1: Non-parametric Historical VaR
// VaR_alpha = -Q_(1-alpha)(L) where Q = empirical quantile

class HistoricalVaR : public VaRModel {
public:
    double calculate(const std::vector<double>& pnl_series, 
                    double confidence_level) const override;
    
    std::string name() const override { return "HistoricalVaR"; }
    std::string assumptions() const override {
        return "IID returns; stationary distribution; 1-day horizon";
    }
};
