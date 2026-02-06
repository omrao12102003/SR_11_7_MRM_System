import pandas as pd
import numpy as np
import data_loader  
import os

def detect_breaches(var_value, pnl_series):
    return (pnl_series < -var_value).astype(int)

def run_backtest(model_name):
    # Fix: Pass required csv_path arguments
    var_df = data_loader.load_var_csv("data/risk_outputs/risk_engine_20260204.csv")
    pnl = data_loader.load_realized_pnl("data/market_data/realized_pnl.csv")
    
    var_value = float(var_df[var_df['model'] == model_name]['var99_1d'].iloc[0])
    breaches = detect_breaches(var_value, pnl)
    
    result = f"{model_name}: {int(breaches.sum())}/{len(pnl)} ({breaches.mean():.1%}) | VaR={var_value:.0f}"
    
    # Save SR 11-7 deliverable
    out_df = pd.DataFrame({
        'date': pnl.index.strftime('%Y-%m-%d'),
        'pnl': pnl.round(2),
        'var_limit': -var_value,
        'breach': breaches
    })
    csv_file = f"outputs/{model_name.lower()}_backtest.csv"
    out_df.to_csv(csv_file, index=False)
    
    print(result)
    return breaches

if __name__ == "__main__":
    print("=== SR 11-7 VaR BACKTESTING ===")
    print("C++ VaR vs Realized PnL")
    print("-"*40)
    
    hist_breaches = run_backtest("HistoricalVaR")
    mc_breaches = run_backtest("MonteCarloVaR")
    
    print(f"\nCSVs saved: outputs/*_backtest.csv")
    print(f"Ready for Kupiec test: hist={hist_breaches.sum()}, mc={mc_breaches.sum()}")
