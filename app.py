from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Try to load the scaler (if available)
try:
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    use_scaler = True
except:
    scaler = None
    use_scaler = False


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Web form prediction route
    """
    try:
        # Extract data from form inputs
        features = [float(x) for x in request.form.values()]
        final_input = np.array([features])

        # Apply scaling if scaler exists
        if use_scaler:
            final_input = scaler.transform(final_input)

        prediction = model.predict(final_input)[0]
        result = "Water is Safe 💧" if prediction == 1 else "Water is Unsafe ⚠️"

        return render_template('home.html', prediction_text=f'Prediction: {result}')
    except Exception as e:
        return render_template('home.html', prediction_text=f'Error: {str(e)}')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    API endpoint for Postman / external requests
    """
    try:
        data = request.json['data']

        # Maintain same feature order as training
        features = np.array([[
            data['ph'],
            data['Hardness'],
            data['Solids'],
            data['Chloramines'],
            data['Sulfate'],
            data['Conductivity'],
            data['Organic_carbon'],
            data['Trihalomethanes'],
            data['Turbidity']
        ]])

        # Apply scaling if scaler exists
        if use_scaler:
            features = scaler.transform(features)

        output = model.predict(features)[0]
        result = "Water is Safe" if output == 1 else "Water is Unsafe"

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
