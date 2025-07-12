import pandas as pd
import os
import time

# Path to the file CSV 
csv_path = r'r..\Datasets\flights.csv'
parquet_path = csv_path.replace('.csv', '.parquet')

# Verify is file exists
if not os.path.exists(csv_path):
    print(f" The File does not exist: {csv_path}")
    exit()

# Read CSV and calculate the time
print(" Reading CSV...")
start_csv = time.time()
df = pd.read_csv(csv_path, low_memory=False, encoding='latin1')  # Change encoding if necessary
end_csv = time.time()
csv_read_time = end_csv - start_csv
print(f" CSV reading time: {csv_read_time:.2f} seconds")

# Store as Parquet and calculate the time
print(" Save as Parquet...")
start_parquet_save = time.time()
df.to_parquet(parquet_path, engine='pyarrow', compression='snappy')
end_parquet_save = time.time()
parquet_write_time = end_parquet_save - start_parquet_save
print(f"  Parquet storage time: {parquet_write_time:.2f} seconds")

# measure weight of the files
csv_size_mb = os.path.getsize(csv_path) / (1024 * 1024)
parquet_size_mb = os.path.getsize(parquet_path) / (1024 * 1024)

# Compression metrics
size_diff = csv_size_mb - parquet_size_mb
reduction_pct = (size_diff / csv_size_mb) * 100
compression_factor = csv_size_mb / parquet_size_mb

print(f"\n CSV size:     {csv_size_mb:.2f} MB")
print(f" Parquet size: {parquet_size_mb:.2f} MB")

print(f"\n Absolute reduction: {size_diff:.2f} MB")
print(f" Porcentage reduction: {reduction_pct:.2f}%")
print(f" Compression factor: x{compression_factor:.2f}")

# Read Parquet y calculate the time
print("\n Reading Parquet...")
start_parquet_read = time.time()
df_parquet = pd.read_parquet(parquet_path)
end_parquet_read = time.time()
parquet_read_time = end_parquet_read - start_parquet_read
print(f" Parquet reading time: {parquet_read_time:.2f} seconds")

# Compare content.
data_equal = df.equals(df_parquet)
print(f"\n ¿Dataframes are the same?: {data_equal}")
