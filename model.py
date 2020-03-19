from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

import pickle

import day

class model:
    #### private member ####
    __X_train = []
    __X_test = []
    __y_train = []
    __y_test = []

    __model = 0

    __saveFile = "Model\\yyyy_mm_dd"

    #### public member ####
    def __init__(self):
        self.__saveFile = "Model\\" + day.day().now()

    #### public method ####
    def mkModel(self, feature, target):  #TODO: モデルの作成についての関数
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(feature, target, random_state=0)
        
        best_score = float(0.0) #最大ベストスコア
        best_param_gamma = 0.01  #ベスト時のガンマ
        best_param_C = 0.0      #ベスト時のC

        progress = 0

        scores = pd.DataFrame()
    
        for C in np.linspace(0.01, 10, 10):
            svm = SVC(kernel = 'rbf', gamma=0.01, C=C)
            svm.fit(self.__X_train, self.__y_train)
            scores = scores.append(
                    {
                        'gamma': 0.01,
                        'C': C,
                        'accuracy': svm.score(self.__X_test, self.__y_test)
                    },
                    ignore_index=True)
    
            if best_score < svm.score(self.__X_test, self.__y_test):
                best_score = svm.score(self.__X_test, self.__y_test)
                best_param_gamma = 0.01
                best_param_C = C
        
            progress += 10

            print(progress)

        gamma = best_param_gamma
        C = best_param_C

        self.__model = SVC(kernel = 'rbf', gamma=gamma, C=C)

    def loadModel(self, date):  #TODO: モデルのロードについての関数
        self.__data = pickle.load(open(self.__saveFile + ".pkl", 'rb'))

    def saveModel(self, date):  #TODO: モデルのセーブについての関数
        pickle.dump(self.__model, open("Model\\" + date, "wb"))

    def predict(self, feature):
        return self.__model.predict(feature)