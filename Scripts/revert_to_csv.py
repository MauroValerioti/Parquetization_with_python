import pandas as pd

# Path to the file Parquet 
parquet_path = r'..\Datasets\flights.parquet'
csv_path = parquet_path.replace('.parquet', '_converted.csv')

# Read parquet and store as CSV
df = pd.read_parquet(parquet_path)
df.to_csv(csv_path, index=False, encoding='latin1') # Change encoding if necessary


