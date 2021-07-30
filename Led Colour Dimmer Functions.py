# Robomaster S1 Led Colour Dimmer Functions Python Program Example:
# How to visually understand functions in Python, with the Robomaster S1.

led=led_ctrl
define=rm_define
l1,l2=0,255
x=-1

def start():
    led.turn_off(define.armor_all)

    def rgb_red_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,i,l1,l1,define.effect_always_on) # Red
            led.set_bottom_led(define.armor_bottom_all,i,l1,l1,define.effect_always_on) # Red

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,i,l1,l1,define.effect_always_on) # Red
            led.set_bottom_led(define.armor_bottom_all,i,l1,l1,define.effect_always_on) # Red

    def rgb_yellow_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,i,i,l1,define.effect_always_on) # Yellow
            led.set_bottom_led(define.armor_bottom_all,i,i,l1,define.effect_always_on) # Yellow

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,i,i,l1,define.effect_always_on) # Yellow
            led.set_bottom_led(define.armor_bottom_all,i,i,l1,define.effect_always_on) # Yellow

    def rgb_blue_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,l1,l1,i,define.effect_always_on) # Blue
            led.set_bottom_led(define.armor_bottom_all,l1,l1,i,define.effect_always_on) # Blue

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,l1,l1,i,define.effect_always_on) # Blue
            led.set_bottom_led(define.armor_bottom_all,l1,l1,i,define.effect_always_on) # Blue

    def rgb_green_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,l1,i,l1,define.effect_always_on) # Green
            led.set_bottom_led(define.armor_bottom_all,l1,i,l1,define.effect_always_on) # Green

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,l1,i,l1,define.effect_always_on) # Green
            led.set_bottom_led(define.armor_bottom_all,l1,i,l1,define.effect_always_on) # Green

    def rgb_pink_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,i,l1,i,define.effect_always_on) # Pink
            led.set_bottom_led(define.armor_bottom_all,i,l1,i,define.effect_always_on) # Pink

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,i,l1,i,define.effect_always_on) # Pink
            led.set_bottom_led(define.armor_bottom_all,i,l1,i,define.effect_always_on) # Pink

    def rgb_cyan_dimmer():        
        for i in range(l1,l2):
            led.set_top_led(define.armor_top_all,l1,i,i,define.effect_always_on) # Cyan
            led.set_bottom_led(define.armor_bottom_all,l1,i,i,define.effect_always_on) # Cyan

        for i in range(l2,l1,x):
            led.set_top_led(define.armor_top_all,l1,i,i,define.effect_always_on) # Cyan
            led.set_bottom_led(define.armor_bottom_all,l1,i,i,define.effect_always_on) # Cyan

# create a while-loop that continuously calls each colour dimmer function.
# Each colour dimmer function contains a forward and reverse for-loop, which
# create the colour dimming effects. See what happens when you type and
# execute/run this Python program example.

    while True:
        rgb_red_dimmer()
        rgb_yellow_dimmer()
        rgb_blue_dimmer()
        rgb_green_dimmer()
        rgb_pink_dimmer()
        rgb_cyan_dimmer()
