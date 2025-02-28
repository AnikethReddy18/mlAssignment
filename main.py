import pandas as pd

# Load dataset
df = pd.read_csv("USA Housing Dataset.csv")  # Adjust filename if needed

# Display first few rows
print(df.head())

# Check dataset info
print(df.info())

# Summary statistics
print(df.describe())
