import RPi.GPIO as GPIO
from time import sleep

IR_PIN = 2
CAN_PIN = 26
OPEN_SIGNAL_PIN = 21
RESET_NUM_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(CAN_PIN, GPIO.OUT)
GPIO.setup(OPEN_SIGNAL_PIN, GPIO.OUT)
GPIO.setup(RESET_NUM_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def readIR():
    return GPIO.input(IR_PIN)

def resultIsCAN(result_is_can):
    GPIO.output(CAN_PIN, result_is_can)

def setOpenSignalPin(is_open):
    GPIO.output(OPEN_SIGNAL_PIN, is_open)

def readResetNumSw():
    if(GPIO.input(RESET_NUM_PIN) == 0):
        return True
    else:
        return False