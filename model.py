from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

class mkModel:
    #### private member ####
    __X_train = []
    __X_test = []
    __y_train = []
    __y_test = []

    #### public member ####

    #### private method ####
    def __init__(self, features, targets):
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(features, targets, random_state=0)

    #### public method ####
    def mkModel(self):
        pass