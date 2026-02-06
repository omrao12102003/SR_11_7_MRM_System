#include "risk_engine_cpp/include/HistoricalVaR.hpp"
#include "risk_engine_cpp/include/MonteCarloVaR.hpp"
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 40-day realistic P&L (mix losses/gains)
    vector<double> pnl_40days = {
        -1500,-800,-1200,-600,-900,200,100,-400,300,-200,
        -1100,150,-700,250,-500,50,-300,400,-100,0,
        -1300,-950,-850,-450,500,1000,-250,750,-350,200,
        -1400,50,-1050,300,-650,800,-550,150,-750,600
    };
    
    HistoricalVaR hvar;
    MonteCarloVaR mcvar(1000);  // Reduced for test
    
    cout << "Realistic 40-day P&L test" << endl;
    cout << "Historical 99%: " << hvar.calculate(pnl_40days, 0.99) << endl;
    cout << "MonteCarlo 99%: " << mcvar.calculate(pnl_40days, 0.99) << endl;
    cout << hvar.assumptions() << endl;
    cout << mcvar.assumptions() << endl;
    cout << "✅ BOTH VaR MODELS LIVE" << endl;
    return 0;
}
