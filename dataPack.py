import numpy as np

class dataPack:
    #### private member ####
    __arr = []

    __dim = 100
    __ch_num = 5

    #### public member ####

    #### private method ####
    def __init__(self, dim=100, ch_num=5):
        self.__dim = dim
        self.__ch_num = ch_num

    def __convert_1d_to_2d(self):
        pass

    #### public method ####
    def addData(self, *datas):
        for data in datas:
            self.__arr += data

    def shaping(self):  #TODO: 得られた筋電位データを望む形にするためのメソッド
        pass

    def show(self):
        return self.__arr

if __name__ == "__main__":
    data = dataPack()
    data.addData([10], [20, 30])
    print(data.show())