
import pandas as pd

# Load the job market dataset
df = pd.read_csv("data/raw/india_job_market_2024_2026.csv")

# Display the first five rows
print("\n--- FIRST FIVE JOBS ---")
print(df.head())

# Display dataset size
print("\n--- DATASET SIZE ---")
print("Rows and columns:", df.shape)

# Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# Display missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())