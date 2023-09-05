import pandas as pd
import random

# Load the CSV dataset into a DataFrame
csv_file = 'dataset.csv'
df = pd.read_csv(csv_file)

# Function to generate random manufacturer prices


def generate_manufacturer_price(selling_price):
    min_price = selling_price * 0.6
    max_price = selling_price * 0.8
    return round(random.uniform(min_price, max_price), 2)


# Apply the function to add a new column 'Manufacturer Price'
df['manufacturing_cost'] = df['price'].apply(generate_manufacturer_price)

# Save the updated DataFrame back to a CSV file
output_csv_file = 'updated_dataset.csv'
df.to_csv(output_csv_file, index=False)

print(f"New dataset with manufacturer prices saved to '{output_csv_file}'")
