import pandas as pd

# Load the CSV dataset into a DataFrame
csv_file = 'updated_dataset.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Calculate the 'Total Income' column as the product of 'Retail Price' and 'Units Sold'
df['total_income'] = df['retail_price'] * df['units_sold']

# Save the updated DataFrame back to a CSV file
output_csv_file = 'new_dataset.csv'  # Replace with your desired output file path
df.to_csv(output_csv_file, index=False)

print(f"New dataset with 'Total Income' column saved to '{output_csv_file}'")
