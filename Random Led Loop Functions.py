# Robomaster S1 Random Led Loop Functions Python Program Example:
# How to visually understand functions in Python, with the Robomaster S1.

led=led_ctrl
media=media_ctrl
define=rm_define
l1,l2=0,255
delay=.1
x=-1

def start():

    led.set_flash(define.armor_all,6)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)

    def single_forward_reverse_leds():
        for j in range(2):
            randcount=random.randint(1,9)
            for i in range(1,randcount):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)

            for i in range(randcount+x,0,x):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)

    def double_forward_reverse_leds():
        for j in range(3):
            randcount=random.randint(1,5)
            for i in range(1,randcount):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)      
                time.sleep(delay)

            for i in range(randcount+x,0,x):
                led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)
                led.set_single_led(define.armor_top_all,[i,i+4],define.effect_always_on)      
                time.sleep(delay)
    
    def trail_chasers_forward_reverse_leds():
        for j in range(2):
            randcount=random.randint(1,9)
            led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_off)

            for i in range(1,randcount):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)
            
            for i in range(1,randcount):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_off)
                time.sleep(delay)

            for i in range(randcount+x,0,x):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_on)
                time.sleep(delay)
            
            for i in range(randcount+x,0,x):
                led.set_single_led(define.armor_top_all,[i],define.effect_always_off)
                time.sleep(delay)

# create a while-loop that continuously calls each random led loop function.
# Each random led loop function contains a forward and reverse for-loop, which
# create the random led looping effects. See what happens when you type and
# execute/run this Python program example.

    while True:
        single_forward_reverse_leds()
        double_forward_reverse_leds()
        trail_chasers_forward_reverse_leds()
