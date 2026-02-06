import pandas as pd
import numpy as np

def compute_drift_metrics(df, windows=[30, 60, 90]):
    """Model stability indicators"""
    drift = df.copy()
    
    for w in windows:
        drift[f'pnl_mean_{w}d'] = df['pnl'].rolling(w).mean()
        drift[f'pnl_vol_{w}d'] = df['pnl'].rolling(w).std()
        drift[f'hist_rate_trend_{w}d'] = (
            df['breach_hist'].rolling(w).mean().diff()
        )
    
    # Stability score (simple composite)
    drift['stability_score'] = (
        (drift['hist_rate_trend_30d'].fillna(0)**2 * -1 + 
         drift['pnl_vol_30d'].fillna(0) / drift['pnl_vol_30d'].std())
        .round(2)
    )
    
    print("✓ Drift metrics computed")
    print("Latest stability:", drift['stability_score'].tail(1).values[0])
    return drift

if __name__ == "__main__":
    from data_loader import load_validation_data
    df = load_validation_data()
    drift = compute_drift_metrics(df)
