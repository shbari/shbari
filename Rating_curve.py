import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
# We appreciate your citation of this article if you use this code: 
# Hefzul Bari, S., Yokoo, Y., & Leong, C. (2024). A brief review of recent global trends in suspended sediment estimation studies. Hydrological Research Letters, 18(2), 51–57. 
# https://doi.org/10.3178/hrl.18.51

def fit_rating_curve(file_path, a_initial=None, b_initial=None, maxfev=None):

# load data from a csv file
    data = pd.read_csv(file_path)

# Handling non-numeric values. Make the data numeric and put NaN for non-numeric values
    data['H'] = pd.to_numeric(data['H'], errors='coerce')  # Convert 'H' column to numeric, replace non-numeric with NaN
    data['Q'] = pd.to_numeric(data['Q'], errors='coerce')  # Convert 'Q' column to numeric, replace non-numeric with NaN

# Remove rows with NaN values. It will remove a time step if any of the Q and H value is NaN
    data = data.dropna(subset=['H', 'Q'])
# Extract data from columns
    time = data['Time'].values
    river_stage = data['H'].values
    discharge = data['Q'].values

# Define the power-law function
    def power_law(h, a, b):
        return a * (h + b)**2  # N is fixed at 2
# Print a message indicating that the function is for Japanese rivers with n=2
    print("This function is for Japanese rivers. It fits Q = a * (H + b)^2. So, n is fixed at 2.")
# Get initial values and maxfev value from the user(if not defined)
    if a_initial is None:
        a_initial = float(input("Enter initial value for 'a': "))
    if b_initial is None:
        b_initial = float(input("Enter initial value for 'b': "))
    if maxfev is None:
        maxfev = int(input("Enter maxfev value: "))
    
    initial_values = [a_initial, b_initial]
# Fit the curve to the given data
    params, covariance = curve_fit(power_law, river_stage, discharge, p0=initial_values, method='lm', maxfev=maxfev)

# Extract the fitted parameters a and b
    a_fit, b_fit = params

# Generate discharge predictions using the fitted parameters
    discharge_fit = power_law(river_stage, a_fit, b_fit)

# Calculate R^2 value using NumPy
    mean_discharge = np.mean(discharge)
    ss_total = np.sum((discharge - mean_discharge)**2)
    ss_residual = np.sum((discharge - discharge_fit)**2)
    r_squared = 1 - (ss_residual / ss_total)

# Print the fitted parameters and R^2 value
    print(f"Fitted parameters: a = {a_fit:.2f}, b = {b_fit:.2f}")
    print(f"R^2 value: {r_squared:.2f}")

# Plot the results with R^2 value
    plt.scatter(discharge, river_stage, label='Observed Data')
    plt.plot(discharge_fit, river_stage, label=f'Fitted Curve: Q = {a_fit:.2f} * (H + {b_fit:.2f})^2\n$R^2$ = {r_squared:.2f}', color='red')
    plt.xlabel('Discharge ($m^3  s^{-1}$)')
    plt.ylabel('River Stage ($m$)')
    plt.legend()
    plt.show()

# Example usage
fit_rating_curve('Rating_curve.csv', a_initial=0.5, b_initial=1.0, maxfev=10000)