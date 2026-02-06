#include "risk_engine_cpp/include/Position.hpp"
#include <iostream>
using namespace std;

int main() {
    Position aapl{"AAPL", 100, 150.25};
    Position msft{"MSFT", 50, 320.50};
    
    cout << "AAPL value: " << aapl.market_value() << endl;
    cout << "AAPL weight (10k portfolio): " << aapl.weight(10000) << endl;
    cout << "✅ Position.hpp PASSED" << endl;
    return 0;
}
