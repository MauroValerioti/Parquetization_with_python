import matplotlib.pyplot as plt

# Real Data (modify if exists other data)
format = ['CSV', 'Parquet']
weight_mb = [93, 0.487]          # weight in MB
times_sec = [0.886, 0.431]    # time in seconds 

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: Weight of the file
axs[0].bar(format, weight_mb, color=['#FFA500', '#4CAF50'])
axs[0].set_title('Weight of the file')
axs[0].set_ylabel('MB')
axs[0].grid(True, linestyle='--', alpha=0.3)

# Chart 2: Reading time
axs[1].bar(format, times_sec, color=['#FFA500', '#4CAF50'])
axs[1].set_title('Reading time of the file')
axs[1].set_ylabel('Seconds')
axs[1].grid(True, linestyle='--', alpha=0.3)

# Add a common title
plt.suptitle('Comparation CSV vs Parquet', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Save the figure
plt.savefig('comparation_csv_parquet.png', dpi=300)

# Show the plot
plt.show()
