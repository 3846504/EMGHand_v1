import pigpio
import dataPack

class data:
    #### private member ####    
    __ch_num = 5    #チャンネル数
    __dim = 100

    __data_arr = dataPack.dataPack() #データ保存のためのリスト

    __slct = 0          # SPI接続機器の番号 chip select gpio7
    __baud = 5000000    # 通信速度
    __flag = 0          # +256  # bin(256) = 0b100000000 は Aux SPI の利用フラグ
    __adch = 0          # MCP3208のCH0の番号

    __pi = pigpio.pi()
    __hndl = __pi.spi_open(__slct, __baud, __flag) # デバイスオープン

    #### private method ####
    def __init__(self, ch_num=5, slct=0):
        self.__ch_num = ch_num
        self.__slct = slct

    #### public method ####
    def saveData(self, dim = 10000):
        __counter = 0
        while __counter <= dim:
            for __adch in range(self.__ch_num):
                __cmnd = ( 0b00011000 + __adch ) << 2

                __c, __raw = self.__pi.spi_xfer(self.__hndl,[__cmnd,0,0]) # 最初の要素が命令の入力

                __data = ((__raw[1] & 0b11111111) <<  4) + \
                         ((__raw[2] & 0b11110000) >>  4)

                self.__data_arr.addData(__data)

                __counter += 1
    
    def shapeData(self):
        self.__data_arr.shaping()

    def getData(self):
        return self.__data_arr

    def __del__(self):
        self.__pi.spi_close(self.__hndl)   
        self.__pi.stop()