import numpy as np
import pandas as pd
from scipy.io import arff
import pytempo
import sys
import math
from scipy.fft import fft
from itertools import *
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale

ud = pytempo.univariate.distances

def load_dataset (path) : 
    ds = arff.loadarff(path)
    df = pd.DataFrame(ds[0])
    data=df.iloc[:,:-1].to_numpy()
    label=df.iloc[:,-1].to_numpy().astype(int)
    print(data.shape)
    return (data, label)
def scale_dataset(data):
    data = scale(data)
    return data
def fourier_transform(data):
    data = np.fft.fft(data) 
    return data

def real_imaginary_values(data):
    data = np.concatenate((data.real, data.imag,np.sqrt((data.real)**2 + (data.imag)**2), np.arctan((data.real/data.imag) )), axis=1)
    print(data.shape)
    return data

def phase_amplitude(data):
    data = np.ascontiguousarray(np.vstack((np.sqrt((data.real)**2 + (data.imag)**2), np.arctan((data.real/data.imag) ))).T)
    data_rows, data_cols = data.shape
    data = data.reshape(data_cols,data_rows)
    return data

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

def logistic_regression(np_train,np_test,np_train_label,np_test_label):
    model=LogisticRegression()
    model.fit(np_train,np_train_label)
    new_labels  = model.predict(np_test)
    ans=0
    for i in range(len(np_test_label)):
        if(new_labels[i]==np_test_label[i]):
            ans=ans+1
    ans = ans/len(np_test_label) 
    return ans

def random_forest(np_train,np_test,np_train_label,np_test_label):
    model = RandomForestClassifier(n_estimators = 100)
    model.fit(np_train,np_train_label) 
    new_labels = model.predict(np_test)
    ans=0
    for i in range(len(np_test_label)):
        if(new_labels[i]==np_test_label[i]):
            ans=ans+1
    ans = ans/len(np_test_label)        
    return ans


