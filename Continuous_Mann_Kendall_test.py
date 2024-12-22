'''This perform Mann-Kendall test continuously to a data set. This can be used as an alternative to sequential 
Mann-Kendall test. Please note that it does not compute change point.
.....................................................................
This code is tested against an python package for MK test.
............................................................................'''
'''Reference:
DOI: https://doi.org/10.1016/j.atmosres.2016.02.008
Perform the Mann-Kendall test for trend analysis. 
:param x: List or array of data points. 
:return: Z-value, p-value, and trend direction and tau.
: works python 3 and later 
'''
import numpy as np
import scipy.stats as stats
import csv
def perform_mann_kendall(x, alpha=None):
    if alpha is None: alpha = 0.05

    def mann_kendall_test(x, alpha):
        n = len(x)
        s = 0
# Calculation of S statistics
        for k in range(n-1):
            for j in range(k+1, n):
                s += np.sign(x[j] - x[k])

        unique_x = np.unique(x)
        g = len(unique_x)
# variance calculation
        if n == g: # No ties
            var_s = (n * (n - 1) * (2 * n + 5)) / 18
        else:
            tp = np.zeros(unique_x.shape)
            for i in range(len(unique_x)):
                tp[i] = sum(x == unique_x[i])
            var_s = (n * (n - 1) * (2 * n + 5) - np.sum(tp * (tp - 1) * (2 * tp + 5))) / 18
# Compute z values
        if s > 0:
            z = (s - 1) / np.sqrt(var_s)
        elif s == 0:
            z = 0
        else:
            z = (s + 1) / np.sqrt(var_s)
# Calculate p value
        p = 2 * (1 - stats.norm.cdf(abs(z))) # Two tail test
    # Determine significance 
        h = abs(z) > stats.norm.ppf(1 - alpha / 2)
# Determine trend direction
        if (z < 0) and h:
            trend = "decreasing"
        elif (z > 0) and h: 
            trend = "increasing"
        else:
            trend = "no trend"
        return z, p, h, trend
# Calculate slope
    def sen_slope(x):
        n = len(x)
        slopes = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                slopes.append((x[j] - x[i]) / (j - i))
        return np.median(slopes)
# perform continuos test
    def continuous_analysis(x, alpha):
        x = np.asarray(x).astype(float)
        x = x[~np.isnan(x)]
        n = len(x)
        z_values = []
        p_values = []
        h_values = []
        trends = []
        sen_slopes = []
        tau_values = []

        for i in range(2, n + 1):
            subset = x[:i]
            z, p, h, trend = mann_kendall_test(subset, alpha)
            z_values.append(z)
            p_values.append(p)
            h_values.append(h)
            trends.append(trend)
            sen_slope_value = sen_slope(subset)
            sen_slopes.append(sen_slope_value)
            tau, _ = stats.kendalltau(range(i), subset)
            tau_values.append(tau)
        return z_values, p_values, h_values, trends, sen_slopes, tau_values

# Apply continuous analysis with the user-provided alpha
    z_values, p_values, h_values, trends, sen_slopes, tau_values = continuous_analysis(x, alpha)

# Write results to a text file
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data_Points", "Z-Value", "P-Value", "h_values", "Trend", "Sen_Slope", "Kendall_Tau"])
        for i in range(len(z_values)):
            writer.writerow([i + 2, f"{z_values[i]:.3f}", f"{p_values[i]:.3f}", h_values[i], trends[i], f"{sen_slopes[i]:.3f}", f"{tau_values[i]:.3f}"])

# Example data
# Apply continuous analysis
alpha_input = float(input("Enter the significance level (alpha) or leave blank for default (0.05): ") or 0.05)
perform_mann_kendall(x, alpha_input)