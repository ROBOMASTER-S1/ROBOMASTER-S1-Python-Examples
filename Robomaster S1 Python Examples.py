# ROBOMASTER-S1-Python-Examples

# Learning how to program the Robomaster S1 in Python

# Note: you must install the Robomaster S1 app, either on your wireless mobile device or on your
# computer, via Wi-Fi. Next after installing the Robomaster S1 App, you will have to update the
# firmware for the Robomaster S1. Next you must calibrate the Robomaster S1 so it can work
# properly.

# Note: to be able to program the Robomaster S1 in Scratch or Python, you must run the Robomaster
# S1 app, then connect the Robomaster S1 to it, via wireless mobile device or on your computer,
# via Wi-Fi.

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# LEDS Examples

# For-loop blinking LED's rate example:

def start():
    
    for i in range(10):
        led_ctrl.set_flash(rm_define.armor_all,i+1)
        
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
        
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make the top right and the top left armor LED's chase forward, while changing two, different colours.
# Make the bottom right, left, front and back armor LED's change two, different colours. Type and
# execute/run the program below and see what happens.

def start():
    
    top_led_pos=[1,2,3,4,5,6,7,8]
    a,b,c,d,e,f=[255,0,255,0,255,255]
    
    while True:
        
        for i in top_led_pos:
            led_ctrl.set_top_led(rm_define.armor_top_right,a,b,c,rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_right,[i],rm_define.effect_always_on)
            led_ctrl.set_top_led(rm_define.armor_top_left,d,e,f,rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_left,[i],rm_define.effect_always_on)
            
            led_ctrl.set_bottom_led(rm_define.armor_bottom_right,a,b,c,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_left,d,e,f,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_front,a,b,c,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_back,d,e,f,rm_define.effect_always_on)
            
            time.sleep(.02)
            
        for i in top_led_pos:
            led_ctrl.set_top_led(rm_define.armor_top_right,d,e,f,rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_right,[i],rm_define.effect_always_on)
            led_ctrl.set_top_led(rm_define.armor_top_left,a,b,c,rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_left,[i],rm_define.effect_always_on)
            
            led_ctrl.set_bottom_led(rm_define.armor_bottom_right,d,e,f,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_left,a,b,c,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_front,d,e,f,rm_define.effect_always_on)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_back,a,b,c,rm_define.effect_always_on)
            
            time.sleep(.02)
            
'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Gimbal Examples

# Rotate the gimbal and set the speed to 20, while making the LED's change from yellow to red and
# back to yellow.

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    led_ctrl.set_flash(rm_define.armor_all,2)
    
    gimbal_ctrl.set_rotate_speed(20)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    
    time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Rotate the gimbal and set the speed to 20, while changing all the LED's from red to yellow.

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    gimbal_ctrl.set_rotate_speed(20)
    
    led_ctrl.set_flash(rm_define.armor_all,2)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Rotate gimbal and pitch example:

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    gimbal_ctrl.recenter()
    
    time.sleep(0.5)
    
    led_ctrl.set_flash(rm_define.armor_all, 2)
    
    gimbal_ctrl.set_rotate_speed(30)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.pitch_ctrl(0)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,360)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Chassis Examples

# Turn on the Robomaster's gun light and make the LED's pulsate, while the chassis rocks back and
# forth. Type and execute/run this program example below and see what happens.

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    for i in range(2):
        led_ctrl.gun_led_on()
        
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255,rm_define.effect_breath)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
        
        chassis_ctrl.set_wheel_speed(50,-50,50,-50)
        
        time.sleep(1)
        
        chassis_ctrl.set_wheel_speed(-50,50,-50,50)
        
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make all the LED's flash ten times a second, while making the chassis rock back and forth. Type and
# execute/run the program example below and see what happens.

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    for i in range(2):
        led_ctrl.set_flash(rm_define.armor_all,10)
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
        
        chassis_ctrl.set_wheel_speed(50,-50,50,-50)
        
        time.sleep(1)
        
        chassis_ctrl.set_wheel_speed(-50,50,-50,50)
        
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Turn on the Robomaster's gun light and make the LED's pulsate, while rotating clockwise and anti
# clockwise. Type and execute/run the program example below and see what happens.

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    led_ctrl.gun_led_on()
    
    for i in range(2):
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255,rm_define.effect_breath)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
        
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make the chassis turn a complete 180 degrees, while making the gimbal stay positioned at 0 degrees.
# On each turn, make the LED's change to cyan, then red and back to cyan when the Robomaster makes
# its last, 180 degree turn

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    chassis_ctrl.set_rotate_speed(50)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_always_on)
    
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,360)
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive Chassis Examples

