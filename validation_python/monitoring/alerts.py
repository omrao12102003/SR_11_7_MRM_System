def generate_alerts(row):
    """SR 11-7 Multi-window Alert Logic"""
    alerts = []
    
    # Historical VaR escalating thresholds
    if row['hist_breaches_30d'] >= 3: alerts.append('30d-YELLOW')
    if row['hist_breaches_60d'] >= 5: alerts.append('60d-ORANGE') 
    if row['hist_breaches_90d'] >= 8: alerts.append('90d-RED')
    
    # Stability deterioration
    if row['stability_score'] < -1.0: alerts.append('DRIFT-FAST')
    
    alert_level = ', '.join(alerts) if alerts else 'GREEN'
    health = 'HEALTHY' if 'GREEN' in alert_level else 'ACTION'
    
    return f"{alert_level} ({health})"

print("✓ Alert system online")
