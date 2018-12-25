################################################
# Class for motor using XY-160D motor shield
################################################

import RPi.GPIO as GPIO
# from time import sleep
# import curses

class Motor:

    # correct pin settings on 24.12.2018 for XY-160D
    # in1 = 27
    # in2 = 22
    # en1 = 16
    # in3 = 17
    # in4 = 4
    # en2 = 19

    def __init__(self, m1_in1, m1_in2, m1_en, m2_in1, m2_in2, m2_en):
        self.m1_in1 = m1_in1
        self.m1_in2 = m1_in2
        self.m1_en = m1_en
        self.m2_in1 = m2_in1
        self.m2_in2 = m2_in2
        self.m2_en = m2_en

        GPIO.setmode(GPIO.BCM)
        #
        GPIO.setup(self.m1_in1, GPIO.OUT)
        GPIO.setup(self.m1_in2, GPIO.OUT)
        GPIO.setup(self.m1_en, GPIO.OUT)
        #
        GPIO.setup(self.m2_in1, GPIO.OUT)
        GPIO.setup(self.m2_in2, GPIO.OUT)
        GPIO.setup(self.m2_en, GPIO.OUT)
        #
        self.__pw1 = GPIO.PWM(self.m1_en, 1000)
        self.__pw2 = GPIO.PWM(self.m2_en, 1000)
        self.__pw1.start(25)
        self.__pw2.start(25)

    def forward_m1(self, pwm1):
        self.__pw1.ChangeDutyCycle(pwm1)
        GPIO.output(self.m1_in1,GPIO.HIGH)
        GPIO.output(self.m1_in2,GPIO.LOW)

    def forward_m2(self, pwm2):
        self.__pw2.ChangeDutyCycle(pwm2)
        GPIO.output(self.m2_in1,GPIO.LOW)
        GPIO.output(self.m2_in2,GPIO.HIGH)

    def backward_m1(self, pwm1):
        self.__pw1.ChangeDutyCycle(pwm1)
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.HIGH)

    def backward_m2(self, pwm2):
        self.__pw2.ChangeDutyCycle(pwm2)
        GPIO.output(self.m2_in1, GPIO.HIGH)
        GPIO.output(self.m2_in2, GPIO.LOW)

    def stop_m1(self, pwm1):
        self.__pw1.ChangeDutyCycle(pwm1)
        GPIO.output(self.m1_in1,GPIO.LOW)
        GPIO.output(self.m1_in2,GPIO.LOW)

    def stop_m2(self, pwm2):
        self.__pw2.ChangeDutyCycle(pwm2)
        GPIO.output(self.m2_in1,GPIO.LOW)
        GPIO.output(self.m2_in2,GPIO.LOW)

    ### old version ###
    def forward(self):
        GPIO.output(self.m1_in1,GPIO.HIGH)
        GPIO.output(self.m1_in2,GPIO.LOW)
        GPIO.output(self.m2_in1,GPIO.LOW)
        GPIO.output(self.m2_in2,GPIO.HIGH)
        print("forward")
        #temp1 = 1

    def backward(self):
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.HIGH)
        GPIO.output(self.m2_in1, GPIO.HIGH)
        GPIO.output(self.m2_in2, GPIO.LOW)
        print("backward")
        #temp1 = 0

    def stop(self):
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.LOW)
        GPIO.output(self.m2_in1, GPIO.LOW)
        GPIO.output(self.m2_in2, GPIO.LOW)
        print("stop")

    def low(self):
        print("low")
        self.__pw1.ChangeDutyCycle(30)
        self.__pw2.ChangeDutyCycle(30)

    def medium(self):
        print("medium")
        self.__pw1.ChangeDutyCycle(60)
        self.__pw2.ChangeDutyCycle(60)

    def high(self):
        print("high")
        self.__pw1.ChangeDutyCycle(85)
        self.__pw2.ChangeDutyCycle(85)

    def left(self):
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.LOW)
        GPIO.output(self.m2_in1, GPIO.LOW)
        GPIO.output(self.m2_in2, GPIO.HIGH)
        print("left")

    def right(self):
        GPIO.output(self.m1_in1, GPIO.HIGH)
        GPIO.output(self.m1_in2, GPIO.LOW)
        GPIO.output(self.m2_in1, GPIO.LOW)
        GPIO.output(self.m2_in2, GPIO.LOW)
        print("right")

    def __del__(self):
        GPIO.cleanup()

