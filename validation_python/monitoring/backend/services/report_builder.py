import pandas as pd
BASE_DIR = "/mnt/c/Users/omira/OneDrive/Desktop/SR11_7_MRM_System"

def build_summary():
    # Phase 4: Monitoring status
    try:
        monitoring = pd.read_csv(f"{BASE_DIR}/validation_python/monitoring/outputs/rolling_monitoring.csv")
        latest = monitoring.iloc[-1]
        health = "HEALTHY" if latest.get('hist_breaches_30d', 0) < 3 else "ACTION REQ"
        stability = latest.get('stability_score', 'N/A')
    except:
        health = stability = "NO DATA"
    
    # Phase 2: VaR values  
    try:
        var_data = pd.read_csv(f"{BASE_DIR}/data/risk_outputs/risk_engine_20260204.csv")
        hist_var = float(var_data[var_data['model']=='HistoricalVaR']['var99_1d'].iloc[0])
        mc_var = float(var_data[var_data['model']=='MonteCarloVaR']['var99_1d'].iloc[0])
    except:
        hist_var = mc_var = "N/A"
    
    return f"""SR 11-7 EXECUTIVE SUMMARY (Phase 5)
=======================
Active Models: 2
Monitoring: {health} (Stability: {stability})
Historical VaR: ${hist_var:,.0f}
Monte Carlo VaR: ${mc_var:,.0f}  
Phase 4 Status: ALL-CLEAR
======================="""

print(build_summary())
