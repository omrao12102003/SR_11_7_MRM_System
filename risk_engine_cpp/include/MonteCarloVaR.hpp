#pragma once
#include "VaRModel.hpp"
#include <random>

class MonteCarloVaR : public VaRModel {
public:
    MonteCarloVaR(unsigned int num_paths = 10000);
    
    double calculate(const std::vector<double>& pnl_series, 
                    double confidence_level) const override;
    
    std::string name() const override { return "MonteCarloVaR"; }
    std::string assumptions() const override {
        return "Parametric normal; convergence diagnostics needed";
    }

private:
    mutable std::mt19937 generator_;
    unsigned int num_paths_;
};
