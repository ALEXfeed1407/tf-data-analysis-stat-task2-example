import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2
    n = x.shape[0]
    sample_mean = np.mean(x)
    sample_var = np.var(x, ddof=1) / 47
    alpha = 1 - p
    t = (n - 1) * sample_var / chi2.ppf([1 - alpha/2, alpha/2], df= n - 1)
    ci_low = np.sqrt(t[0])    
    ci_high = np.sqrt(t[1])
    return ci_low, ci_high
