import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#first (right) cell
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

#second (left) cell
GPIO.setup(9,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)



#first (right) cell
GPIO.output(2,GPIO.HIGH)
GPIO.output(3,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
GPIO.output(10,GPIO.HIGH)

#second (left) cell
GPIO.output(9,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(19,GPIO.HIGH)
GPIO.output(26,GPIO.HIGH)