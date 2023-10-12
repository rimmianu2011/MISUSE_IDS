"""
Project 1 (Misuse-based IDS)
Group : 3
File_name : inference.py 
@authors : Eshaan Deshpande, Venkat Anurag Nandigala, Anushka Yadav
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Reads the CSV file and loads it into the panda DataFrames
df = pd.read_csv('Processed_data/reneg.csv')

# creates the set 'X' that includes only the features. This is done by 
# dropping the 'attack' column from the CSV data file.
X = df.drop(columns=['attack'])  

# gets the record at the specified location from 'X' and converts it to 
# numPy array
X_test = X.iloc[9414].to_numpy()

# Loads the trained Random Forest Classifier model from the saved file. 
# This model is created in the train_forest.py file. 
loaded_model = joblib.load('random_forest_model.pkl')

# Reshapes the observation to match the expected input shape 
# which is 1 sample with 115 features in this case.
sample_observation = X_test.reshape(1, -1)

# Perform inference on the reshaped observation.
predicted_class = loaded_model.predict(sample_observation)

# Prints the predicted class label for the specific entry in the CSV
# file.
print("Predicted Class:", predicted_class)
