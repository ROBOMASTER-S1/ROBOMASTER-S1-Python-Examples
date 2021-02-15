# Make the Robomaster S1 become a cool Clap Disco Lamp. Simply clap your hands
# twice every time to change his leds into your favourite Disco leds setting.
# Clap your hands three times to turn his leds off and on, while maintaining
# your desired leds settings. Type and execute/run this program example below
# and see what happens.

led=led_ctrl
media=media_ctrl
define=rm_define
delay1,delay2=.1,1
l1,l2=0,255

RGB=[
    [],         # Empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    ]

def start():
    def rgb_single_colour_chasers_forward():
        while True:
            for i in range(1,9):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break 

    def rgb_single_colour_chasers_reverse():
        while True:            
            for i in range(8,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break

    def rgb_double_colour_chasers_forward():   
        while True:
            for i in range(1,5):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+4],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break 

    def rgb_double_colour_chasers_reverse():   
        while True:
            for i in range(4,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+4],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break

    def rgb_quad_colour_chasers_forward():
        while True:
            for i in range(1,3):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+2,i+4,i+6],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break

    def rgb_quad_colour_chasers_reverse():
        while True:
            for i in range(2,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+2,i+4,i+6],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
                time.sleep(delay1)
            if media.check_condition(define.cond_sound_recognized_applause_twice):
                break

    media.enable_sound_recognition(rm_define.sound_detection_applause)
                
    while True:
        rgb_single_colour_chasers_forward()
        rgb_double_colour_chasers_forward()
        rgb_quad_colour_chasers_forward()
        rgb_quad_colour_chasers_reverse()
        rgb_double_colour_chasers_reverse()
        rgb_single_colour_chasers_reverse()
        
def sound_recognized_applause_thrice(msg):
    led.turn_off(define.armor_all)
    media.cond_wait(define.cond_sound_recognized_applause_thrice)
