import time 
from time import sleep 
import RPi.GPIO as GPIO
import os


#DC MOTORS

#enable_pin = 13
in1_pin =29
in2_pin =31
in3_pin=33
in4_pin=35
in5_pin=36
in6_pin=38
in7_pin=37
in8_pin=19
in9_pin=32
in10_pin=40
#servoblaster motor
servo_min = 500 # uS
servo_max = 2500# uS
servo = 0 # pin 7

def init_drivers():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    #GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(in1_pin, GPIO.OUT)
    GPIO.setup(in2_pin, GPIO.OUT)
    GPIO.setup(in3_pin, GPIO.OUT)
    GPIO.setup(in4_pin, GPIO.OUT)
    GPIO.setup(in5_pin, GPIO.OUT)
    GPIO.setup(in6_pin, GPIO.OUT)
    GPIO.setup(in7_pin, GPIO.OUT)
    GPIO.setup(in8_pin, GPIO.OUT)
    GPIO.setup(in9_pin, GPIO.OUT)
    GPIO.setup(in10_pin, GPIO.OUT)
def hand_open():
        #when open hand (1,4,5,7,9)is Hight 
	GPIO.output(in1_pin, True)
	GPIO.output(in2_pin, False)
	GPIO.output(in4_pin, True)
	GPIO.output(in3_pin, False)
	GPIO.output(in5_pin, True)
	GPIO.output(in6_pin, False)
	GPIO.output(in7_pin, True)
	GPIO.output(in8_pin, False)
	GPIO.output(in9_pin, True)
	GPIO.output(in10_pin, False)
                
def hand_close():
        #when close hand (2,3,6,8,10)is Hight
	GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, True)
	GPIO.output(in4_pin, False)
	GPIO.output(in3_pin, True)
	GPIO.output(in5_pin, False)
	GPIO.output(in6_pin, True)
	GPIO.output(in7_pin, False)
	GPIO.output(in8_pin, True)
	GPIO.output(in9_pin, False)
	GPIO.output(in10_pin, True)

def thump_open():

        GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, True)
	GPIO.output(in4_pin, False)
	GPIO.output(in3_pin, True)
	GPIO.output(in5_pin, True)
	GPIO.output(in6_pin, False)
	GPIO.output(in7_pin, False)
	GPIO.output(in8_pin, True)
	GPIO.output(in9_pin, False)
	GPIO.output(in10_pin, True)

def hand_rest():
        
        GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, False)
	GPIO.output(in4_pin, False)
	GPIO.output(in3_pin, False)
	GPIO.output(in5_pin, False)
	GPIO.output(in6_pin, False)
	GPIO.output(in7_pin, False)
	GPIO.output(in8_pin, False)
	GPIO.output(in9_pin, False)
	GPIO.output(in10_pin,False)

def hold_pen():
	
	GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, True)
	GPIO.output(in4_pin, False)
	GPIO.output(in3_pin, True)
	GPIO.output(in5_pin, True)
	GPIO.output(in6_pin, False)
	GPIO.output(in7_pin, False)
	GPIO.output(in8_pin, True)
	GPIO.output(in9_pin, False)
	GPIO.output(in10_pin, True)


def map(value, from_low, from_high, to_low, to_high):
    from_range = from_high - from_low
    to_range = to_high - to_low
    scale_factor = float(from_range) / float(to_range)
    return to_low + (value / scale_factor)
def set_angle(angle):
    pulse = int(map(angle, 0, 180, servo_min, servo_max))
    command = "echo {}={}us > /dev/servoblaster".format(servo, pulse)
    os.system(command)
    print command
