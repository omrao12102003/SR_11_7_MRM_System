#pragma once
#include "Position.hpp"
#include <vector>
#include <string>
#include <map>

class Portfolio {
public:
    void load_positions(const std::string& csv_file);
    void load_returns(const std::string& csv_file);
    
    // SR 11-7 Pillar 1: Deterministic core computation
    std::vector<double> compute_pnl_series() const;
    
    double total_value() const;
    size_t num_positions() const { return positions_.size(); }

private:
    std::vector<Position> positions_;
    std::vector<std::vector<double>> returns_;  // time x instruments
};
