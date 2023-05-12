import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template

# create flask app
app = Flask(__name__)

# load the model
model = pickle.load(open("neural_net.pickle", 'rb'))


@app.route("/")
def home():
    return render_template("index.htm")


@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    return render_template("index.htm", prediction_text="pregnant {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)