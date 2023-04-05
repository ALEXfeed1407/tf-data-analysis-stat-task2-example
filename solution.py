import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    import scipy.stats as st
    alpha = 1 - p
    S_new = sum([item**2 for item in x])
    z1 = st.chi2.ppf(alpha/2,df= len(x)*2)
    z2 = st.chi2.ppf(1- alpha/2,df= len(x)*2)
    a = np.sqrt( S_new/(z2 * 47))
    b = np.sqrt( S_new/(z1 * 47) )
    return (a, b)

