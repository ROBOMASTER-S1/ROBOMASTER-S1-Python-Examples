# Now that you've built your very own Robomaster S1 robot.
# It's now time to break the Robomaster S1 robot with this
# really cool hit detector Python program example. All you
# have to do is tap one of Robomaster S1's bottom hit detectors
# to see and hear his special effects.

armor=armor_ctrl
media=media_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255
second,milli_second=1,.1

def start():
    armor.set_hit_sensitivity(10)
    led.turn_off(define.armor_all)
    time.sleep(second)

    while True:
        while True:
            led.set_top_led(define.armor_top_right,l1,l1,l2,define.effect_always_on)
            led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_front,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l1,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l2,l1,l2,define.effect_always_on)
            media.play_sound(define.media_sound_recognize_success,wait_for_complete_flag=True)

            led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_always_on)
            led.set_top_led(define.armor_top_left,l1,l1,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_front,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l2,l1,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l1,l2,l1,define.effect_always_on)
            media.play_sound(define.media_sound_recognize_success,wait_for_complete_flag=True)

            led.set_bottom_led(define.armor_bottom_front,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l1,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l2,l1,l2,define.effect_always_on)

def armor_hit_detection_all(msg):        
    media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
    
    for i in range(2):
        led.gun_led_on()
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)
        time.sleep(milli_second)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l2,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l2,l2,define.effect_always_on)
        time.sleep(milli_second)
        led.gun_led_off()
