from flask import Flask, render_template, request, url_for,redirect
import pickle
from sklearn.preprocessing import StandardScaler

import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__, template_folder='Template')


@app.route('/')
def hello_world():
    return render_template('Home.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [x for x in request.form.values()]
    final = [np.array(int_features, dtype=float)]
    prediction = model.predict(final)
    print(prediction)
    if prediction == 1:
        return render_template('Home.html', info='Patient has Breast Cancer')
    else:
        return render_template('Home.html', info='Patient does not have Breast Cancer')


if __name__ == '__main__':
    app.run()