# To avoid damaging your Robomaster S1, never set any speeds higher than they are shown here,
# especially in smaller play areas.

# IMPORTANT! Never pick up or move the Robomaster S1, while its program is running. Doing so
# may cause damage to the unit; you must stop the program first.

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make the Robomaster drive non-stop while making all the LED's flash-rotate two, different colours.
# Type and execute/run the program example below and see what happens.

def start():

    while True:
        chassis_ctrl.set_wheel_speed(20,20,20,20)

        led_ctrl.set_top_led(rm_define.armor_top_right,255,0,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_right,[1,3,5,7],rm_define.effect_always_on)

        led_ctrl.set_top_led(rm_define.armor_top_left,0,255,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_left,[1,3,5,7],rm_define.effect_always_on)

        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,255,rm_define.effect_always_on)

        time.sleep(.095)

        led_ctrl.set_top_led(rm_define.armor_top_right,0,255,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_right,[2,4,6,8],rm_define.effect_always_on)

        led_ctrl.set_top_led(rm_define.armor_top_left,255,0,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_left,[2,4,6,8],rm_define.effect_always_on)

        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)

        time.sleep(.095)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive sideways side to side example 1:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(-20,20,20,-20)

        time.sleep(3)

        chassis_ctrl.set_wheel_speed(20,-20,-20,20)

        time.sleep(3)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive sideways side to side example 2:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_trans_speed(0.2)
        chassis_ctrl.move_with_time(90,3)
        chassis_ctrl.move_with_time(-90,3)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 1:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(20,-20,20,-20)

        time.sleep(4)

        chassis_ctrl.set_wheel_speed(20,20,20,20)

        time.sleep(8)

        chassis_ctrl.set_wheel_speed(-20,20,-20,20)

        time.sleep(4)

        chassis_ctrl.set_wheel_speed(20,20,20,20)

        time.sleep(8)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 2:

def start():

    chassis_ctrl.set_rotate_speed(20)

    while True:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.set_wheel_speed(20,20,20,20)

        time.sleep(4)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        chassis_ctrl.set_wheel_speed(20,20,20,20)

        time.sleep(4)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 3:

def start():

    chassis_ctrl.set_trans_speed(0.3)
    chassis_ctrl.set_rotate_speed(50)

    for i in range(2):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)

        chassis_ctrl.move_with_time(0,4)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)

        chassis_ctrl.move_with_time(0,4)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 4:

# Take your time, don’t rush. Type and execute/run this Robomaster S1 program example below and
# see what happens.

def start():

# Store list variables and values:

    turn_clockwise=[20,-20,20,-20]
    turn_anticlockwise=[-20,20,-20,20]
    drive_straight_speed=[20,20,20,20]
    leds=[0,255];time_delay=[4,8]

# Set gimbal to follow chassis.

    robot_ctrl.set_mode(
        rm_define.robot_mode_gimbal_follow
        )

# Create a never ending while-loop.

    while True:

# Make the top and bottom LED's colour to yellow and flash.

        led_ctrl.set_top_led(
            rm_define.armor_top_all,
            leds[1],leds[1],leds[0],
            rm_define.effect_flash
            )

        led_ctrl.set_bottom_led(
            rm_define.armor_bottom_all,
            leds[1],leds[1],leds[0],
            rm_define.effect_flash
            )

