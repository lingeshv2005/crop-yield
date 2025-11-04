from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_yield

app = Flask(__name__)
CORS(app)  # ⚡ This enables CORS for all routes

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Expect JSON input
        predicted = predict_yield(data)
        return jsonify({"predicted_yield": predicted})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
