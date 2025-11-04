import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from preprocess import load_data, get_preprocessor

# Paths
data_path = "data/crop_yield.csv"
model_path = "model/crop_yield_model.pkl"

# Load data
df = load_data(data_path)
X = df.drop("Yield", axis=1)
y = df["Yield"]

categorical_cols = ["Crop", "Season", "State"]
numerical_cols = ["Crop_Year", "Area", "Production", "Annual_Rainfall", "Fertilizer", "Pesticide"]

# Preprocessor
preprocessor = get_preprocessor(categorical_cols, numerical_cols)

# Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
print("Training model...")
model.fit(X_train, y_train)
print("Training completed!")

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Test RMSE: {rmse:.4f}")

# Save model
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
