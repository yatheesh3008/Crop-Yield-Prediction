# -*- coding: utf-8 -*-
"""Hack

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J8qnl810Xr0klxCn2qjTbIv8WahWHylY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('/content/crop_yield.csv.zip')
data

print("Shape of the dataset : ",data.shape)

data.isnull().sum()

data.describe()

data.head()

data.duplicated().sum()

data.head()

data['Crop_Year'] = data['Crop_Year'].astype(int)
data['Area'] = data['Area'].astype(int)
data['Production'] = data['Production'].astype(int)
data['Annual_Rainfall'] = data['Annual_Rainfall'].astype(int)
data['Pesticide'] = data['Pesticide'].astype(int)
data['Fertilizer'] = data['Fertilizer'].astype(int)

data['Crop'] = data['Crop'].astype('category')
data['Season'] = data['Season'].astype('category')
data['State'] = data['State'].astype('category')

data

col =['Crop_Year','Area','Production','Annual_Rainfall','Fertilizer','Pesticide','Crop','State','Season','Yield']
data= data[col]
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0, shuffle=True)

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
ohe = OneHotEncoder(drop='first')
scale = StandardScaler()

preprocesser = ColumnTransformer(
        transformers = [
            ('StandardScale', scale, [0,1,2,3,4,5]),
            ('OHE', ohe, [6,7,8]),
        ],
        remainder='passthrough'
)

X_train = preprocesser.fit_transform(X_train)
X_test = preprocesser.transform(X_test)

preprocesser.get_feature_names_out(col[:-1])

from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.tree import DecisionTreeClassifier

models = {
    'lr':LinearRegression(),
    'lss':Lasso(),
    'Rid':Ridge(),
    'Dtr':DecisionTreeRegressor(),


}
for name, md in models.items():
    md.fit(X_train,y_train)
    y_pred = md.predict(X_test)

    print(f"{name} : mae : {mean_absolute_error(y_test,y_pred)} score : {r2_score(y_test,y_pred)}")

dtr = DecisionTreeRegressor()
dtr.fit(X_train,y_train)
dtr.predict(X_test)



result

