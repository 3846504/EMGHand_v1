import datetime

class day:
    __date = "yyyy_mm_dd"

    def __init__(self):
        __today = datetime.datetime.now()
        self.__date = str(__today.year) + "_" + str(__today.month) + "_" + str(__today.day)

    def now(self):
        return self.__date