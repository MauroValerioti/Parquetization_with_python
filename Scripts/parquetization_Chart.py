import matplotlib.pyplot as plt

# Real Data from Flights dataset
formats = ['CSV', 'Parquet']
weight_mb = [578, 136]           # File sizes in MB
times_sec = [0.88, 0.43]         # Read times in seconds

# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: File weight
axs[0].bar(formats, weight_mb, color=['#FFA500', '#4CAF50'])
axs[0].set_title('File Size Comparison')
axs[0].set_ylabel('Size (MB)')
axs[0].grid(True, linestyle='--', alpha=0.3)

# Chart 2: Reading time
axs[1].bar(formats, times_sec, color=['#FFA500', '#4CAF50'])
axs[1].set_title('Reading Time Comparison')
axs[1].set_ylabel('Time (seconds)')
axs[1].grid(True, linestyle='--', alpha=0.3)

# Overall title
plt.suptitle('CSV vs Parquet – Size and Performance Comparison', fontsize=14)

# Layout adjustments
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Save and display
plt.savefig('flights_csv_parquet_comparison.png', dpi=300)
plt.show()
