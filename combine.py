import pandas as pd
import os
from tqdm import tqdm

# Directory where your CSV files are located
directory = "Processed_data/"  # Replace with the actual path to your directory

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Initialize an empty list to store DataFrames
data_frames = []

# Initialize the tqdm progress bar
progress_bar = tqdm(total=len(csv_files), position=0, leave=True)

# Loop through the list of CSV files and read them into DataFrames
for file in csv_files:
    file_path = os.path.join(directory, file)
    data = pd.read_csv(file_path)
    data_frames.append(data)
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Concatenate the list of DataFrames into one
combined_data = pd.concat(data_frames, ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv("combined_data.csv", index=False)
