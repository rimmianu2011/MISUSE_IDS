"""
Project 1 (Misuse-based IDS)
Group : 3
File_name : select_labels.py 
@authors : Eshaan Deshpande, Venkat Anurag Nandigala, Anushka Yadav
"""

import pandas as pd

# Path to where the CSV data file is stored.
path = 'Labels/ssl_renegotiation_labels.csv'

# Reads the CSV file using panda without the column names
df = pd.read_csv(path, header=None)

# The following 2 lines extracts 5000 rows each, that have values '0' and
# and values '1'.
# Select 5000 rows where the value of the second column (at index 1) is 0
df_where_0 = df[df[1] == 0].head(5000)

# Select 5000 rows where the value of the second column (at index 1) is 1
df_where_1 = df[df[1] == 1].head(5000)

# The retrieved 5000 values of '0' and '1' each, are then combined. 
# The two DataFrames are merged into one.
selected_data = pd.concat([df_where_0, df_where_1])

# This lines replaces the value 1 with the value 3.
selected_data[1] = selected_data[1].replace(1,3)

# Exports the selected data to a new CSV file.
selected_data.to_csv('selected_ssl_renegotiation.csv', index=False, header=False)