import pandas as pd
import time

# Path to the CSV and Parquet files
csv_path = r'r..\Datasets\flights.csv'
parquet_path = csv_path.replace('.csv', '.parquet')

# Read CSV and measure time
start_csv = time.time()
df_csv = pd.read_csv(csv_path, encoding='latin1', sep=';')
end_csv = time.time()
csv_time = end_csv - start_csv

# Read Parquet and measure time
start_parquet = time.time()
df_parquet = pd.read_parquet(parquet_path)
end_parquet = time.time()
parquet_time = end_parquet - start_parquet

# Cpompare file times
print(f"⏱ Tiempo de lectura CSV:     {csv_time:.4f} segundos")
print(f"⏱ Tiempo de lectura Parquet: {parquet_time:.4f} segundos")

# Compare files if are equals
print("\n¿Los dataframes son iguales?:", df_csv.equals(df_parquet))
