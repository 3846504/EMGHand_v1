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

    #### public member ####

    #### private method ####
    def __init__(self, ch_num=5, slct=0):
        self.__ch_num = ch_num
        self.__slct = slct

    #### public method ####
    def saveData(self):
        for adch in range(self.__ch_num):
            cmnd = ( 0b00011000 + adch ) << 2

            c, raw = self.__pi.spi_xfer(self.__hndl,[cmnd,0,0]) # 最初の要素が命令の入力
            print(c)
            print(raw)

            data = ((raw[1] & 0b11111111) <<  4) + \
                    ((raw[2] & 0b11110000) >>  4)

            self.__data_arr.addData(data)
    
    def shapeData(self):
        self.__data_arr.shaping()

    def getData(self):
        return self.__data_arr

    def __del__(self):
        self.__pi.spi_close(self.__hndl)   
        self.__pi.stop()