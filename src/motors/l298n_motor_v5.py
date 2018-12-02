import RPi.GPIO as GPIO
from time import sleep
import curses

class Motor:

    def __init__(self, m1_in1, m1_in2, m1_en, m2_in1, m2_in2, m2_en):
        self.m1_in1 = m1_in1
        self.m1_in2 = m1_in2
        self.m1_en = m1_en
        self.m2_in1 = m2_in1
        self.m2_in2 = m2_in2
        self.m2_en = m2_en
        #self.temp1 = 1

        # Set GPIO
        # in1 = 24
        # in2 = 23
        # en = 25
        # temp1 = 1
        #
        # # M2
        # in4 = 17
        # in3 = 27
        # en2 = 22
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

    def right(self):
        self.__pw1 = GPIO.PWM(self.m1_en, 0)
        GPIO.output(self.m1_in1,GPIO.LOW)
        GPIO.output(self.m1_in2,GPIO.LOW)
        # self.__pw2 = GPIO.PWM(self.m2_en, 1000)
        GPIO.output(self.m2_in1,GPIO.HIGH)
        GPIO.output(self.m2_in2,GPIO.LOW)
        print("rigt")
        #temp1 = 1

    def left(self):
        # self.__pw1 = GPIO.PWM(self.m1_en, 1000)
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.HIGH)
        self.__pw2 = GPIO.PWM(self.m2_en, 0)
        GPIO.output(self.m2_in1, GPIO.LOW)
        GPIO.output(self.m2_in2, GPIO.LOW)
        print("left")
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

    def forward(self):
        # self.__pw1 = GPIO.PWM(self.m1_en, 1000)
        # self.__pw2 = GPIO.PWM(self.m2_en, 1000)
        GPIO.output(self.m1_in1, GPIO.LOW)
        GPIO.output(self.m1_in2, GPIO.HIGH)
        GPIO.output(self.m2_in1, GPIO.HIGH)
        GPIO.output(self.m2_in2, GPIO.LOW)
        print("forward")

    def backward(self):
        GPIO.output(self.m1_in1, GPIO.HIGH)
        GPIO.output(self.m1_in2, GPIO.LOW)
        GPIO.output(self.m2_in1, GPIO.LOW)
        GPIO.output(self.m2_in2, GPIO.HIGH)
        print("backward")

    def __del__(self):
        GPIO.cleanup()

def main(win):
    robotMotor = Motor(m1_in1=24, m1_in2=23, m1_en=25, m2_in1=17, m2_in2=27, m2_en=22)
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

    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")

    while 1:
        try:
           key = win.getkey()
           #win.clear()
           win.addstr("Detected key:")
           win.addstr(str(key))

           if str(key) == 'KEY_UP':
               print(" forward ")
               robotMotor.forward()

           if str(key) == 'KEY_DOWN':
               print(" forward ")
               robotMotor.backward()

           if str(key) == 'KEY_RIGHT':
               print(" right ")
               robotMotor.right()

           if str(key) == 'KEY_LEFT':
               print(" left ")
               robotMotor.left()

           if str(key) == ' ':
               print(" stop ")
               robotMotor.stop()

           if str(key) == '1':
               print(" low speed ")
               robotMotor.low()
           if str(key) == '2':
               print(" medium speed ")
               robotMotor.medium()
           if str(key) == '3':
               print(" high speed ")
               robotMotor.high()

           if str(key) == 'q':
               print("quit")
               del robotMotor
               break

           if key == os.linesep:
              break

        except Exception as e:
           # No input
           #print("Exception...")
           pass
        #finally:
        #    del robotMotor
        #    break

##########################################################################################################################
if __name__ == "__main__":
    print("Start....")
    curses.wrapper(main)

########################################################################################################################
    # while (1):
    #     x = raw_input()
    #
    #     if x == 'm':
    #         print("run")
    #         if (temp1 == 1):
    #             robotMotor.forward()
    #             x = 'z'
    #         else:
    #             robotMotor.backward()
    #             x='z'
    #
    #     elif x=='s':
    #         robotMotor.stop()
    #         x='z'
    #
    #     elif x=='f':
    #         robotMotor.forward()
    #         temp1 = 1
    #         x='z'
    #
    #     elif x=='b':
    #         robotMotor.backward()
    #         temp1 = 0
    #         x='z'
    #
    #     elif x=='1':
    #         robotMotor.low()
    #         x='z'
    #
    #     elif x=='2':
    #         robotMotor.medium()
    #         x='z'
    #
    #     elif x=='3':
    #         robotMotor.high()
    #         x='z'
    #
    #     elif x=='l':
    #         robotMotor.left()
    #         x='z'
    #
    #     elif x=='r':
    #         robotMotor.right()
    #         x='z'
    #
    #     elif x=='e':
    #         del robotMotor
    #         break
    #
    #     else:
    #         print("<<<  wrong data  >>>")
    #         print("please enter the defined data to continue.....")
### -------------------------------------

# def main(win):
