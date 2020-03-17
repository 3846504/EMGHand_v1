import RPi.GPIO as GPIO
import time
import os

class motor:    #TODO: 動作確認
    #---- モータについてのセットアップ ----#
    __gp_out1 = 18
    __gp_out2 = 17
    __gp_out3 = 27
    __gp_out4 = 24

    GPIO.setup(__gp_out1, GPIO.OUT)
    GPIO.setup(__gp_out2, GPIO.OUT)
    GPIO.setup(__gp_out3, GPIO.OUT)
    GPIO.setup(__gp_out4, GPIO.OUT)

    #700µs~2300µs(270°) neutral=1500µs
    #7~23%
    __servo1 = GPIO.PWM(__gp_out1, 100)
    __servo2 = GPIO.PWM(__gp_out2, 100)
    __servo3 = GPIO.PWM(__gp_out3, 100)
    __servo4 = GPIO.PWM(__gp_out4, 100)
    #-------------------------------------#

    #---- 動作開始 ----#
    #パルスの初期化 5秒間の間に電源を入れる
    __servo1.start(0)
    __servo2.start(0)
    __servo3.start(0)
    __servo4.start(0)

    __ang1 = 20 #親指開閉
    __ang2 = 20 #親指内外転
    __ang3 = 20 #4指手のひら
    __ang4 = 20 #4指手の甲

    __servo1.ChangeDutyCycle(__ang1)
    __servo2.ChangeDutyCycle(__ang2)
    __servo3.ChangeDutyCycle(__ang3)
    __servo4.ChangeDutyCycle(__ang4)

    def LoS(self):
        self.__ang1 = 20
        self.__ang2 = 20
        self.__ang3 = 20
        self.__ang4 = 20

        self.__servo1.ChangeDutyCycle(self.__ang1)
        self.__servo2.ChangeDutyCycle(self.__ang2)
        self.__servo3.ChangeDutyCycle(self.__ang3)
        self.__servo4.ChangeDutyCycle(self.__ang4)

    def thumbOpen(self):
        self.__ang1 = 23
        self.__servo1.ChangeDutyCycle(self.__ang1)

    def thumbClose(self):
        self.__ang1 = 15
        self.__servo1.ChangeDutyCycle(self.__ang1)

    def thumbAddc(self):
        self.__ang2 = 13
        self.__servo2.ChangeDutyCycle(self.__ang2)

    def thumbAbdc(self):
        self.__ang2 = 23
        self.__servo2.ChangeDutyCycle(self.__ang2)

    def fingOpen(self):
        self.__ang3 = 23
        self.__ang4 = 23
        self.__servo3.ChangeDutyCycle(self.__ang3)
        self.__servo4.ChangeDutyCycle(self.__ang4)

    def fingClose(self):
        self.__ang3 = 11
        self.__ang4 = 11
        self.__servo4.ChangeDutyCycle(self.__ang4)
        self.__servo3.ChangeDutyCycle(self.__ang3)

    def __del__(self):
        self.__servo1.stop()
        self.__servo2.stop()
        self.__servo3.stop()
        self.__servo4.stop()