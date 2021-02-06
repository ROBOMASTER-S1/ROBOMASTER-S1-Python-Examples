# Let's make the Robomaster S1 become a cool RGB Pink Dimmer effect with this
# fun Robomaster S1 Python program example. Simply type and execute/run this
# program example below and see what happens.

# Create some strings to shorten some of the long Robomaster S1 Python commands,
# such as those long led commands. Give these strings similar names to the ones
# used for parts of Robomaster S1's Python commands. For example:
'''
robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
blaster=ir_blaster_ctrl
gun=gun_ctrl
led=led_ctrl
armor=armor_ctrl
vision=vision_ctrl
media=media_ctrl
distance=ir_distance_sensor_ctrl
sensor=sensor_adapter_ctrl
define=rm_define

led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)
'''
# This is what unpacking variables looks like in Python. Unpacking variables
# involves just one equal (=) sign, without having to index through a list. Just
# simply call the actual variable you want to use, and it will keep its positional
# index value intact. Sometimes it's a good idea to unpack variables instead,
# rather than creating a list with indexes that might not be useful in some cases.
# For example:

# x1,x2,x3,x4,x5 = 0,255,-1,1,2

# Let's have some fun and unpack these strings into variables instead of the actual
# integer numbers themselves.

# For example: 'x1,x2,x3,x4,x5' are called variables and the actual integer numbers
# '0,255,-1,1,2' are called values, which the variables hold integer numbers, or
# text as well; not shown here.

# Create a while-loop to repeat the two for-loops twice, using the function called
# "rgb_pink_dimmer()".

led=led_ctrl
define=rm_define
x1,x2,x3,x4,x5=0,255,-1,1,2

def start():
    led.turn_off(define.armor_all)
    time.sleep(x4)

    def rgb_pink_dimmer():        
        for i in range(x1,x2):
            led.set_top_led(define.armor_top_all,
            i,x1,i,define.effect_always_on) # Pink

            led.set_bottom_led(define.armor_bottom_all,
            i,x1,i,define.effect_always_on) # Pink

        for i in range(x2,x1,x3):
            led.set_top_led(define.armor_top_all,
            i,x1,i,define.effect_always_on) # Pink

            led.set_bottom_led(define.armor_bottom_all,
            i,x1,i,define.effect_always_on) # Pink
    x=x1
    while x<x5:
        rgb_pink_dimmer()
        x+=x4 # is also x=x+x4 if you like.

    led.turn_off(define.armor_all)
    time.sleep(x4)
