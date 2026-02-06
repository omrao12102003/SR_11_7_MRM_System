#!/usr/bin/env python3
"""
SR 11-7 PHASE 4: Ongoing Model Monitoring
Pillar 3 - Continuous Performance Oversight
"""

import pandas as pd
from datetime import datetime
from data_loader import load_validation_data
from rolling_metrics import compute_rolling_breaches
from drift_detection import compute_drift_metrics

def generate_alerts(row):
    """Multi-window SR 11-7 alerting"""
    alerts = []
    
    # Breach thresholds (99% VaR)
    if row['hist_breaches_30d'] >= 3: alerts.append('30d-EARLY')
    if row['hist_breaches_60d'] >= 5: alerts.append('60d-ESCALATE')
    if row['hist_breaches_90d'] >= 8: alerts.append('90d-CRITICAL')
    
    # Drift alert
    if pd.notna(row['stability_score']) and row['stability_score'] < -0.5:
        alerts.append('DRIFT-DETECTED')
    
    return '; '.join(alerts) if alerts else 'ALL-CLEAR'

def run_full_monitoring():
    print("🚀 SR 11-7 PHASE 4: DAILY MONITORING RUN")
    print("="*60)
    
    # Step 1: Load Phase 3 data
    df = load_validation_data()
    
    # Step 2: Rolling metrics
    rolling = compute_rolling_breaches(df)
    
    # Step 3: Drift detection  
    monitoring = compute_drift_metrics(rolling)
    
    # Step 4: Latest status (today)
    latest = monitoring.iloc[-1]
    
    print("\n📊 LATEST MONITORING STATUS:")
    print(f"Date: {latest['date']}")
    print(f"Hist 30d breaches: {latest['hist_breaches_30d']:.1f}")
    print(f"MC 30d breaches: {latest['mc_breaches_30d']:.1f}")
    print(f"PnL 30d vol: {latest['pnl_vol_30d']:.0f}")
    print(f"Stability score: {latest['stability_score']:.2f}")
    
    # Step 5: Alerts
    alert = generate_alerts(latest)
    health = 'HEALTHY' if 'ALL-CLEAR' in alert else '⚠️  ACTION REQUIRED'
    print(f"\n🚨 CURRENT ALERT: {alert}")
    print(f"Model Health: {health}")
    
    # Step 6: Save outputs
    monitoring[['date', 'hist_breaches_30d', 'mc_breaches_30d', 
                'pnl_vol_30d', 'stability_score', 'hist_rate_trend_30d']].to_csv(
        'outputs/rolling_monitoring.csv', index=False
    )
    
    # Model health report
    with open('outputs/model_health.txt', 'w') as f:
        f.write(f"SR 11-7 Monitoring Report: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Status: {health}\n")
        f.write(f"Alert: {alert}\n")
        f.write(f"Hist 30d: {latest['hist_breaches_30d']:.1f} breaches\n")
        f.write(f"MC 30d: {latest['mc_breaches_30d']:.1f} breaches\n")
        f.write("Action: " + ("None" if 'ALL-CLEAR' in alert else "Escalate to Risk Committee") + "\n")
    
    print("\n✅ Outputs saved:")
    print("  outputs/rolling_monitoring.csv")
    print("  outputs/model_health.txt")
    print("="*60)
    
    return monitoring

if __name__ == "__main__":
    monitoring_data = run_full_monitoring()
