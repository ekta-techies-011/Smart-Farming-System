import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Load dataset
try:
    df = pd.read_csv("data/Crop_recommendation.csv")
    if df.empty:
        raise ValueError("The CSV file is empty.")
except FileNotFoundError:
    print("Error: 'data/Crop_recommendation.csv' not found. Please ensure the file exists in the 'data' directory.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: The CSV file has no columns to parse. Check the file format.")
    exit(1)
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))
print("Model Accuracy:", accuracy)

# Save model
os.makedirs("models", exist_ok=True)

pickle.dump(model, open("models/crop_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

print("✅ Model and scaler saved successfully!")
