// src/Portfolio.cpp
// SR 11-7 Pillar 1: Correct Implementation
#include "Portfolio.hpp"
#include <fstream>
#include <sstream>
#include <iostream>

void Portfolio::load_positions(const std::string& csv_file) {
    std::ifstream file(csv_file);
    std::string line;
    
    // Skip header
    std::getline(file, line);
    
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string id;
        double qty, price;
        
        std::getline(iss, id, ',');
        iss >> qty;
        iss.ignore();
        iss >> price;
        
        positions_.emplace_back(Position{id, qty, price});
    }
}

void Portfolio::load_returns(const std::string& csv_file) {
    std::ifstream file(csv_file);
    std::string line;
    
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<double> day_returns;
        std::string token;
        
        while (std::getline(iss, token, ',')) {
            day_returns.push_back(std::stod(token));
        }
        returns_.push_back(day_returns);
    }
}

std::vector<double> Portfolio::compute_pnl_series() const {
    std::vector<double> pnl_series;
    
    for (const auto& day_returns : returns_) {
        double daily_pnl = 0.0;
        
        for (size_t i = 0; i < positions_.size() && i < day_returns.size(); ++i) {
            daily_pnl += positions_[i].quantity * 
                        positions_[i].price * 
                        day_returns[i];
        }
        pnl_series.push_back(daily_pnl);
    }
    return pnl_series;
}

double Portfolio::total_value() const {
    double total = 0.0;
    for (const auto& pos : positions_) {
        total += pos.market_value();
    }
    return total;
}
