# ROBOMASTER-S1-Python-Examples

# Learning how to program the Robomaster S1 in Python

# Note: you must install the Robomaster S1 app, either on your wireless mobile device or on your computer, via Wi-Fi.
# Next after installing the Robomaster S1 App, you will have to update the firmware for the Robomaster S1.
# Next you must calibrate the Robomaster S1 so it can work properly.

# Note: to be able to program the Robomaster S1 in Scratch or Python, you must run the Robomaster S1 app, then connect
# the Robomaster S1 to it, via wireless mobile device or on your computer, via Wi-Fi.
'''----------------------------------------------------------------------------------------------------------------'''
# Make the Robomaster drive non-stop while making all the LEDS flash-rotate two, different colours.
# Type and execute/run this program example below and see what happens.

while True:
    chassis_ctrl.set_wheel_speed(50,50,50,50)
    led_ctrl.set_top_led(rm_define.armor_top_right,255,0,255,rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right,[1,3,5,7],rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_left,0,255,255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_left,[1,3,5,7],rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,255,rm_define.effect_always_on)
    time.sleep(.095)
    led_ctrl.set_top_led(rm_define.armor_top_right,0,255,255,rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right,[2,4,6,8],rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_left,255,0,255,rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_left,[2,4,6,8],rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    time.sleep(.095)
    
# Make all the LEDs flash ten times a second, while making the chassis rocks back and forth.
# Type and execute/run the program example below and see what happens.

for i in range(2):
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    led_ctrl.set_flash(rm_define.armor_all,10)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    chassis_ctrl.set_wheel_speed(50,-50,50,-50)
    time.sleep(1)
    chassis_ctrl.set_wheel_speed(-50,50,-50,50)
    time.sleep(1)
    
# Turn on the Robomaster's gun light and make the LEDs pulsate, while the chassis rocks back and forth.
# Type and execute/run this program example below and see what happens.
    
for i in range(2):
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    led_ctrl.gun_led_on()
    led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255, rm_define.effect_breath)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
    chassis_ctrl.set_wheel_speed(50,-50,50,-50)
    time.sleep(1)
    chassis_ctrl.set_wheel_speed(-50,50,-50,50)
    time.sleep(1)    

# Turn on the Robomaster's gun light and make the LEDS pulsate, while rotating clockwise and anti
# clockwise. Type and execute/run the program example below and see what happens.

for i in range(2):
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    led_ctrl.gun_led_on()
    led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255,rm_define.effect_breath)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    
# Make the Robomaster recognize the red heart and make him wait for it to be recognized
# before he works his bright cyan lights and starts to move his chassis forward for one
# second each time the red heart is shown to him. Type and execute/run the program example
# below and see what happens.
    
def start():
    while True:
        media_ctrl.zoom_value_update(1)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)        
def vision_recognized_marker_trans_red_heart(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(50,50,50,50)
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_off)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255, rm_define.effect_always_off)
    chassis_ctrl.stop()   

# More future Robomaster s1 Python examples still to come.
