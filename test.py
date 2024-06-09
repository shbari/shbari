import numpy as np
from scipy.stats import norm

def sequential_mann_kendall_test(data, window_size):
    n = len(data)
    num_windows = n - window_size + 1
    
    # Initialize arrays to store results
    trend = np.zeros(num_windows)
    p_values = np.zeros(num_windows)
    
    for i in range(num_windows):
        window_data = data[i:i+window_size]
        
        # Calculate Mann-Kendall test statistics for the window
        n_window = len(window_data)
        S = 0
        for j in range(n_window - 1):
            for k in range(j + 1, n_window):
                S += np.sign(window_data[k] - window_data[j])
        
        var_S = (n_window * (n_window - 1) * (2 * n_window + 5)) / 18
        if S > 0:
            z = (S - 1) / np.sqrt(var_S)
        elif S < 0:
            z = (S + 1) / np.sqrt(var_S)
        else:
            z = 0
        
        # Calculate p-value using normal distribution approximation
        p_value = 2 * (1 - norm.cdf(abs(z)))
        
        # Determine trend direction
        trend[i] = 1 if S > 0 else -1 if S < 0 else 0
        p_values[i] = p_value
    
    return trend, p_values

# Example usage
np.random.seed(0)
time_series = np.random.rand(100)
window_size = 10

trend, p_values = sequential_mann_kendall_test(time_series, window_size)

# Output the results for each window
for i, (t, p) in enumerate(zip(trend, p_values)):
    print(f"Window {i+1}: Trend {'Increasing' if t == 1 else 'Decreasing' if t == -1 else 'No trend'}, p-value: {p}")
