import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2026-01-01', periods=250)
daily_returns = np.random.normal(-0.005, 0.12, 250)
pnl = daily_returns.cumsum() * 10000

# Force 4-6 breaches for 1500/2076 VaR levels
breach_days = np.random.choice(250, 5, replace=False)
pnl[breach_days] = np.random.uniform(1600, 2500, 5)

df = pd.DataFrame({'date': dates.strftime('%Y-%m-%d'), 'pnl': pnl.round(-1)})
df.to_csv('data/market_data/realized_pnl.csv', index=False)

print('✅ CREATED: {} days'.format(len(df)))
print('Breaches vs 1500 VaR: {}'.format((df['pnl'] > 1500).sum()))
print('Breaches vs 2076 VaR: {}'.format((df['pnl'] > 2076).sum()))
print('Last 5 PnL:', df['pnl'].tail().tolist())
