from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [float(x) for x in data]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
