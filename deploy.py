import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask, request, render_template, jsonify
app = Flask(__name__, template_folder='.')
@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    model_prediction = None
    if request.method == 'POST':
        print(request.form)
        try:
            var_1 = float(request.form['sepal_length'])
            var_2 = float(request.form['sepal_width'])
            var_3 = float(request.form['petal_length'])
            var_4 = float(request.form['petal_width'])
            pred_args = [var_1, var_2, var_3, var_4]
            pred_arr = np.array(pred_args)
            preds = pred_arr.reshape(1, -1)
            model = open("train_model.pkl", "rb")
            lr_model = joblib.load(model)
            app.logger.info("Loaded model successfully.")
            model_prediction = lr_model.predict(preds)[0]
            model_prediction = round(float(model_prediction), 2)
            app.logger.info(f"model prediction: {model_prediction}")
        except ValueError:
            return "Please Enter valid values"
    return render_template("Predction.html", prediction=model_prediction)         
if __name__ == '__main__':
    app.run(debug=True)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    