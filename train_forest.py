"""
Project 1 (Misuse-based IDS)
Group : 3
File_name : train_forest.py 
@authors : Eshaan Deshpande, Venkat Anurag Nandigala, Anushka Yadav
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib


# Reads the data using panda into a DataFrame
df = pd.read_csv('combined_data.csv')

# Extract features into 'X' and labels into 'y'.
# To extract the 'X' label the 'attack' column is dropped, this ensures
# the extraction of only numeric values. 
# The 'y' label consists of only the 'attack' column.
y = df['attack']
X = df.drop(columns=['attack'])  

# This part splits the data into training and testing sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)


# For misuse-based IDS the Random Forest Classifier model is used.
rf_classifier = RandomForestClassifier(n_estimators=1, random_state=1)

# The model is trained using the Random Forest Classifier.
rf_classifier.fit(X_train, y_train)

# Predictions are made on the Validation set
Y_pred = rf_classifier.predict(X_val)

# Evaluated the model by calculating the accuracy.
accuracy = accuracy_score(y_val, Y_pred)
print("Accuracy:", accuracy)

# Printed a classification report for more detailed metrics of the model.
print(classification_report(y_val, Y_pred))
joblib.dump(rf_classifier, 'random_forest_model.pkl')