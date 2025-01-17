# -*- coding: utf-8 -*-
"""IML_ Lab6_B21BB006.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U5R5yCi0fIpYHiImhLljSEcypRamdlwq
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

#opening file
DataLabels=[" Alcohol","Malic acid","Ash","Alcalinity of ash" ,"Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines"
 	,"Proline"]
df= pd.read_csv("/content/wine.csv", header=None, names=DataLabels )
df.head()
df

df.fillna(method ='ffill', inplace = True)
df

iris = pd.read_csv("/content/wine.csv", header=None, names = ["Wine type"," Alcohol","Malic acid","Ash","Alcalinity of ash" ,"Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines"
 	,"Proline"])
iris

"""(a)Taking all the pairs of attribute."""

x = iris.iloc[:,1:].values
x

true_labels = iris.iloc[:,0]
true_labels = true_labels.values
true_labels_list = []
class_names = ['1','2','3']
for i in true_labels:
  if i=='1':
    true_labels_list.append(1)
  elif i=='2':
    true_labels_list.append(0)
  else:
    true_labels_list.append(2)

sns.set_style("whitegrid")
sns.pairplot(iris,size=3);
plt.show()

sns.set_style("whitegrid")
sns.pairplot(iris,hue = 'Wine type',size=3);
plt.show()

"""Taking certain pairs of  attributes to get more observation.
Part (a)-(b):Taking Alcohol and Colour Intensity as pairs.



"""

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
X=df.iloc[:,:]
minmax.fit(X)
minmaxdata = minmax.transform(X)
df=pd.DataFrame(minmaxdata)

d = df.dropna(axis=0)
d.columns = ["Alcohol","Malic acid","Ash","Alcalinity of ash" ,"Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines"
 	,"Proline"]
d

plt.scatter(d.Alcohol,d['Color intensity'])
plt.xlabel('Alcohol')
plt.ylabel('Color intensity')

from sklearn.cluster import KMeans
km= KMeans(n_clusters=3)
y_predicted = km.fit_predict(d[['Alcohol','Color intensity']])
y_predicted

km.cluster_centers_

d['cluster1']=y_predicted
d.head()

df1 = d[d.cluster1==0]
df2 = d[d.cluster1==1]
df3 = d[d.cluster1==2]
plt.scatter(df1.Alcohol,df1['Color intensity'],color='green')
plt.scatter(df2.Alcohol,df2['Color intensity'],color='red')
plt.scatter(df3.Alcohol,df3['Color intensity'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Alcohol')
plt.ylabel('Color intensity')
plt.legend()

#Elbow Plot
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(d[['Alcohol','Color intensity']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)

print("The curve looks like an elbow. In the above plot, the elbow is at k=3 (i.e. Sum of squared distances falls suddenly) indicating the optimal k for this dataset is 3.")

"""Taking Flavanoids and Color intensity as pairs.

"""

plt.scatter(d.Flavanoids,d['Color intensity'])
plt.xlabel('Flavanoids')
plt.ylabel('Color intensity')

from sklearn.cluster import KMeans
km= KMeans(n_clusters=4)
y_predicted = km.fit_predict(d[['Flavanoids','Color intensity']])
y_predicted

km.cluster_centers_

d['cluster2']=y_predicted
d.head()

df1 = d[d.cluster2==0]
df2 = d[d.cluster2==1]
df3 = d[d.cluster2==2]
df4 = d[d.cluster2==3]
plt.scatter(df1.Flavanoids,df1['Color intensity'],color='green')
plt.scatter(df2.Flavanoids,df2['Color intensity'],color='red')
plt.scatter(df3.Flavanoids,df3['Color intensity'],color='black')
plt.scatter(df4.Flavanoids,df4['Color intensity'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Flavanoids')
plt.ylabel('Color intensity')
plt.legend()

#Elbow Plot
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(d[['Flavanoids','Color intensity']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)

print("The curve looks like an elbow. In the above plot, the elbow is at k=4 (i.e. Sum of squared distances falls suddenly) indicating the optimal k for this dataset is 3.")

"""***(d)
Implementing K mean from Scratch.***

"""

X=d[['Alcohol', 'Color intensity']].to_numpy()

m=X.shape[0]
n=X.shape[1] 
n_iter=60
K=3
import random

# creating an empty centroid array
centroids=np.array([]).reshape(n,0) 

# creating 5 random centroids
for k in range(K):
    centroids=np.c_[centroids,X[random.randint(0,m-1)]]

output={}

# creating an empty array
euclid=np.array([]).reshape(m,0)

# finding distance between for each centroid
for k in range(K):
       dist=np.sum((X-centroids[:,k])**2,axis=1)
       euclid=np.c_[euclid,dist]

# storing the minimum value we have computed
minimum=np.argmin(euclid,axis=1)+1

# computing the mean of separated clusters
cent={}
for k in range(K):
    cent[k+1]=np.array([]).reshape(2,0)

# assigning of clusters to points
for k in range(m):
    cent[minimum[k]]=np.c_[cent[minimum[k]],X[k]]
for k in range(K):
    cent[k+1]=cent[k+1].T

# computing mean and updating it
for k in range(K):
     centroids[:,k]=np.mean(cent[k+1],axis=0)

for i in range(n_iter):
      euclid=np.array([]).reshape(m,0)
      for k in range(K):
          dist=np.sum((X-centroids[:,k])**2,axis=1)
          euclid=np.c_[euclid,dist]
      C=np.argmin(euclid,axis=1)+1
      cent={}
      for k in range(K):
           cent[k+1]=np.array([]).reshape(2,0)
      for k in range(m):
           cent[C[k]]=np.c_[cent[C[k]],X[k]]
      for k in range(K):
           cent[k+1]=cent[k+1].T
      for k in range(K):
           centroids[:,k]=np.mean(cent[k+1],axis=0)
      final=cent

plt.scatter(X[:,0],X[:,1])
plt.rcParams.update({'figure.figsize':(10,7.5), 'figure.dpi':100})
plt.title('Original Dataset')

for k in range(K):
    plt.scatter(final[k+1][:,0],final[k+1][:,1])
plt.scatter(centroids[0,:],centroids[1,:],s=300,c='yellow')
plt.rcParams.update({'figure.figsize':(10,7.5), 'figure.dpi':100})
plt.show()