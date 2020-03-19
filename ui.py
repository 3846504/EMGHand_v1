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
    __selectButtonPin = 1
    __powerButtonPin = 2

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

    __pi.write(__ModeLED1, 0)
    __pi.write(__ModeLED2, 0)
    __pi.write(__ModeLED3, 0)

    __pi.write(__PoseLED1, 0)
    __pi.write(__PoseLED2, 0)
    __pi.write(__PoseLED3, 0)
    __pi.write(__PoseLED4, 0)
    __pi.write(__PoseLED5, 0)

    __pi.setMode(__powerButtonPin, pigpio.INPUT)
    __pi.set_pull_up_down(__powerButtonPin, pigpio.PUD_UP)
    
    __pi.setMode(__selectButtonPin, pigpio.INPUT)
    __pi.set_pull_up_down(__selectButtonPin, pigpio.PUD_UP)

    __mode = 0
    __pose = 0

    #### public member ####
    __endFlag = 0

    def __init__(self):
        pass

    def OnLED(self, num):
        self.__pi.write(num, 1)

    def OffLED(self, num):
        self.__pi.write(num, 0)

    def selectPose(self):
        return self.__mode

    def selectMode(self):
        return self.__mode

    def modeShow(self):
        return self.__actionMode

    def pushResetButton(self):
        return self.__endFlag