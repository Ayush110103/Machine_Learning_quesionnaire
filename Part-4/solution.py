# -*- coding: utf-8 -*-
"""Lab-9_B21BB006.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kGatITvKICARsxg8CW6FDJhJjGsfM6JP
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

#opening file
DataLabels=["variance of Wavelet Transformed image","skewness of Wavelet Transformed image","curtosis of Wavelet Transformed image","entropy of image","class"]
df= pd.read_csv("/content/data_banknote_authentication.csv", header=None, names=DataLabels )
df.head()

df.fillna(method ='ffill', inplace = True)
df

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

import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(new_data["variance of Wavelet Transformed image"],new_data["skewness of Wavelet Transformed image"],hue=new_data["class"])

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
X = new_data.iloc[:,:]
minmax.fit(X)
minmaxdata = minmax.transform(X)

df_data = pd.DataFrame(minmaxdata)
df_data = df_data.dropna(axis=0)
df_data.columns = ["variance of Wavelet Transformed image","skewness of Wavelet Transformed image","curtosis of Wavelet Transformed image","entropy of image","class"]
df_data

x = df_data.iloc[:,:-1].values
y = df_data.iloc[:,-1].values

from sklearn.model_selection import train_test_split

x_main ,x_test , y_main , y_test  = train_test_split( x , y , test_size = 0.1 )

x_train , x_val , y_train , y_val = train_test_split(x_main , y_main , test_size = 0.18 )

import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(df_data["variance of Wavelet Transformed image"],df_data["skewness of Wavelet Transformed image"],hue=df_data["class"])

"""Perceptron"""

from sklearn.linear_model import Perceptron
clf=Perceptron() 
clf.fit(x_train, y_train)

clf.score(x_test, y_test)

y_pred=clf.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

clf.coef_

clf.intercept_

"""Using K-mean Cross validiction"""

X=df_data.iloc[:,:-1]
y=df_data.iloc[:,-1]

from sklearn.model_selection import KFold
kf = KFold(n_splits=3)
kf

def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

"""K fold validation using Cross_val_score"""

from sklearn.model_selection import cross_val_score
maxi=[]
mean=[]
for i in range(2,10):
 print(cross_val_score(Perceptron(), X, y,cv=i))
 maxi.append(max(cross_val_score(Perceptron(), X, y,cv=i)))
 mean.append(sum(cross_val_score(Perceptron(), X, y,cv=i))/i)

w=mean.index(max(mean))+2

print("The best value of k using k fold validation method is",w)

"""From scratch"""

class Perceptron:
  def __init__(self,learning_rate,n_iters=1000):
    self.lr=learning_rate
    self.n_iters=n_iters
    self.activation_func=self.unit_step_func
    self.weights=None
    self.bais=None
  
  def unit_step_func(self,x):
    return np.where(x>=0,1,0)
  
  def fit(self,x,y):
    n_samples,n_features=X.shape
    #initialie weights
    self.weights=np.zeros(n_features)
    self.bais=0

    y_=np.array([1 if i>0 else 0 for i in y])
    for _ in range(self.n_iters):
      for idx,x_i in enumerate(x):
        linear_output=np.dot(x_i,self.weights)+self.bais
        y_predicted =self.activation_func(linear_output)
        update=self.lr*(y_[idx]-y_predicted)
        self.weights+=update*x_i
        self.bais+=update*1


  def predict (self,x):
    linear_output=np.dot(x,self.weights)+self.bais
    y_predicted=self.activation_func (linear_output)
    return y_predicted

def accuracy(y_true,y_pred):
  accuracy=np.sum(y_true==y_pred)/len(y_true)
  return accuracy

acc=[]
lr=[]
for i in range(1,26,4):
  p=Perceptron(i/10*3,n_iters=1000)
  p.fit(x_train,y_train)
  prediction=p.predict(x_test)
  lr.append(i/(10*3))
  acc.append(prediction)

print("Perceptron classifiacation accuracy  for :-",)
for i in range(len(lr)):
      
      print("learning rate=",lr[i],"is:",accuracy(y_test,acc[i]))

p=Perceptron(1,n_iters=1000)
p.fit(x_train,y_train)
prediction=p.predict(x_test)
print(accuracy(y_test,prediction))

"""SVM"""

from sklearn.svm import SVC
model = SVC()

model.fit(x_train, y_train)

model.score(x_test, y_test)

li=[]
for i in range(1,11):
  model_C = SVC(C=i)
  model_C.fit(x_train, y_train)
  li.append(model_C.score(x_test, y_test))
x=li.index(max(li))+1
print(li)
print("The best value for c is",x)

from sklearn import linear_model, svm
svm_clf = svm.SVC(C=5, kernel='rbf')
svm_clf.fit(x_train, y_train)
svm_clf.score(x_test, y_test)