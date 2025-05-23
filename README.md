# MISUSE_IDS – Machine Learning-based Intrusion Detection Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/ML-Scikit--Learn-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

MISUSE_IDS is a modular and reproducible machine learning pipeline designed to detect network intrusions using supervised learning. Built with a data engineering-first approach, the project walks through the complete lifecycle of preparing raw network data, engineering features, labeling threats, training a Random Forest classifier, and applying the model for batch inference.

---

## 🔍 Use Case

In cybersecurity, it's critical to detect known attack signatures in high-volume network traffic. This project focuses on misuse detection—particularly identifying **Man-in-the-Middle (MITM)** attacks—through batch data processing and machine learning.

---

## ⚙️ Workflow Overview

The pipeline is structured into the following stages:

1. **Data Ingestion & Preprocessing**  
   Raw network logs are parsed, cleaned, and converted into structured tabular datasets. Custom scripts automate data wrangling and normalization.

2. **Label Engineering**  
   Threat-specific labels (e.g., MITM) are aligned with the feature data using reference CSVs, ensuring supervised learning compatibility.

3. **Model Training**  
   A Random Forest classifier is trained using `scikit-learn` on the processed dataset. The model is serialized and saved for later use.

4. **Batch Inference**  
   The trained model is applied to new datasets to predict intrusions. Outputs can be redirected to downstream analytics or alert systems.

---

## 🧰 Tech Stack

- **Language:** Python 3.8+
- **Libraries:** pandas, NumPy, scikit-learn
- **Model:** Random Forest Classifier
- **Data Format:** CSV
- **Pipeline Type:** Batch (Modular Scripts)

---

## 📁 Project Structure

MISUSE_IDS/
├── create_dataset.py # Parses raw data and prepares feature set
├── combine.py # Combines partial datasets into a master set
├── select_labels.py # Extracts and aligns label information
├── train_forest.py # Trains Random Forest and saves model
├── inference.py # Loads model and runs predictions
├── mitm_labels.csv # Sample label file
├── random_forest_model.pkl # Serialized trained model
├── Processed_data/ # Cleaned feature sets
└── Processed_labels/ # Cleaned labels



---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install pandas numpy scikit-learn
```
### 2. Prepare the Dataset
python create_dataset.py
python combine.py
python select_labels.py


### 3. Train the Model
python train_forest.py


### 4. Run Inference
python inference.py
