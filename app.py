import pickle #to load regression model pickle file
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

# create app
app = Flask(__name__)
# load model
regression_model = pickle.load(open('regression_model.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

# create a predict API
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    # convert values into list and array, then reshape the array
    reshaped = np.array(list(data.values())).reshape(1,-1)
    print(reshaped)
    new_data = scaler.transform(reshaped)
    # new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))

    output = regression_model.predict(new_data)
    print(output[0]) #will be in a 2d array, pick first value
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)

    