# Make the chassis turn clockwise at speed 20,-20.

        chassis_ctrl.set_wheel_speed(
            turn_clockwise[0],turn_clockwise[1],
            turn_clockwise[2],turn_clockwise[3]
            )

# Set a time.sleep() function with the variable 'time_delay'.

        time.sleep(time_delay[0])

# Make the top and bottom LED's colour to red and breath.

        led_ctrl.set_top_led(
            rm_define.armor_top_all,
            leds[1],leds[0],leds[0],
            rm_define.effect_breath
            )

        led_ctrl.set_bottom_led(
            rm_define.armor_bottom_all,
            leds[1],leds[0],leds[0],
            rm_define.effect_breath
            )

# Make the chassis drive straight ahead at speed 20,-20.

        chassis_ctrl.set_wheel_speed(
            drive_straight_speed[0],drive_straight_speed[1],
            drive_straight_speed[2],drive_straight_speed[3]
            )

# Set a time.sleep() function with the variable 'time_delay'.

        time.sleep(time_delay[1])

# Make the top and bottom LED's colour to yellow and flash.

        led_ctrl.set_top_led(
            rm_define.armor_top_all,
            leds[1],leds[1],leds[0],
            rm_define.effect_flash
            )

        led_ctrl.set_bottom_led(
            rm_define.armor_bottom_all,
            leds[1],leds[1],leds[0],
            rm_define.effect_flash
            )

# Make the chassis turn anticlockwise at speed 20,-20.

        chassis_ctrl.set_wheel_speed(
            turn_anticlockwise[0],turn_anticlockwise[1],
            turn_anticlockwise[2],turn_anticlockwise[3]
            )

# Set a time.sleep() function with the variable 'time_delay'.

        time.sleep(time_delay[0])

# Make the top and bottom LED's colour to red and breath.

        led_ctrl.set_top_led(
            rm_define.armor_top_all,
            leds[1],leds[0],leds[0],
            rm_define.effect_breath
            )

        led_ctrl.set_bottom_led(
            rm_define.armor_bottom_all,
            leds[1],leds[0],leds[0],
            rm_define.effect_breath
            )

# Make the chassis drive straight ahead at speed 20,-20.

        chassis_ctrl.set_wheel_speed(
            drive_straight_speed[0],drive_straight_speed[1],
            drive_straight_speed[2],drive_straight_speed[3]
            )

# Set a time.sleep() function with the variable 'time_delay'.

        time.sleep(time_delay[1])

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle right example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(80,-80,-20,20)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle left example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle left example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(-20,20,80,-80)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle right and left example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)

        time.sleep(10)

        chassis_ctrl.set_wheel_speed(80,-80,-20,20)

        time.sleep(10)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right and left example:

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)

        time.sleep(10)

        chassis_ctrl.set_wheel_speed(-20,20,80,-80)

        time.sleep(10)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Drive the chassis at -45, 45 and 135, -135 degrees. Create a for-loop to repeat the sequence two times.
# Set the chassis translation speed to (0.2) Use a time.sleep(1) delay to allow the chassis to move for
# one second on each degee turn.

# Type and execute/run the program example below and see what happens.

def start():

    chassis_ctrl.set_trans_speed(0.2)

    for i in range(2):
        chassis_ctrl.move(-45)

        time.sleep(1)

        chassis_ctrl.move(45)

        time.sleep(1)

        chassis_ctrl.move(135)

        time.sleep(1)

        chassis_ctrl.move(-135)

        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make Robomaster drive in a square using a for-loop.

drive_speed=(0.2)
wheel_degree=(90,180,-90,0)
seconds=2

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

    for i in wheel_degree:
        chassis_ctrl.set_trans_speed(drive_speed)
        chassis_ctrl.move_with_time(i,seconds)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make Robomaster drive in an X shape using a for-loop.

drive_speed=(0.2)
wheel_degree=(90,-135,90,-45)
seconds=2

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

    for i in wheel_degree:
        chassis_ctrl.set_trans_speed(drive_speed)
        chassis_ctrl.move_with_time(i,seconds)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Blaster Fire Examples

# Rapid-fire blaster gun 8 times example:

