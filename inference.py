from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Assuming you have X and Y as your data and labels
# Load your CSV file into a pandas DataFrame
df = pd.read_csv('Processed_data/reneg.csv')

X = df.drop(columns=['attack'])  # Drop the 'class_name' column to get features

X_test = X.iloc[9414].to_numpy()

import joblib

# Load the trained Random Forest model from the saved file
loaded_model = joblib.load('random_forest_model.pkl')

# Create a sample observation (replace this with your actual data)
sample_observation = X_test  # Assuming you want to use the first row of your test data

# Reshape the observation to match the expected input shape (1 sample with 115 features)
sample_observation = sample_observation.reshape(1, -1)

# Perform inference
predicted_class = loaded_model.predict(sample_observation)

# Print the predicted class label
print("Predicted Class:", predicted_class)
