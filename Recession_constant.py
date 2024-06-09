import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

def calculate_recession_constant(discharge_data):
    """
    Calculate the recession constant (k) from discharge data.
    """
    def exponential_decay(t, Q0, k):
        """
        Exponential decay function: Q(t) = Q0 * exp(-k*t)
        where:
        Q(t) is the discharge at time t,
        Q0 is the initial discharge,
        k is the recession constant.
        """
        return Q0 * np.exp(-k * t)

    # Create a time array
    t = np.arange(len(discharge_data))

    # Use curve fitting to find the optimal parameters
    popt, _ = curve_fit(exponential_decay, t, discharge_data)

    Q0, k = popt
    return k

# Test the function
data = pd.read_csv('Recession_data.csv')
discharge_data = data['h'].values
print(calculate_recession_constant(discharge_data))