def start():
    
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make the blaster fire four times. Type and execute/run the program example below and see what
# happens.

def start():
    
    for count in range(4):
        led_ctrl.gun_led_on()
        
        gun_ctrl.fire_once()
        
        led_ctrl.gun_led_off()

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Blaster fire and rotate 180 degrees example:

def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    gun_ctrl.set_fire_count(2)
    
    gimbal_ctrl.set_rotate_speed(200)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    
    time.sleep(0.5)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make Robomaster fire his blaster every time he sees a person. Set the zoom value update from 1 to
# 4 for farther distances.

def start():

    led1,led2=(0,255)
    blink_rate=(6,8)

# Blaster fire example function:

    def blaster_fire_example():

        robot_ctrl.set_mode(rm_define.robot_mode_free)
        
        while True:
            led_ctrl.set_top_led(rm_define.armor_top_all,led2,led2,led1,rm_define.effect_breath)
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all,led2,led2,1,rm_define.effect_breath)
            
            media_ctrl.zoom_value_update(1)
            vision_ctrl.enable_detection(rm_define.vision_detection_people)
            vision_ctrl.cond_wait(rm_define.cond_recognized_people)
            
            while True:
                randgimbal_speed=random.randint(20,100)
                randup=random.randint(1,55)

                gimbal_ctrl.set_rotate_speed(randgimbal_speed)
                
                media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                led_ctrl.set_flash(rm_define.armor_all,blink_rate[0])
                led_ctrl.set_top_led(rm_define.armor_top_all,led2,led1,led1,rm_define.effect_marquee)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all,led2,led1,led1,rm_define.effect_flash)

                gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,randup)

                led_ctrl.set_flash(rm_define.armor_all,blink_rate[1])
                led_ctrl.set_top_led(rm_define.armor_top_all,led1,led2,led2,rm_define.effect_flash)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all,led1,led2,led2,rm_define.effect_flash)

                media_ctrl.play_sound(rm_define.media_sound_shoot,wait_for_complete_flag=True)
                media_ctrl.play_sound(rm_define.media_sound_shoot,wait_for_complete_flag=True)

                commands_exit=random.randint(1,2)
                
                if commands_exit==1:
                    continue
                elif commands_exit==2:
                    led_ctrl.set_flash(rm_define.armor_all,blink_rate[0])
                    led_ctrl.set_top_led(rm_define.armor_top_all,led2,led1,led1,rm_define.effect_marquee)
                    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,led2,led1,led1,rm_define.effect_flash)
                    
                    gimbal_ctrl.recenter()                        
                    break
                
# Call up the blaster_fire_example function. Be sure to properly indent the function or it won't work.

    blaster_fire_example()
            
'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Red Heart Examples

# Make the Robomaster recognize the red heart and make him wait for it to be recognized before he
# works his bright red LED's and starts blinking them twice. Type and execute/run the program
# example below and see what happens.

def start():

    media_ctrl.zoom_value_update(1)
    
    while True:
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,0,rm_define.effect_always_off)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,0,rm_define.effect_always_off)
        
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        
def vision_recognized_marker_trans_red_heart(msg):
    
    led_ctrl.set_flash(rm_define.armor_all,2)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    
    time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Make the Robomaster recognize the red heart and make him wait for it to be recognized before he
# works his bright cyan LED's and starts to move his chassis forward for one second each time the red
# heart is shown to him. Type and execute/run the program example below and see what happens.

def start():

    media_ctrl.zoom_value_update(1)
    
    while True:
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        
def vision_recognized_marker_trans_red_heart(msg):
    
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    
    chassis_ctrl.set_wheel_speed(20,20,20,20)
    
    time.sleep(1)
    
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_off)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_off)
    
    chassis_ctrl.stop()

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# Red heart aim example:

def start():
    
    while True:
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        
        led_ctrl.set_top_led(rm_define.armor_top_all,255,255,255,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,255,rm_define.effect_always_on)
        
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_always_on)
        
        vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

# More future Robomaster s1 Python examples still to come as I learn more and more, each and every day.

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''
