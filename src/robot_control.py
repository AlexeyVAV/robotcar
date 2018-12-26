import pygame
from motors/xy160d_motor_v6 import Motor


def speed_control(speed_gear,speed_sequence): # Speed control

    if speed_sequence:
        speed_gear += 0.3
    else:
        speed_gear -= 0.3

    if speed_gear >= 0.9:
        speed_gear = 0.9
    elif speed_gear <= 0.3:
        speed_gear = 0.3

    return speed_gear


def main():

    # -------------- Motor initialisation --------------
    # correct pin settings on 24.12.2018 for XY-160D
    in1 = 27
    in2 = 22
    en1 = 16
    in3 = 17
    in4 = 4
    en2 = 19

    robot_motor = Motor(m1_in1=in1, m1_in2=in2, m1_en=en1, m2_in1=in3, m2_in2=in4, m2_en=en2)

    # -------------- Joystick initialisation --------------
    # Frame delay
    clock = pygame.time.Clock()

    # initialisation
    pygame.init()
    joystick = pygame.joystick.Joystick(0)

    joystick.init()

    name = joystick.get_name()
    print(name)

    # -------- General settings -----------
    done = False

    speed_gear = 0.3

    # -------- Main Program Loop -----------
    while not done:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # joystick test code
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
            # JOYBUTTONUP JOYHATMOTION
            # if event.type == pygame.JOYBUTTONDOWN:
            #     print("Joystick button pressed.")
            # if event.type == pygame.JOYBUTTONUP:
            #     print("Joystick button released.")


            # Motor 1 control
            axis_1 = joystick.get_axis(1)
            #print("Axis value : {}".format(axis_1))

            if axis_1 == 0:

                print("M1 Stop. Power : {}".format(axis_1))
                robot_motor.stop_m1(pwm1 = (axis_1 * speed_gear))

            elif axis_1 < 0:

                print("M1 Forward. Power : {}".format(axis_1 * speed_gear * -1))
                robot_motor.forward_m1(pwm1 = (axis_1 * speed_gear * -1))

            elif axis_1 > 0:

                print("M1 Backward. Power : {}".format(axis_1 * speed_gear * -1))
                robot_motor.backward_m1(pwm1 = (axis_1 * speed_gear))


            # Motor 2 control
            axis_4 = joystick.get_axis(4)

            if axis_4 == 0:

                print("M2 Stop. Power : {}".format(axis_4))
                robot_motor.stop_m1(pwm2 = (axis_4 * speed_gear))

            elif axis_4 < 0:

                print("M2 Forward. Power : {}".format(axis_4 * speed_gear * -1))
                robot_motor.forward_m2(pwm2 = (axis_4 * speed_gear * -1))

            elif axis_4 > 0:

                print("M2 Backward. Power : {}".format(axis_4 * speed_gear * -1))
                robot_motor.backward_m2(pwm2=(axis_4 * speed_gear))


            if joystick.get_button(4):

                speed_gear = speed_control(speed_gear, 1)
                print("Speed UP. Gear: {}.".format(speed_gear))


            if joystick.get_button(5):

                speed_gear = speed_control(speed_gear, 0)
                print("Speed DOWN. Gear: {}.".format(speed_gear))


            if joystick.get_button(8):

                pygame.quit()
                break

        # Limit to 30 frames per second
        clock.tick(30)

    pygame.quit()
    exit()

# Main code
if __name__ == '__main__':
    main()