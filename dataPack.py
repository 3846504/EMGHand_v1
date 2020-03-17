class dataPack:
    #### private member ####
    __EMG = []
    __pose = []

    __dim = 100
    __ch_num = 5

    #### public member ####

    #### private method ####
    def __init__(self, dim=100, ch_num=5):
        self.__dim = dim
        self.__ch_num = ch_num

    #### public method ####
    def addData(self, pose, *datas):
        self.__pose += pose
        for data in datas:
            self.__EMG += data

    def show(self):
        return self.__EMG, self.__pose

if __name__ == "__main__":
    data = dataPack()
    data.addData([10], [20, 30])
    print(data.show())