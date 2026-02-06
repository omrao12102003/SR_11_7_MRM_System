import pandas as pd
import numpy as np

def benchmark_models(hist_breaches, mc_breaches, horizon=250):
    """
    SR 11-7 Model benchmarking: Historical vs Monte Carlo VaR
    """
    hist_rate = hist_breaches.sum() / horizon
    mc_rate = mc_breaches.sum() / horizon
    
    hist_conservative = hist_rate <= 0.01
    mc_conservative = mc_rate <= 0.01
    
    better_model = "Historical" if hist_rate < mc_rate else "MonteCarlo"
    
    result = {
        "horizon": horizon,
        "historical": {
            "breaches": int(hist_breaches.sum()),
            "rate_pct": round(hist_rate * 100, 2),
            "target_1pct": hist_conservative
        },
        "monte_carlo": {
            "breaches": int(mc_breaches.sum()),
            "rate_pct": round(mc_rate * 100, 2),
            "target_1pct": mc_conservative
        },
        "winner": better_model,
        "breach_diff_pct": round(abs(hist_rate - mc_rate)*100, 2),
        "sr117_compliant": hist_conservative or mc_conservative
    }
    return result

def save_benchmark_csv(result, filename="outputs/benchmark_results.csv"):
    df = pd.DataFrame([result["historical"], result["monte_carlo"]])
    df.index = ["Historical_VaR", "MonteCarlo_VaR"]
    df.to_csv(filename)
    print(f"Benchmark saved: {filename}")

if __name__ == "__main__":
    # WSL test data
    hist_breaches = np.array([0]*247 + [1]*3)
    mc_breaches = np.array([0]*243 + [1]*7)
    
    result = benchmark_models(hist_breaches, mc_breaches)
    print("BENCHMARK RESULTS:")
    print(result)
    save_benchmark_csv(result)
