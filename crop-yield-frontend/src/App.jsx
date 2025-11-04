import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    Crop: "Rice",
    Crop_Year: 1997,
    Season: "Summer",
    State: "Assam",
    Area: 1000,
    Production: 500,
    Annual_Rainfall: 2000,
    Fertilizer: 10000,
    Pesticide: 500,
  });

  const [predictedYield, setPredictedYield] = useState(null);
  const [loading, setLoading] = useState(false);

  // Units mapping for each field
  const units = {
    Crop: "",
    Crop_Year: "Year",
    Season: "",
    State: "",
    Area: "hectares (ha)",
    Production: "tonnes",
    Annual_Rainfall: "millimetres (mm)",
    Fertilizer: "kg/ha",
    Pesticide: "kg/ha",
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", formData);
      setPredictedYield(response.data.predicted_yield);
    } catch (error) {
      console.error(error);
      alert("Error fetching prediction. Make sure Flask API is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1 className="title">🌾 Crop Yield Prediction</h1>

        <form className="form-card" onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <div key={key} className="input-group">
              <label>{key.replace(/_/g, " ")}</label>
              <div className="input-with-unit">
                <input
                  type={
                    ["Crop_Year", "Area", "Production", "Annual_Rainfall", "Fertilizer", "Pesticide"].includes(key)
                      ? "number"
                      : "text"
                  }
                  name={key}
                  value={formData[key]}
                  onChange={handleChange}
                  required
                />
                {units[key] && <span className="unit">{units[key]}</span>}
              </div>
            </div>
          ))}

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Predicting..." : "Predict Yield"}
          </button>
        </form>

        {predictedYield !== null && (
          <div className="result-card">
            <h2>Predicted Yield</h2>
            <p>{predictedYield.toFixed(4)} t/ha</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
