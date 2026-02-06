#pragma once
#include <vector>
#include <string>

// SR 11-7 Pillar 1: Model Comparability + Documentation

class VaRModel {
public:
    virtual double calculate(const std::vector<double>& pnl_series, 
                            double confidence_level) const = 0;
    virtual std::string name() const = 0;
    virtual std::string assumptions() const = 0;
    virtual ~VaRModel() = default;
};
