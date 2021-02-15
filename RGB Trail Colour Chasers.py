# Let's make the Robomaster S1 do some cool RGB Colour Trail Chasers effects with
# this fun Robomaster S1 Python program example. Simply type and execute/run this
# program example below and see what happens.

# Create some strings to shorten some of the long Robomaster S1 Python commands,
# such as those long led commands. Give these strings similar names to the ones used
# for parts of Robomaster S1's Python commands. For example:
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
# This Robomaster S1 Python program example causes the gimbal leds to
# trail forwards, while they change in all six RGB colour codes every time
# the outer for-loop increments by one whole cycle through after it allows
# the two nested for-loops to loop through their individual cycles through.
# After the nested loops do what they have to do, the outer for-loop, once
# again gets incremented and the whole process starts all over again, until
# the outer for-loop reaches its last increment; its final, proverbial end. 

# The while-loop simply makes this function called 'rgb_colour_trail_chasers()'
# execute/run the whole program twice. You can increase while-loop value to
# any number you like. You can simply make the while-loop run forever, none-stop.
# The while-loop will make the for-loops run forever. Sometimes you need a while-
# loop to make for-loops start at the beginning again, so you can make the for-loop
# indexes repeat themselves, when they terminate. Sometimes you need for-loops
# to start all over again, but without while-loops, that's not always possible to
# achieve. For-loops have only whatever iterations you give them. But, once they
# terminate, they stop running completely. If you try and make the for-loop count
# higher than the iterations you give it, an 'Index Out of Range Error' will occur.

# Run this Robomaster S1 Python program and you will have a much better
# understanding of for-loops and while-loops and how they play a vital role
# in computer programming. For-loops and while-loops also reduce redundant
# code, via the programmer's part.

'''Now it's time to learn, but most important. Have Fun!'''

# Use a multi two dimensional list to loop through all six RGB colours. You need
# to add this empty list box [] at position 0, since the leds on the gimbal and the
# chassis start at 1 through 8 and 1 through 4. Note: no gimbal or chassis leds
# start at 0. If you want the gimbal leds to rotate backwards, simply create a
# reverse for-loop like this illustration shows: 'for i in range(8,0,-1):'. You must
# include the start value, the end value and the step value, -1. Always use negative
# integers in the step value to cause the for-loop to reverse looping. If you don't set
# the step value to a negative integer, the for-loop still runs, but nothing happens.
# Instead the program just does nothing for the duration of the loop iterations.

# Create a while-loop to repeat the outer for-loop and the two nested for-loops two
# times, using the function called "rgb_colour_trail_chasers()".

led=led_ctrl
define=rm_define
delay1,delay2=.1,1
l1,l2=0,255

RGB=[
    [],         # Empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

def start():    
    led.set_flash(define.armor_all,4)
    led.turn_off(define.armor_all)
    time.sleep(delay2)

    def rgb_colour_trail_chasers():
        for i in range(1,7):            
            led.set_top_led(define.armor_top_all,
            RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)

            led.set_bottom_led(define.armor_bottom_all,
            RGB[i][0],RGB[i][1],RGB[i][2],define.effect_flash)

            for i in range(1,9):
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_on)
                time.sleep(delay1)
            
            for i in range(1,9):
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_off)
                time.sleep(delay1)            
    x=0
    while x<2:
        rgb_colour_trail_chasers()
        x+=1 # is also x=x+1 if you like.

    led.turn_off(define.armor_all)
    time.sleep(delay2)
