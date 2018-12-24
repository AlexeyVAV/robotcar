import pygame

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

        #if event.type == pygame.JOYAXISMOTION:
            #print("Joystick Axis Motion.")

        axis_1 = joystick.get_axis(1)
        #print("Axis value : {}".format(axis_1))
        if axis_1 == 0:
            print("M1 Stop. Power : {}".format(axis_1))

        elif axis_1 < 0:
            print("M1 Forward. Power : {}".format(axis_1 * -1))

        elif axis_1 > 0:
            print("M1 Backward. Power : {}".format(axis_1 * -1))


        axis_4 = joystick.get_axis(4)
        if axis_4 == 0:
            print("M2 Stop. Power : {}".format(axis_4))

        elif axis_4 < 0:
            print("M2 Forward. Power : {}".format(axis_4 * -1))

        elif axis_4 > 0:
            print("M2 Backward. Power : {}".format(axis_4 * -1))

    #---------------------------------------------------------------------
    # # Get count of joysticks
    # joystick_count = pygame.joystick.get_count()
    #
    # textPrint.printt(screen, "Number of joysticks: {}".format(joystick_count))
    # textPrint.indent()
    #
    # # For each joystick:
    # for i in range(joystick_count):
    #     joystick = pygame.joystick.Joystick(i)
    #     joystick.init()
    #
    #     textPrint.printt(screen, "Joystick {}".format(i))
    #     textPrint.indent()
    #
    #     # Get the name from the OS for the controller/joystick
    #     name = joystick.get_name()
    #     textPrint.printt(screen, "Joystick name: {}".format(name))
    #
    #     # Usually axis run in pairs, up/down for one, and left/right for
    #     # the other.
    #     axes = joystick.get_numaxes()
    #     textPrint.printt(screen, "Number of axes: {}".format(axes))
    #     #print(axes)
    #     textPrint.indent()
    #
    #     for i in range(axes):
    #         axis = joystick.get_axis(i)
    #         textPrint.printt(screen, "Axis {} value: {:>6.3f}".format(i, axis))
    #         print("{0} : {1}".format(i,axis))
    #     textPrint.unindent()
    #
    #     buttons = joystick.get_numbuttons()
    #     textPrint.printt(screen, "Number of buttons: {}".format(buttons))
    #     textPrint.indent()
    #
    #     for i in range(buttons):
    #         button = joystick.get_button(i)
    #         textPrint.printt(screen, "Button {:>2} value: {}".format(i, button))
    #     textPrint.unindent()
    #
    #     # Hat switch. All or nothing for direction, not like joysticks.
    #     # Value comes back in an array.
    #     hats = joystick.get_numhats()
    #     textPrint.printt(screen, "Number of hats: {}".format(hats))
    #     textPrint.indent()
    #
    #     for i in range(hats):
    #         hat = joystick.get_hat(i)
    #         textPrint.printt(screen, "Hat {} value: {}".format(i, str(hat)))
    #     textPrint.unindent()
    #
    #     textPrint.unindent()
        #-------------------------------------------------------------------------------------

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()