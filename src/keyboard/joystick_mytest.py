import pygame


def speed_control(speed_gear,speed_sequence): # Speed control

    if speed_sequence:
        speed_gear += 0.3
    else:
        speed_gear -= 0.3

    if speed_gear >= 0.9:
        speed_gear = 0.9
    elif speed_gear <= 0.3:
        speed_gear = 0.3

    print(speed_gear)

    return speed_gear

def main():
    # Frame delay
    clock = pygame.time.Clock()

    # initialisation
    pygame.init()
    joystick = pygame.joystick.Joystick(0)

    joystick.init()

    name = joystick.get_name()
    print(name)

    # -------- Main Program Loop -----------
    done = False

    speed_gear = 0.3

    while not done:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
            # JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")


            # Motor 1 control
            axis_1 = joystick.get_axis(1)
            #print("Axis value : {}".format(axis_1))
            if axis_1 == 0:
                print("M1 Stop. Power : {}".format(axis_1))

            elif axis_1 < 0:
                print("M1 Forward. Power : {}".format(axis_1 * speed_gear * -1))

            elif axis_1 > 0:
                print("M1 Backward. Power : {}".format(axis_1 * speed_gear * -1))

            # Motor 2 control
            axis_4 = joystick.get_axis(4)
            if axis_4 == 0:
                print("M2 Stop. Power : {}".format(axis_4))

            elif axis_4 < 0:
                print("M2 Forward. Power : {}".format(axis_4 * speed_gear * -1))

            elif axis_4 > 0:
                print("M2 Backward. Power : {}".format(axis_4 * speed_gear * -1))

            if joystick.get_button(4):
                speed_gear = speed_control(speed_gear, 1)
                print("Speed UP. Gear: {}.".format(speed_gear))

            if joystick.get_button(5):
                speed_gear = speed_control(speed_gear, 0)
                print("Speed DOWN. Gear: {}.".format(speed_gear))


            if joystick.get_button(8):
                pygame.quit()
                break


        # Limit to 60 frames per second
        clock.tick(30)

    pygame.quit()
    exit()

if __name__ == '__main__':
    main()