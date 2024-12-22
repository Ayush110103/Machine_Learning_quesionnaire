# -*- coding: utf-8 -*-
"""IML_Lab5_B21BB006.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UjFNV3VEP-MrhBP2FV6dggF7XIRKyBNP

QUESTION 1
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

#opening file

df=pd.read_csv('/content/penguins_lter.csv - penguins_lter.csv',encoding='windows-1252')
df

df.info()

df.describe()

#filling null values with value from above row/column respectively
df.fillna(method ='ffill', inplace = True)
df

df.hist( bins=50, figsize=(10, 10))

#plotting the scatter plots
from pandas.plotting import scatter_matrix
scatter_matrix( df, figsize=(20,20))

for columns in df.columns:
  print( columns)

print('\n\n\n')
for attribute in ['Species', 'Island', 'Sex']:
  fig,ax=plt.subplots()
  df[attribute].value_counts().plot(ax=ax,kind='pie')

#coverting all categorical data types to numerical data types
from sklearn.preprocessing import OneHotEncoder
# define one hot encoding
encoder = OneHotEncoder( drop = "first", sparse = False)
onehot = encoder.fit_transform(df[["Sex","Species","Region","Island"]])
print(onehot)

#initalized a new dictionary by adding the converted nominal values to numerical along with the older numerical ones
d = {
    'Species': onehot[:, 1],
    'Region': onehot[:, 2],
    'Island': onehot[:, 3],
     'Culmen Length (mm)' : df.iloc[:,3],
     'Culmen Depth (mm)' : df.iloc[:,4],
     'Flipper Length (mm)' : df.iloc[:,5],
     'Body Mass (g)' : df.iloc[:,6],
    'Sex': onehot[:, 0]
}

new_data = pd.DataFrame.from_dict(d)
new_data

#Spliting the dataset into training-validation-test splits
from sklearn.model_selection import train_test_split

for columns in new_data.columns:
  print( columns)

train_set, val_plus_test_set = train_test_split(new_data, test_size=0.3, random_state=40)
val_set, test_set = train_test_split(new_data, test_size=0.1, random_state=40)

X_train= train_set[['Culmen Length (mm)', 'Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']]
y_train= train_set.loc[:, train_set.columns=='Species']
X_val= val_set[['Culmen Length (mm)', 'Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']]
y_val= val_set.loc[:, val_set.columns=='Species']

X_train.head()

y_train.head()

X_val.head()

y_val.head()

#Making tree with parameter max depth and min_samples_leafs for different values
#max Depth =5 and  min_samples_leaf=2
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

tree_clf= DecisionTreeClassifier(criterion='entropy', max_depth=5, min_samples_leaf= 2)
tree_clf.fit( X_train, y_train)

y_pred= tree_clf.predict( X_val)

z1=accuracy_score( y_pred, y_val)
print( accuracy_score( y_pred, y_val))


#plotting the diagram

from sklearn import tree
import matplotlib.pyplot as plt


fn=['Culmen Length (mm)',
    'Culmen Depth (mm)',
    'Flipper Length (mm)',
    'Body Mass (g)']

cn=['Adelie Penguin',
    'Gentoo penguin',
    'Chinstrap penguin']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (16,6), dpi=300)
tree.plot_tree(tree_clf,
               feature_names = fn, 
               class_names=cn,
               filled = True);
fig.savefig('penguin_tree.png')

#max Depth =10 and  min_samples_leaf=7
tree_clf1= DecisionTreeClassifier(criterion='entropy', max_depth=10, min_samples_leaf= 7)
tree_clf1.fit( X_train, y_train)

y_pred= tree_clf1.predict( X_val)
z2=accuracy_score( y_pred, y_val)

print( accuracy_score( y_pred, y_val))


#plotting the diagram

from sklearn import tree
import matplotlib.pyplot as plt


fn=['Culmen Length (mm)',
    'Culmen Depth (mm)',
    'Flipper Length (mm)',
    'Body Mass (g)']

cn=['Adelie Penguin',
    'Gentoo penguin',
    'Chinstrap penguin']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (16,6), dpi=300)
tree.plot_tree(tree_clf1,
               feature_names = fn, 
               class_names=cn,
               filled = True);
fig.savefig('penguin_tree.png')

#max Depth =4 and  min_samples_leaf=3
tree_clf1= DecisionTreeClassifier(criterion='entropy', max_depth=4, min_samples_leaf= 3)
tree_clf1.fit( X_train, y_train)

y_pred= tree_clf1.predict( X_val)
z2=accuracy_score( y_pred, y_val)

print( accuracy_score( y_pred, y_val))


#plotting the diagram

from sklearn import tree
import matplotlib.pyplot as plt


fn=['Culmen Length (mm)',
    'Culmen Depth (mm)',
    'Flipper Length (mm)',
    'Body Mass (g)']

cn=['Adelie Penguin',
    'Gentoo penguin',
    'Chinstrap penguin']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (16,6), dpi=300)
tree.plot_tree(tree_clf1,
               feature_names = fn, 
               class_names=cn,
               filled = True);
fig.savefig('penguin_tree.png')