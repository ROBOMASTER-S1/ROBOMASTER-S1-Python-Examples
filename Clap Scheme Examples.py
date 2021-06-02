media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():
    media.enable_sound_recognition(define.sound_detection_applause)

    while True:
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_always_on)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():
    media.enable_sound_recognition(define.sound_detection_applause)
    
    while True:
        if media_ctrl.check_condition(rm_define.cond_sound_recognized_applause_twice):
            led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

        if media_ctrl.check_condition(rm_define.cond_sound_recognized_applause_thrice):
            led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():

    media.enable_sound_recognition(define.sound_detection_applause)
    
    while True:
        pass

def sound_recognized_applause_twice(msg):
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

def sound_recognized_applause_thrice(msg):
    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)
