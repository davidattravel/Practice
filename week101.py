# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from sklearn import preprocessing


input_data = np.array([[5.1,-2.9,3.3],[-1.2,7.8,-6.1],[3.9,0.4,2.1],[7.3,-9.9,-4.5]])

print(type(input_data))
print(input_data.shape)
print(input_data)

data_bz = preprocessing.Binarizer(threshold=2).transform(input_data)
print(data_bz)
print(input_data.mean(axis=0))

sc = preprocessing.scale(input_data,axis=0)
print(sc)

c_list = ['toronto','paris','montreal']
le = preprocessing.LabelEncoder()
le.fit(c_list)
e_list = []
for c in c_list:
    e_list.append(le.transform([c]))
print(e_list)

n_list = []
for c in c_list:
    n_list.append([c])
print(n_list)
ohe = preprocessing.OneHotEncoder()
ohe.fit(n_list)
print(ohe.transform(n_list).toarray())

