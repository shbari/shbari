import pandas as pd
import numpy as np

def process_wide_data(input_file, output_file, value_name='Data'):
    # Read data from the file
    df = pd.read_csv(input_file)

    # Melt the DataFrame to merge days into rows
    melted_data = pd.melt(df, id_vars=['Location', 'Year', 'Month'], var_name='Day', value_name=value_name)

    # Convert 'day' column to numeric for correct sorting
    melted_data['Day'] = pd.to_numeric(melted_data['Day'], errors='coerce')

    # Filter out rows where 'day' exceeds the number of days in the corresponding month
    melted_data = melted_data[melted_data['Day'] <= melted_data.apply(lambda row: pd.Timestamp(f'{int(row["Year"])}-{int(row["Month"])}-1').days_in_month, axis=1)]

    # Sort the DataFrame based on 'year', 'month', and 'day'
    sorted_data = melted_data.sort_values(by=['Year', 'Month', 'Day']).reset_index(drop=True)
# Convert 'Day' column to integer
    sorted_data['Day'] = sorted_data['Day'].astype(int)
    # Add a new 'Date' column based on 'Year', 'Month', and 'Day' after the 'Day' column
    sorted_data.insert(sorted_data.columns.get_loc('Day') + 1, 'Date', pd.to_datetime(sorted_data[['Year', 'Month', 'Day']].astype(str).agg('-'.join, axis=1)))

    # Save the resulting DataFrame to a CSV file
    sorted_data.to_csv(output_file, index=False, na_rep='NaN')

# Example usage
process_wide_data('melt_data.csv', 'Melted_data.csv', value_name='Temperature')