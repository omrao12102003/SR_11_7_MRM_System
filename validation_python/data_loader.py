import pandas as pd
from pathlib import Path

def load_var_csv(csv_path):
    """Load immutable C++ VaR outputs - read-only"""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"C++ output missing: {csv_path}")
    
    df = pd.read_csv(path)
    print(f"Loaded C++ VaR: {len(df)} models")
    print(df.head())
    return df

def load_realized_pnl(csv_path):
    """Load market realized P&L for backtesting"""
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    print(f"Realized P&L: {len(df)} days")
    print(df.head())
    return df

if __name__ == "__main__":
    # Test Phase 2 output
    var_df = load_var_csv("../data/risk_outputs/risk_engine_20260204.csv")
    print("Data loader: PASS")
