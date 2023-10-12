"""
Project 1 (Misuse-based IDS)
Group : 3
File_name : combine.py 
@authors : Eshaan Deshpande, Venkat Anurag Nandigala, Anushka Yadav
"""

import pandas as pd
import os
from tqdm import tqdm

# This is the directory where CSV data of 5 types of attacks is stored.
directory = "Processed_data/"  # Replace with the actual path to your directory

# this line gets the list of all the files in the directory.
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# initialized an list taht will store the data frames later.
data_frames = []

# Initialized the tqdm progress bar
progress_bar = tqdm(total=len(csv_files), position=0, leave=True)

# this part goes through each CSV file from the list and adds it into 
# DataFrames
for file in csv_files:
    file_path = os.path.join(directory, file)
    data = pd.read_csv(file_path)
    data_frames.append(data)
    # Updates the progress bar
    progress_bar.update(1)

# Closes the progress bar
progress_bar.close()

# Combines all the DataFrames into one.
combined_data = pd.concat(data_frames, ignore_index=True)

# Saves the combined data to a new CSV file named 'combined_data.csv'
combined_data.to_csv("combined_data.csv", index=False)
