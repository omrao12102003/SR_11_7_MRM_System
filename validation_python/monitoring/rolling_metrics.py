import pandas as pd

def compute_rolling_breaches(df, windows=[30, 60, 90]):
    """Rolling breach counts (SR 11-7 ongoing monitoring)"""
    metrics = df.copy()
    
    for model in ['hist', 'mc']:
        breach_col = f'breach_{model}'
        for w in windows:
            metrics[f'{model}_breaches_{w}d'] = (
                metrics[breach_col].rolling(w, min_periods=1).sum()
            )
    
    # Breach rates
    for w in windows:
        metrics[f'hist_rate_{w}d'] = metrics[f'hist_breaches_{w}d'] / w * 100
        metrics[f'mc_rate_{w}d'] = metrics[f'mc_breaches_{w}d'] / w * 100
    
    print("✓ Rolling metrics computed")
    return metrics

if __name__ == "__main__":
    from data_loader import load_validation_data
    df = load_validation_data()
    rolling = compute_rolling_breaches(df)
    print(rolling[['date', 'hist_breaches_30d', 'mc_breaches_30d']].tail())
