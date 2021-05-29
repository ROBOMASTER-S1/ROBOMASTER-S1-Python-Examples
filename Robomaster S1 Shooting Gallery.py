# Make Robomaster S1 sharpen his shooting gallery skills with
# this fun, easy to understand Python program example. Simply
# line up his vision markers from one through five, including
# aiming at the red heart vision marker. Create a simple scenario
# where the Robomaster S1 searches for the correct vision makers
# given. Make sure to place the red heart vision marker in between
# the other vision markers, directly in front of the robomaster S1
# robot. Note: place the robot about one metre away from the vision
# makers to achieve accurate vision marker detection from the robot.

# Tip: Create some string variables to shorten most of the Robomaster
# S1 Python commands. Choose names that resemble the actual
# Robomaster S1's leading commands such as robot = robot_ctrl and
# gimbal = gimbal_ctrl. Also create two packed variables for the RGB
# lights such as 'l1,l2 = 0,255' to make it easier to choose the desired
# RGB led colour combinations you want the robot to use throughout
# your program execution/run.

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
vision=vision_ctrl
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():

    robot.set_mode(define.robot_mode_chassis_follow)
    vision.enable_detection(define.vision_detection_marker)
    vision.set_marker_detection_distance(3)

    x=0
    
    while x<2:
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

        vision.detect_marker_and_aim(define.marker_number_one)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
        
        vision.detect_marker_and_aim(define.marker_number_two)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

        vision.detect_marker_and_aim(define.marker_number_three)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

        vision.detect_marker_and_aim(define.marker_number_four)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

        vision.detect_marker_and_aim(define.marker_number_five)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

        vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)

        led.set_flash(define.armor_all,8)
        led.set_top_led(define.armor_top_all,l2,l1,l2,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l2,define.effect_flash)
        led.gun_led_on()

        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
        led.gun_led_off()
        gimbal.recenter()
    
        x=x+1 # or instead use 'x+=1'
