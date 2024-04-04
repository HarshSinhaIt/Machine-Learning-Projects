# prompt: deploy my model using flask

from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the saved model
model = pickle.load(open('model_KN.sav', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()
    input_data = data['data']

    # Convert the input data to a NumPy array
    input_array = np.array(input_data).reshape(1, -1)

    # Make a prediction using the model
    prediction = model.predict(input_array)

    # Convert the prediction to a string
    output = prediction[0]

    # Return the prediction as a JSON response
    return jsonify({'prediction': output})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)