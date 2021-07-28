# Robomaster S1 Led Loop Functions Python Program Example:
# How to visually understand functions in Python, with the
# Robomaster S1

led=led_ctrl
media=media_ctrl
define=rm_define
l1,l2=0,255
delay=.1

def start():

    led.set_flash(define.armor_all,6)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
    
    def single_forward_leds():
        for j in range(2):
            for i in range(1,9):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)

    def single_reverse_leds():
        for j in range(2):
            for i in range(8,0,-1):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)

    def double_forward_leds():
        for j in range(2):
            for i in range(1,5):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)      
                time.sleep(delay)

    def double_reverse_leds():
        for j in range(2):
            for i in range(4,0,-1):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)      
                time.sleep(delay)

    def double_forward_reverse_leds():
        for j in range(2):
            for i in range(1,5):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)
                time.sleep(delay)

            for i in range(3,1,-1):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)
                time.sleep(delay)

    def double_reverse_forward_leds():
        for j in range(2):
            for i in range(4,0,-1):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)
                time.sleep(delay)

            for i in range(2,4):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)
                time.sleep(delay)

    def quad_chasers_forward():
        for j in range(3):
            for i in range(1,3):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+2,i+4,i+6],define.effect_always_on)
                time.sleep(delay)

    def quad_chasers_reverse():
        for j in range(3):
            for i in range(2,0,-1):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+2,i+4,i+6],define.effect_always_on)
                time.sleep(delay)

    def trail_chasers_forward():
        for j in range(2):
            led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)            
            for i in range(1,9):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)
            
            for i in range(1,9):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_off)
                time.sleep(delay)

    def trail_chasers_reverse():
        for j in range(2):
            led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
            for i in range(8,0,-1):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)
            
            for i in range(8,0,-1):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_off)
                time.sleep(delay)

# create a while-loop that continuously calls each led loop function.
# Each led loop function contains a forward and reverse for-loop, which
# create the led looping effects. See what happens when you type and
# execute/run this Python program example.
                
    while True:
        single_forward_leds()
        single_reverse_leds()
        double_forward_leds()
        double_reverse_leds()
        double_forward_reverse_leds()
        double_reverse_forward_leds()
        quad_chasers_forward()
        quad_chasers_reverse()
        trail_chasers_forward()
        trail_chasers_reverse()
