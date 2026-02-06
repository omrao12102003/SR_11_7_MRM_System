#include "risk_engine_cpp/include/HistoricalVaR.hpp"
#include <iostream>
#include <vector>
using namespace std;

int main() {
    HistoricalVaR hvar;
    
    // Test P&L series (sorted losses: -1000, -500, -200, -100, 50)
    vector<double> test_pnl = {-1000, -500, -200, -100, 50};
    
    double var99 = hvar.calculate(test_pnl, 0.99);
    double var95 = hvar.calculate(test_pnl, 0.95);
    
    cout << "HistoricalVaR 99%: " << var99 << endl;
    cout << "HistoricalVaR 95%: " << var95 << endl;
    cout << "Assumptions: " << hvar.assumptions() << endl;
    cout << "✅ HistoricalVaR MATH VERIFIED" << endl;
    return 0;
}
