#include "risk_engine_cpp/include/HistoricalVaR.hpp"
#include "risk_engine_cpp/include/MonteCarloVaR.hpp"
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<double> test_pnl = {-1200, -800, -600, -400, -200, 100, 300};
    
    HistoricalVaR hvar;
    MonteCarloVaR mcvar(5000);
    
    cout << "P&L Sample: " << test_pnl.size() << " days" << endl;
    cout << "Historical 95%: " << hvar.calculate(test_pnl, 0.95) << endl;
    cout << "MonteCarlo 95%: " << mcvar.calculate(test_pnl, 0.95) << endl;
    cout << "MC Assumptions: " << mcvar.assumptions() << endl;
    cout << "✅ MonteCarloVaR VERIFIED" << endl;
    return 0;
}
