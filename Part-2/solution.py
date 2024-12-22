# -*- coding: utf-8 -*-
"""IML_Lab 7_B21BB006.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NC1DeZWll6iUsTiyvywN42S84xMgkz74
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

df= pd.read_csv("/content/iris.csv", header=None, names = ["sepal length in cm","sepal width in cm","petal length in cm","petal width in cm","class" ])
df.head()

df.fillna(method ='ffill', inplace = True)
df

df.info

column = np.array(df.columns)
new_data = df[:]
# print(new_data)
for i in column:
  # print(data[i])
  if(i=="class"):
    continue

  percentile25 = df[i].quantile(0.25)
  percentile75 = df[i].quantile(0.75)
  iqr = percentile75 - percentile25
  upperlimit = percentile75 + 1.5*iqr
  lowerlimit = percentile25 - 1.5*iqr

  new_data= new_data[(new_data[i] < upperlimit) & (new_data[i] > lowerlimit)]
 
  
new_data

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
X = new_data.iloc[:,:-1]
minmax.fit(X)
minmaxdata = minmax.transform(X)

df_data = pd.DataFrame(minmaxdata)
df_data = df_data.dropna(axis=0)
df_data.columns = ["sepal length in cm","sepal width in cm","petal length in cm","petal width in cm"]
df_data

df_data["Class"]=new_data["class"]
df_data

df_data.fillna(method ='ffill', inplace = True)
df_data

x=df_data.iloc[:,:-1]
y=df_data.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train ,x_test , y_train , y_test  = train_test_split( x , y , test_size = 0.2, random_state=30)

x_train.head()

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
model.score(x_test, y_test)

from sklearn.decomposition import PCA

pca = PCA(0.95)
X_pca = pca.fit_transform(X)
X_pca.shape

pca.explained_variance_ratio_

pca.n_components_

X_pca

X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)

pca = PCA(n_components=4)
X_pca = pca.fit_transform(X)
X_pca.shape

X_pca

pca.explained_variance_ratio_

X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)
X_pca.shape

X_pca

pca.explained_variance_ratio_

X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
X_pca.shape

X_pca

pca.explained_variance_ratio_

X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)

from sklearn.decomposition import PCA

pca = PCA(0.8)
X_pca = pca.fit_transform(X)
X_pca.shape

pca.explained_variance_ratio_

pca.n_components_

X_pca

X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)