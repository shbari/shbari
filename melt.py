import pandas as pd
import numpy as np

def process_wide_data(input_file, output_file):
    # Read data from the file
    df = pd.read_csv(input_file)

    # Melt the DataFrame to merge days into rows
    melted_data = pd.melt(df, id_vars=['location', 'year', 'month'], var_name='day', value_name='temperature')

    # Convert 'day' column to numeric for correct sorting
    melted_data['day'] = pd.to_numeric(melted_data['day'], errors='coerce')

    # Filter out rows where 'day' exceeds the number of days in the corresponding month
    melted_data = melted_data[melted_data['day'] <= melted_data.apply(lambda row: pd.Timestamp(f'{int(row["year"])}-{int(row["month"])}-1').days_in_month, axis=1)]

    # Sort the DataFrame based on 'year', 'month', and 'day'
    sorted_data = melted_data.sort_values(by=['year', 'month', 'day']).reset_index(drop=True)

    # Save the resulting DataFrame to a CSV file
    sorted_data.to_csv(output_file, index=False, na_rep='NaN')

# Example usage
process_wide_data('melt_data.csv', 'Melted_data.csv')