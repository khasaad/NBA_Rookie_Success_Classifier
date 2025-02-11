from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the saved model (The best trained model SVC with RandomizedSearchCV)
model = joblib.load('../Models/Support_Vector_Classifier_RSV_model.pkl')

app = Flask(__name__)

# Define a scaler (This should be the same scaler used during training)
scaler = MinMaxScaler()

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.json

    # Ensure that the input data contains the required number of features
    if len(data) != 19:
        return jsonify({'error': 'Invalid input. Please provide exactly 19 features.'}), 400

    # Convert the input data to a numpy array
    input_data = np.array([data])

    # Normalize input data
    data_normalized = scaler.fit_transform(input_data)

    # Make a prediction
    prediction = model.predict(data_normalized)

    # Return the result
    result = 'Will last 5+ years' if prediction[0] == 1 else 'Will not last 5+ years'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

