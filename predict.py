import pandas as pd
import joblib

# -------------------------------
# 1️⃣ Load the trained model
# -------------------------------
model_path = "model/crop_yield_model.pkl"
model = joblib.load(model_path)
print("Model loaded successfully!")

# -------------------------------
# 2️⃣ Prediction function
# -------------------------------
def predict_yield(user_input_dict):
    """
    Predict crop yield for a single input.
    
    user_input_dict example:
    {
        "Crop": "Rice",
        "Crop_Year": 1997,
        "Season": "Summer",
        "State": "Assam",
        "Area": 1000,
        "Production": 500,
        "Annual_Rainfall": 2000,
        "Fertilizer": 10000,
        "Pesticide": 500
    }
    """
    user_df = pd.DataFrame([user_input_dict])
    pred = model.predict(user_df)
    return float(pred[0])

# -------------------------------
# 3️⃣ Example single prediction
# -------------------------------
example_input = {
    "Crop": "Rice",
    "Crop_Year": 1997,
    "Season": "Summer",
    "State": "Assam",
    "Area": 1000,
    "Production": 500,
    "Annual_Rainfall": 2000,
    "Fertilizer": 10000,
    "Pesticide": 500
}

predicted_yield = predict_yield(example_input)
print(f"Predicted Yield (single input): {predicted_yield:.4f}")

# -------------------------------
# 4️⃣ Optional: Predict from a test CSV
# -------------------------------
try:
    test_df = pd.read_csv("crop_yield_test.csv")
    print(f"\nLoaded test data: {test_df.shape[0]} rows")
    
    test_predictions = model.predict(test_df)
    test_df["Predicted_Yield"] = test_predictions
    
    # Save predictions
    test_df.to_csv("crop_yield_test_predicted.csv", index=False)
    print("Predictions saved to crop_yield_test_predicted.csv")
except FileNotFoundError:
    print("\ncrop_yield_test.csv not found. Skipping batch predictions.")
