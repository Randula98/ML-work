import pandas as pd
import random

# Load the CSV file into a pandas DataFrame
file_path = 'dataset.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Calculate the manufactured price into 2 decimal places based on the selling price
manufactured_prices = ["{:.2f}".format(int(random.uniform(
    selling_price * 0.6, selling_price * 0.8) for selling_price in df['price']))]

# Add the manufactured price as a new column to the DataFrame
df['manufacturing_cost'] = manufactured_prices

# Save the updated DataFrame back to a CSV file
# Replace with the desired output file path
output_file_path = 'updated_dataset.csv'
df.to_csv(output_file_path, index=False)

print(f"Manufactured prices have been added and saved to '{output_file_path}'")
