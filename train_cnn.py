import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from keras.utils import to_categorical
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('combined_data.csv')

# Extract features and labels
y = df['attack']
X = df.drop(columns=['attack'])  # Drop the 'class_name' column to get features
X = X.astype(float)
Y_one_hot = tf.keras.utils.to_categorical(y, num_classes=6)


print(X.shape)
print(y.shape)


# # Define the CNN model
# model = Sequential()
# model.add(Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(115, 1)))
# model.add(MaxPooling1D(pool_size=2))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(6, activation='softmax'))  # 6 output classes (1, 2, 3, 4, 5, 0)

# Define a deep 20-layer CNN model
# Define a deep 20-layer CNN model
# Define the CNN model
model = keras.Sequential()

# Input layer
model.add(layers.Input(shape=(115, 1)))  # You need to reshape the input to match your data shape

# Convolutional layers
model.add(layers.Conv1D(32, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling1D(pool_size=2))
model.add(layers.Conv1D(64, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling1D(pool_size=2))
model.add(layers.Conv1D(128, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling1D(pool_size=2))

# Flatten the output for the fully connected layers
model.add(layers.Flatten())

# Fully connected layers
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(6, activation='softmax'))  # 6 classes for multiclass classification

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Reshape X to match the input shape
#X_reshaped = X.reshape(50000, 115, 1)

# Train the model
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test data
#accuracy = model.evaluate(X_test, y_test)
#print("Test accuracy: {:.2f}%".format(accuracy[1] * 100))
