import pandas as pd
import glob

# Read and combine all three CSV files into a single DataFrame
csv_files = glob.glob('data/*.csv')
df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)

# Filter to Pink Morsel products only
df = df[df["product"] == "pink morsel"]

# Clean the price field by removing the dollar sign and converting it to a float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Create the "sales" field by multiplying the "quantity" and "price" fields
df["sales"] = df["quantity"] * df["price"]

# Keep only the required fields: "date", "sales", and "region"
output = df[["date", "sales", "region"]]

# Save the output to a single CSV file named "pink_morsel_sales.csv"
output.to_csv("pink_morsel_sales.csv", index=False)

print(f"Wrote {len(output)} rows to pink_morsel_sales.csv")