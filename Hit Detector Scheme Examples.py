# Hit Detector Scheme Examples:

# Hit Detectors Wait Example:

media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():
    armor.set_hit_sensitivity(10)

    while True:
        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_right_hit)
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_left_hit)
        led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)

        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_front_hit)
        led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)

        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)
        led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_always_on)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Hit Detectors Wait If Example:

media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():
    armor.set_hit_sensitivity(10)
    armor.cond_wait(define.cond_armor_hit)

    while True:        
        if armor.check_condition(define.cond_armor_bottom_right_hit):
            led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

        if armor.check_condition(define.cond_armor_bottom_left_hit):
            led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)            

        if armor.check_condition(define.cond_armor_bottom_front_hit):
            led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)

        if armor.check_condition(define.cond_armor_bottom_back_hit):
            led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_always_on)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Hit Detector Functions Example:

media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():
    armor.set_hit_sensitivity(10)

    while True:
        armor.cond_wait(define.cond_armor_hit)
    
def armor_hit_detection_bottom_right(msg):
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

def armor_hit_detection_bottom_left(msg):
    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)

def armor_hit_detection_bottom_front(msg):
    led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)

def armor_hit_detection_bottom_back(msg):
    led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_always_on)
