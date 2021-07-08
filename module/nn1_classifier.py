# -*- coding: utf-8 -

import numpy as np
import pandas as pd
from scipy.io import arff
import pytempo
import sys
import math

ud = pytempo.univariate.distances

def load_dataset (path) : 
    ds = arff.loadarff(path)
    df = pd.DataFrame(ds[0])
    data=df.iloc[:,:-1].to_numpy()
    label=df.iloc[:,-1].to_numpy().astype(int)
    return (data, label)

#Euclidean
def Euclidean(np_test,np_train,np_test_label,np_train_label) :
    d=0
    for i in range(len(np_test)):
        q = np_test[i]
        min_ed =sys.maxsize
        min_y = sys.maxsize
        for j in range(len(np_train)):
            c= np_train[j]
            v = np.linalg.norm(q - c)
            if(v<min_ed):
                min_ed = v
                min_y = np_train_label[j]
        if min_y == np_test_label[i]:
            d = d + 1
    result = d/len(np_test_label)        
    return result


# DTW
def dtw(np_test,np_train,np_test_label,np_train_label):
    d=0
    for i in range(len(np_test)):
        q = np_test[i]
        min_dtw = math.inf
        min_y = math.inf
        for j in range(len(np_train)):
            c= np_train[j]
            v = ud.dtw(q, c,min_dtw)
            if(v<min_dtw):
                min_dtw = v
                min_y = np_train_label[j]
        if min_y == np_test_label[i]:
            d = d + 1
    result = d/len(np_test_label)  
    return result


#cdtw
def cdtw(np_test,np_train,np_test_label,np_train_label,w,length):
    d=0
    for i in range(len(np_test)):
        q = np_test[i]
        min_cdtw =math.inf
        min_y = math.inf
        for j in range(len(np_train)):
            c= np_train[j]
            v = ud.cdtw(q, c, round(w*(length/100)),min_cdtw)
            if(v<min_cdtw):
                min_cdtw = v
                min_y = np_train_label[j]
        if min_y == np_test_label[i]:
            d = d + 1
    result = d/len(np_test_label)  
    return result
