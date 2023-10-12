"""
Project 1 (Misuse-based IDS)
Group : 3
File_name : create_dataset.py 
@authors : Eshaan Deshpande, Venkat Anurag Nandigala, Anushka Yadav
"""

import pandas as pd

# This file was executed 5 times to create a combined dataset of 5 
# different types of attacks. This leads to the creation of 5 different
# CSV files of 5 types of attacks used later for model training and 
# prediction.

label_path = 'Processed_labels/selected_ssl_renegotiation.csv'

data_path = 'Data/SSL_Renegotiation_data.csv'

output = 'reneg.csv'

# Define column names for the first CSV file
csv1_columns = ['index', 'attack']

# Read the first CSV file with the specified column names in the above name.
csv1 = pd.read_csv(label_path, names=csv1_columns, header=None)

# Reads the second CSV file
csv2 = pd.read_csv(data_path,  header=None)

# The rows from the second CSV file are chosen based on the 
# index values present in the first CSV file in the following line.
selected_rows = csv2.loc[csv1.index]

# The following line adds the 'attack' column from the first CSV file
# to the selected rows of the second CSV file.
selected_rows['attack'] = csv1['attack']

# Stored the entire combined dataset in a new CSV file, the name for this is 
# initialized above.
selected_rows.to_csv(output, index=False)
