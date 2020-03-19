import time
import RPi.GPIO as GPIO
import os

def shutdownButton():
    pin_num = 3
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(pin_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pin_num, GPIO.FALLING)
        counter = 0

        while True:
            sw_status = GPIO.input(pin_num)

            if sw_status == 0:
                counter = counter + 1
                if counter >= 50:
                    GPIO.cleanup()
                    os.system("system shutdown")
                    os.system("sudo shutdonw -h now")
            
            else:
                os.system("button pushed")
                break

if __name__ == "__main__":
    shutdownButton()