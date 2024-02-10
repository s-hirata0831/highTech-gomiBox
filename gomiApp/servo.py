import pigpio
import time

pi = pigpio.pi()
def setAnglePET(angle):
    SERVO_PIN = 18
    assert 0 <= angle <= 180, '0to180only'
    
    pulse_width = (angle / 180) * (2500 - 500) + 500
    
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)
    
def setAngleCAN(angle):
    SERVO_PIN = 3
    assert 0 <= angle <= 180, '0to180only'
    
    pulse_width = (angle / 180) * (2500 - 500) + 500
    
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)
    
def openPetCover():
    setAnglePET(0)

def closePetCover():
    setAnglePET(121)

def openCanCover():
    setAngleCAN(110)

def closeCanCover():
    setAngleCAN(0)
