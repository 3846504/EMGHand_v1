import motor
import dataTool
import model
import day

class EMGhand:
    date = day.day().now()

    model = model.model()
    model.loadModel(date)

    EMG = dataTool.dataTool()

    motor = motor.motor()

    while(True):
        EMG.getData(100)
        EMG.mkFeature()

        prePose = model.predict(EMG.showFeature())

        if(prePose == 0):
            motor.nPos()

        elif(prePose == 1):
            motor.thumbClose()
            motor.fingClose()

        elif(prePose == 2):
            motor.thumbOpen()
            motor.fingOpen()

        elif(prePose == 3):
            motor.thumbAddc()
            motor.thumbAbdc()

