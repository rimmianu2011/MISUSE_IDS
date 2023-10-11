import pandas as pd

label_path = 'Processed_labels/selected_ssl_renegotiation.csv'

data_path = 'Data/SSL_Renegotiation_data.csv'

output = 'reneg.csv'

# Define column names for the first CSV file
csv1_columns = ['index', 'attack']

# Read the first CSV file with the specified column names
csv1 = pd.read_csv(label_path, names=csv1_columns, header=None)

# Define column names for the second CSV file
#csv2_columns = ['index']

# Read the second CSV file with the specified column names
csv2 = pd.read_csv(data_path,  header=None)

# Select rows from the second CSV file based on the index values from the first CSV file
selected_rows = csv2.loc[csv1.index]

# Add the second column from the first CSV file to the selected rows
selected_rows['attack'] = csv1['attack']

# Store the entire combined dataset in a new CSV file
selected_rows.to_csv(output, index=False)
