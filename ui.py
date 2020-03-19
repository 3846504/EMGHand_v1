import pigpio

class ui:   #TODO: UI（リモコン）についてのクラス　どうしましょうか？
    #### private member ####
    __actionMode = 2

    # ---- ピンについての設定 ---- #
    # ---- LED ---- #
    __ModeLED1 = 1
    __ModeLED2 = 2
    __ModeLED3 = 3

    __PoseLED1 = 1
    __PoseLED2 = 2
    __PoseLED3 = 3
    __PoseLED4 = 4
    __PoseLED5 = 5

    # ---- Button ---- #
    __selectButton = 1
    __powerButton = 2

    # ---- インスタンスの生成 ---- #
    __pi = pigpio.pi()

    # ---- モードの設定 ---- #
    __pi.setMode(__ModeLED1, pigpio.OUTPUT)
    __pi.setMode(__ModeLED2, pigpio.OUTPUT)
    __pi.setMode(__ModeLED3, pigpio.OUTPUT)

    __pi.setMode(__PoseLED1, pigpio.OUTPUT)
    __pi.setMode(__PoseLED2, pigpio.OUTPUT)
    __pi.setMode(__PoseLED3, pigpio.OUTPUT)
    __pi.setMode(__PoseLED4, pigpio.OUTPUT)
    __pi.setMode(__PoseLED5, pigpio.OUTPUT)

    #### public member ####
    endFlag = 0

    def __init__(self):
        pass

    def OnLED(self, num):
        self.__pi.write(num, 1)

    def OffLED(self, num):
        self.__pi.write(num, 0)

    def selectMode(self):
        pass

    def modeShow(self):
        return self.__actionMode