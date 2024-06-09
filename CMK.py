'''This perform Mann-Kendall test continiuesly to a data set. This can be used as an alternative to sequential 
Mann-Kendall test. Please note that it does not compute change point.
.....................................................................
This code is not tested against known results yets. It is under development.
............................................................................'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def mann_kendall_test(x):
    x = np.array(x)
    x = x[~np.isnan(x)]

    n = len(x)
    s = 0

    for k in range(n-1):
        for j in range(k+1, n):
            s += np.sign(x[j] - x[k])

    unique_x = np.unique(x)
    g = len(unique_x)

    if n == g:
        var_s = (n * (n - 1) * (2 * n + 5)) / 18
    else:
        tp = np.zeros(unique_x.shape)
        for i in range(len(unique_x)):
            tp[i] = sum(x == unique_x[i])
        var_s = (n * (n - 1) * (2 * n + 5) - np.sum(tp * (tp - 1) * (2 * tp + 5))) / 18

    if s > 0:
        z = (s - 1) / np.sqrt(var_s)
    elif s == 0:
        z = 0
    else:
        z = (s + 1) / np.sqrt(var_s)

    p = 2 * (1 - stats.norm.cdf(abs(z)))

    if p < 0.05:
        if z < 0:
            trend = "decreasing"
        else:
            trend = "increasing"
    else:
        trend = "no trend"

    return z, p, trend

def continuous_mann_kendall(x):
    n = len(x)
    z_values = []
    p_values = []
    trends = []

    for i in range(2, n + 1):
        subset = x[:i]
        z, p, trend = mann_kendall_test(subset)
        z_values.append(z)
        p_values.append(p)
        trends.append(trend)

    return z_values, p_values, trends

# Example data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Apply continuous Mann-Kendall test
z_values, p_values, trends = continuous_mann_kendall(x)

# Plotting results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(range(2, len(x) + 1), z_values, marker='o')
plt.axhline(y=1.96, color='r', linestyle='--', label='Significance level (1.96)')
plt.axhline(y=-1.96, color='r', linestyle='--')
plt.title('Mann-Kendall Z-Values Over Time')
plt.xlabel('Number of Data Points')
plt.ylabel('Z-Value')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(range(2, len(x) + 1), p_values, marker='o')
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance level (0.05)')
plt.title('Mann-Kendall P-Values Over Time')
plt.xlabel('Number of Data Points')
plt.ylabel('P-Value')
plt.legend()

plt.tight_layout()
plt.show()
