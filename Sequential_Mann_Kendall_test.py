# This is a translted version from R package pheno.
# This will compute a series of kendall's tau as described by Sneyers(1990).
# https://rdrr.io/cran/pheno/src/R/seqMK.R
import numpy as np
from scipy.stats import kendalltau
import pandas as pd

def seqMK(x):
    n = len(x)
    y = x[::-1]
    prog = np.zeros(n)
    retr = np.zeros(n)
    tp = np.zeros(n, dtype=bool)
    prog[0] = retr[0] = np.nan
    tp[0] = tp[-1] = False
    if n < 2:
        raise ValueError("seqMK: not enough finite observations")
    # progressive and retrograde series
    '''In Python, the range(start, stop) function generates a sequence of integers 
    starting from start up to, but not including, stop.'''
    for i in range(1, n):
        prog[i] = kendalltau(x[:i+1], range(i+1))[0]
        retr[i] = kendalltau(y[:i+1], range(i+1))[0]
    retr = retr[::-1]
    diff = prog - retr
    # index vector of crossing points
    for i in range(1, n-1):
        if np.sign(diff[i]) == np.sign(diff[i+1]):
            tp[i+1] = False
        else:
            tp[i+1] = True
    # Create a DataFrame from the results
    result_df = pd.DataFrame({'prog': prog, 'retr': retr, 'tp': tp})
    # Save the DataFrame to a CSV file
    result_df.to_csv('result.csv', index=False)
    return result_df

# Your time series data
x = np.array([1, 2, 3, 2, 3, 4, 5, 4, 5, 6])

# Apply the seqMK function
result = seqMK(x)
print(result)