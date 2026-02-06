import numpy as np
from scipy.stats import chi2

def kupiec_pof_test(N, x, p=0.01):
    """
    Kupiec Proportion of Failures Test (SR 11-7)
    H0: Breach rate = p (99% VaR → p=0.01)
    """
    if x > N or N == 0:
        return np.nan, np.nan
    
    # Likelihood ratio test
    lr_uc = -2 * np.log(
        ((1 - p) ** (N - x) * p ** x) /
        ((1 - x/N) ** (N - x) * (x/N) ** x)
    )
    
    p_value = 1 - chi2.cdf(lr_uc, 1)
    
    status = "PASS" if p_value > 0.05 else "FAIL"
    
    print(f"Kupiec Test (N={N}, x={x}, p={p}):")
    print(f"LR_UC = {lr_uc:.2f}")
    print(f"p-value = {p_value:.4f} ({status})")
    
    return lr_uc, p_value, status

if __name__ == "__main__":
    # Test cases
    print("Test 1: Perfect (2/250 = 0.8%)")
    kupiec_pof_test(250, 2, 0.01)
    
    print("\nTest 2: Fail (12/250 = 4.8%)")
    kupiec_pof_test(250, 12, 0.01)
