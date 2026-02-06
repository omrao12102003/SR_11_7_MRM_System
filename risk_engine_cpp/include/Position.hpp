#pragma once
#include <string>

struct Position {
    std::string instrument_id;
    double quantity;
    double price;
    
    double market_value() const { return quantity * price; }
    double weight(double total_value) const {
        return total_value > 0 ? market_value() / total_value : 0.0;
    }
};
