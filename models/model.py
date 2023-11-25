import pandas as pd
import numpy as np
import sklearn 
import joblib
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
df= load_iris()
 
df_iris = pd.DataFrame(data=df.data, columns=df.feature_names)
df_iris['target'] = df.target
X=df_iris.loc[:,df_iris.columns !='target']
# print(f"features:\n {X}")
Y=df_iris["target"]
# print("Labels:{}".format(Y))
print(df_iris.columns)
lr=LinearRegression().fit(X,Y)
print(lr.score(X,Y))

train_model=joblib.dump(lr,"train_model.pkl")

