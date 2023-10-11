import pandas as pd

path = 'Labels/ssl_renegotiation_labels.csv'
# Read the CSV file without column names
df = pd.read_csv(path, header=None)

# Select 5000 rows where the value of the second column (index 1) is 0
df_where_0 = df[df[1] == 0].head(5000)

# Select 5000 rows where the value of the second column (index 1) is 1
df_where_1 = df[df[1] == 1].head(5000)

# Combine the two DataFrames
selected_data = pd.concat([df_where_0, df_where_1])
selected_data[1] = selected_data[1].replace(1,3)

# Export the selected data to a new CSV file
selected_data.to_csv('selected_ssl_renegotiation.csv', index=False, header=False)