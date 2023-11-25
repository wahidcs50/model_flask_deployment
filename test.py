# print(request.form.get("sepal length (cm)"))
# print(request.form.get("sepal width (cm)"))
# print(request.form.get("petal length (cm)"))
# print(request.form.get("petal width (cm)"))
      
# var_1=float(request.form['sepal length (cm)'])
# var_2=float(request.form['sepal width (cm)'])
# var_3=float(request.form['petal length (cm)'])
# var_4=float(request.form['petal width (cm)'])
# import numpy as np
# import pandas as pd
# import joblib
# from sklearn.compose import make_column_transformer
# input_data = pd.DataFrame({
#                 'sepal length (cm)': [0.01],
#                 'sepal width (cm)': [0.02],
#                 'petal length (cm)': [0.11],
#                 'petal width (cm)': [0.034]
#             })
# print(input_data)
# model=open("train_model.pkl","rb")
# print(model)
# model
# lr_model=joblib.load(model)
# print(lr_model)
# model_prediction=lr_model.predict(input_data)
# print(model_prediction)
# print(type(model_prediction))
#             app.logger.info("Loaded model successfully.")
#             model_prediction=round(float(model_prediction),2)
#             app.logger.info(f"model prediction : {model_prediction}")

###### different methods #######

# if request.method == 'POST':
#         # Get the input data from the POST request
#         input_data = request.get_json()

#         # Convert input data to DataFrame
#         input_df = pd.DataFrame.from_dict(input_data, orient='index').transpose()

#         # Load the pre-trained model
#         with open("train_model.pkl", "rb") as model_file:
#             lr_model = joblib.load(model_file)

#         # Make predictions
#         model_prediction = lr_model.predict(input_df)

#         # Return predictions as JSON
#         return jsonify({"model_predictions": list(model_prediction)})

#     # Handle GET request (optional)
#     return "This endpoint requires a POST request."

# def predict():
    
#     input_data = pd.DataFrame({
#                     'sepal length (cm)': [0.01],
#                     'sepal width (cm)': [0.02],
#                     'petal length (cm)': [0.11],
#                     'petal width (cm)': [0.034]
#                 })
#     print(input_data)
#     model=open("train_model.pkl","rb")
#     print(model)
#     model
#     lr_model=joblib.load(model)
#     print(lr_model)
#     model_prediction=lr_model.predict(input_data)
#     print(model_prediction)
#     return ("model predictions: {}".format(list(model_prediction)))

##### errors #####

# to check the http request in postman use rquest.jason in the flask code 
# instead of request.form so that postman can get in the right jason format
