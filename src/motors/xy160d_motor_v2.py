import RPi.GPIO as GPIO
from time import sleep

class Motor:

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


##########################################################################################################################
if __name__ == "__main__":
    robotMotor = Motor(m1_in1=27, m1_in2=22, m1_en=16, m2_in1=17, m2_in2=4, m2_en=19)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("m-run \
           s-stop \
           f-forward \
           b-backward \
           1-low \
           2-medium \
           3-high \
           l-left \
           r-right \
           e-exit")
    print("\n")

    temp1 = 1

    while (1):
        x = raw_input()

        if x == 'm':
            print("run")
            if (temp1 == 1):
                robotMotor.forward()
                x = 'z'
            else:
                robotMotor.backward()
                x='z'

        elif x=='s':
            robotMotor.stop()
            x='z'

        elif x=='f':
            robotMotor.forward()
            temp1 = 1
            x='z'

        elif x=='b':
            robotMotor.backward()
            temp1 = 0
            x='z'

        elif x=='1':
            robotMotor.low()
            x='z'

        elif x=='2':
            robotMotor.medium()
            x='z'

        elif x=='3':
            robotMotor.high()
            x='z'

        elif x=='l':
            robotMotor.left()
            x='z'

        elif x=='r':
            robotMotor.right()
            x='z'

        elif x=='e':
            del robotMotor
            break

        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")

