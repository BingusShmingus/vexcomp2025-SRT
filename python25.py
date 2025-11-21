screen_precision = 0
console_precision = 0
controller_1_precision = 0
myVariable = 0
ServButt = Event()

def when_started1():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    while True:
        brain.screen.set_cursor(1, 1)
        brain.screen.print(brain.battery.capacity(), precision=screen_precision)
        brain.screen.set_cursor(3, 1)
        brain.screen.print("VEXcode")
        brain.screen.clear_row(1)
        brain.screen.set_cursor(brain.screen.row(), 1)
        brain.screen.clear_row(3)
        brain.screen.set_cursor(brain.screen.row(), 1)
        wait(5, SECONDS)
        wait(5, MSEC)

def controller_1buttonRight_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    servo_a.set_position(70 - 50.0, DEGREES)
    print("SER180N", end="")
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("SER180NL")
    ServButt.broadcast()
    print("SER180P", end="")
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("SER180PR")
    ServButt.broadcast()

def controller_1buttonA_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    servo_b.set_position(90 - 50.0, DEGREES)

def controller_1buttonA_released_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    servo_b.set_position(-230 - 50.0, DEGREES)

def controller_1buttonR1_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    mc55_4.spin(FORWARD, 6, VOLT)

def controller_1buttonR1_released_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    mc55_4.stop()

def controller_1buttonR2_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    mc55_4.spin(REVERSE, 6, VOLT)

def controller_1buttonR2_released_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    mc55_4.stop()

def controller_1buttonL1_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.spin(FORWARD, 4, VOLT)

def controller_1buttonL1_pressed_callback_1():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.spin(FORWARD, 4, VOLT)

def controller_1buttonL1_released_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.set_stopping(BRAKE)
    MC55_arm.stop()

def controller_1buttonL1_released_callback_1():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.set_stopping(BRAKE)
    MC55_arm.stop()

def when_started2():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    controller_1.screen.clear_screen()
    while True:
        controller_1.screen.set_cursor(2, 1)
        controller_1.screen.print("Batt.")
        controller_1.screen.set_cursor(4, 1)
        controller_1.screen.print(brain.battery.capacity(), precision=controller_1_precision)
        wait(0.5, SECONDS)
        controller_1.screen.set_cursor(2, 14)
        controller_1.screen.print("Drv. W")
        controller_1.screen.clear_row(4)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        controller_1.screen.set_cursor(4, 16)
        controller_1.screen.print(drivetrain.power(), precision=controller_1_precision)
        wait(0.5, SECONDS)
        controller_1.screen.clear_row(4)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        controller_1.screen.set_cursor(2, 16)
        controller_1.screen.set_cursor(4, 10)
        wait(0.5, SECONDS)
        controller_1.screen.clear_row(4)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        wait(5, MSEC)

def controller_1buttonL2_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.spin(REVERSE, 1.5, VOLT)

def controller_1buttonL2_released_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    MC55_arm.set_stopping(BRAKE)
    MC55_arm.stop()

def when_started3():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    while True:
        if brain.battery.capacity() < 20:
            for repeat_count in range(30):
                controller_1.screen.set_cursor(1, 10)
                controller_1.screen.print("BATT LOW")
                controller_1.screen.next_row()
                controller_1.rumble("....")
                wait(30, SECONDS)
                controller_1.screen.clear_row(1)
                controller_1.screen.set_cursor(controller_1.screen.row(), 1)
                wait(5, MSEC)
        wait(5, MSEC)

def ServButt_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    pass

def ServButt_callback_1():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    wait(2, SECONDS)
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)

def controller_1buttonLeft_pressed_callback_0():
    global myVariable, my_event, ServButt, ax3, ax2, screen_precision, console_precision, controller_1_precision
    servo_a.set_position(-180 - 50.0, DEGREES)
    print("SER180N", end="")
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("SER180NR")
    ServButt.broadcast()

# system event handlers
controller_1.buttonRight.pressed(controller_1buttonRight_pressed_callback_0)
controller_1.buttonA.pressed(controller_1buttonA_pressed_callback_0)
controller_1.buttonA.released(controller_1buttonA_released_callback_0)
controller_1.buttonR1.pressed(controller_1buttonR1_pressed_callback_0)
controller_1.buttonR1.released(controller_1buttonR1_released_callback_0)
controller_1.buttonR2.pressed(controller_1buttonR2_pressed_callback_0)
controller_1.buttonR2.released(controller_1buttonR2_released_callback_0)
controller_1.buttonL1.pressed(controller_1buttonL1_pressed_callback_0)
controller_1.buttonL1.pressed(controller_1buttonL1_pressed_callback_1)
controller_1.buttonL1.released(controller_1buttonL1_released_callback_0)
controller_1.buttonL1.released(controller_1buttonL1_released_callback_1)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_0)
controller_1.buttonL2.released(controller_1buttonL2_released_callback_0)
ServButt(ServButt_callback_0)
ServButt(ServButt_callback_1)
controller_1.buttonLeft.pressed(controller_1buttonLeft_pressed_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
when_started1()
