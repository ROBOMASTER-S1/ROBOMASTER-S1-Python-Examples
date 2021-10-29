# Make the Robomaster S1 Count his leds from one to five
# using his vision markers. See what happens when you type
# and Execute/run this Python program example:

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
vision=vision_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

led_set_single=led.set_single_led

led_set_top_bottom=(
    led_ctrl.set_top_led,
    led_ctrl.set_bottom_led)

gun_led_on_off=(
    led_ctrl.gun_led_off,
    led.gun_led_on)

define_armor_all=(rm_define.armor_all)

define_armor_top_bottom_all=(
    rm_define.armor_top_all,
    rm_define.armor_bottom_all)

define_armor_top_right_left=(
    rm_define.armor_top_right,
    rm_define.armor_top_left)

define_armor_bottom_right_left=(
    rm_define.armor_bottom_right,
    rm_define.armor_bottom_left)

define_armor_bottom_front_back=(
    rm_define.armor_bottom_front,
    rm_define.armor_bottom_back)

define_effect=(
    rm_define.effect_always_off,
    rm_define.effect_always_on,
    rm_define.effect_flash,
    rm_define.effect_breath,
    rm_define.effect_marquee)

l1,l2,x,y=0,255,1,-1
delay1,delay2,seconds=.1,.2,1

RGB_COLOURS=[
    [],         # empty list box
    [l2,l2,l2], # RGB White
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

RGB_RY=[
    [],         # empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    ]

RGB_YR=[
    [],         # empty list box
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l2,l1,l1], # RGB Red
    ]

RGB_BG=[
    [],         # empty list box
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    ]

RGB_GB=[
    [],         # empty list box
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l1,l1,l2], # RGB Blue
    ]

RGB_PC=[
    [],         # empty list box
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

RGB_CP=[
    [],         # empty list box
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    [l2,l1,l2], # RGB Pink
    ]

RGB_RYBG=[
    [],         # empty list box
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    ]

vision.enable_detection(define.vision_detection_marker)
vision.set_marker_detection_distance(1)

def start():
    def leds_count():
        while True:
            led.turn_off(define.armor_all)
            if vision.check_condition(define.cond_recognized_marker_number_one):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[0])

                for j in range(x,2):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[1])
                    media.play_sound(define.media_sound_recognize_success,
                    wait_for_complete_flag=False);time.sleep(seconds)

                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l2,define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],[1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l2,define_effect[2])
                media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
                gun_led_on_off[x]();time.sleep(2);gun_led_on_off[l1]()

            elif vision.check_condition(define.cond_recognized_marker_number_two):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[0])

                for j in range(x,3):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[1])
                    media.play_sound(define.media_sound_recognize_success,
                    wait_for_complete_flag=False);time.sleep(seconds)

                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l2,define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],[1,2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l2,define_effect[2])
                media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
                gun_led_on_off[x]();time.sleep(2);gun_led_on_off[l1]()

            elif vision.check_condition(define.cond_recognized_marker_number_three):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[0])

                for j in range(x,4):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[1])
                    media.play_sound(define.media_sound_recognize_success,
                    wait_for_complete_flag=False);time.sleep(seconds)

                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l2,define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],[1,2,3],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l2,define_effect[2])
                media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
                gun_led_on_off[x]();time.sleep(2);gun_led_on_off[l1]()
            
            elif vision.check_condition(define.cond_recognized_marker_number_four):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[0])

                for j in range(x,5):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[1])
                    media.play_sound(define.media_sound_recognize_success,
                    wait_for_complete_flag=False);time.sleep(seconds)

                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l2,define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l2,define_effect[2])
                media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
                gun_led_on_off[x]();time.sleep(2);gun_led_on_off[l1]()

            elif vision.check_condition(define.cond_recognized_marker_number_five):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[0])

                for j in range(x,6):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[1])
                    media.play_sound(define.media_sound_recognize_success,
                    wait_for_complete_flag=False);time.sleep(seconds)

                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l2,define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],[1,2,3,4,5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l2,define_effect[2])
                media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False)
                gun_led_on_off[x]();time.sleep(2);gun_led_on_off[l1]()
                
    leds_count()
