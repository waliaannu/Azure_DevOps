import pandas as pd

# Load the data
df = pd.read_csv("claims_data.csv")

# Data type correction
df['claim_amount'] = pd.to_numeric(df['claim_amount'], errors='coerce')  # Fix incorrect data types
df['service_date'] = pd.to_datetime(df['service_date'], errors='coerce')  # Parse dates

# Handle missing values
df.dropna(subset=['claim_amount', 'provider_id', 'service_date'], inplace=True)

# Normalize provider names
df['provider_name'] = df['provider_name'].str.strip().str.upper()

# Save the cleaned data
df.to_csv("cleaned_claims_data.csv", index=False)
print("Data cleaned and saved.")
