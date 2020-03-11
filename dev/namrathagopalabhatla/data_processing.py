import os
import numpy as  np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

def read_data(path=None):
    '''Function to read dataset from file'''
    if path is None:
        print('Path not specified.')
        return None, None, None, None, None
    elif os.path.exists(path) is False:
        print('File not found.')
        return None, None, None, None, None
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    data = data.to_numpy()

    # Data processing specifically for vehicles.csv
    X = data[:, :18]
    y = data[:, -1]

    classes = np.unique(y)
    indices = list(np.arange(len(classes)))
    class_map = dict(list(zip(classes, indices)))
    y = np.array([class_map[y[i]] for i in range(len(y))])

    return X, y, class_map, data, df

def lda(X=None, y=None, k=3):
    '''Function to compute LDA of data points to k dimensions'''
    if X is None or y is None:
        return None
    model = LDA(n_components=k)
    projection = model.fit_transform(X, y)
    return projection

def pca(X=None, k=3):
    '''Function to compute PCA of data points to k dimensions'''
    if X is None:
        return None
    model = PCA(n_components=k)
    projection = model.fit_transform(X)
    return projection

def split_data(X=None, y=None, train_size=None):
    '''Function to get train-test split of the dataset'''
    if X is None or y is None:
        return None, None, None, None
    elif train_size is None:
        X_train, X_test, y_train, y_test = train_test_split(X, y)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size)

    return X_train, X_test, y_train, y_test

def visualize_data(method='LDA', X=None, y=None):
    '''Function to visualize data using LDA or PCA in 3-D'''
    if X is None or y is None:
        return False
    else: 
        if method == 'LDA': 
            projection = lda(X, y, 3)
        elif method=='PCA':
            projection = pca(X, 3)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(projection[:,0], projection[:,1], projection[:, 2], c=y)
    plt.title(method)
    plt.show()

    return True