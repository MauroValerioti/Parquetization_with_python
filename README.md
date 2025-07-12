# CSV to Parquet Conversion – Performance & Storage Optimization

This small project is a hands-on experiment focused on **converting large CSV files into Parquet format** using Python and Pandas, with the goal of improving:

- File size (storage optimization)
- Read speed (performance benchmarking)

---

## 🔍 What I Learned

While working on this, I wanted to explore how Parquet — as a columnar, compressed file format — compares to traditional CSV files in practical terms.

Key insights:
- Parquet significantly reduces file size (up to 76% in my tests)
- It improves read time by ~50%
- Not all datasets compress equally — data types and structure matter
- Converting back to CSV ("de-parquetizing") often results in even larger files due to expansion into plain text

---

## 📁 Project Structure

Parquet/
├── datasets/
│ └── flights.csv # Sample dataset (not uploaded due to size, but you can find it in this: https://www.kaggle.com/datasets/usdot/flight-delays?resource=download)
├── scripts/
│ ├── convert_to_parquet.py # Converts CSV to Parquet
│ ├── compare_times_and_sizes.py # Benchmarks read speed and size differences
│ └── revert_to_csv.py # Converts Parquet back to CSV

## ⚙️ How to Run

1. Clone the repository:
 ``` bash
git clone https://github.com/MauroValerioti/Parquetization_with_python.git
cd parquet-experiment

2. Place your CSV file inside the datasets/ folder.

3. Run the conversion script:
python scripts/convert_to_parquet.py

4. Run the benchmarking script:
python scripts/compare_times_and_sizes.py

5. Optionally, revert to CSV:
python scripts/revert_to_csv.py
```

📦 Tools & Libraries
- Python 3.10+
- pandas
- pyarrow
- time
- os / pathlib

🧪 Example Results
- Original CSV size: 578 MB
- Converted Parquet size: 136 MB
- Compression ratio: ~76%
- CSV read time: 0.88s
- Parquet read time: 0.43s

🧠 Why This Matters
Working with large datasets is common in data pipelines, analytics, and ETL processes. Learning to optimize how data is stored and read can have a real impact on speed, cost, and scalability.
This was a quick, practical way to understand how formats like Parquet can make a difference.

## 📬 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/maurovalerioti) if you have feedback or want to connect.
