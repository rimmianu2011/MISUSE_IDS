from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Assuming you have X and Y as your data and labels
# Load your CSV file into a pandas DataFrame
df = pd.read_csv('combined_data.csv')

# Extract features and labels
y = df['attack']
X = df.drop(columns=['attack'])  # Drop the 'class_name' column to get features

# Split the data into training and testing sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)


# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=1, random_state=1)

# Train the Random Forest model
rf_classifier.fit(X_train, y_train)

# Make predictions on the Validation set
Y_pred = rf_classifier.predict(X_val)

# Evaluate the model
accuracy = accuracy_score(y_val, Y_pred)
print("Accuracy:", accuracy)

# You can also print a classification report for more detailed metrics
print(classification_report(y_val, Y_pred))
joblib.dump(rf_classifier, 'random_forest_model.pkl')