# The Robomaster S1 Rocks
# Make the Robomaster S1 rock back and forth.
# See what happens when you type and execute/run
# this Python program example.

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():

    robot.set_mode(define.robot_mode_free)
    
    chassis.set_rotate_speed(120)
    gimbal.set_rotate_speed(120)

    led.set_flash(define.armor_all,4)
    led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_flash)
    led.gun_led_on()

    for i in range(2):
        gimbal.rotate(define.gimbal_right)
        chassis.rotate_with_time(define.anticlockwise, 0.3)
        gimbal.rotate(define.gimbal_left)
        chassis.rotate_with_time(define.clockwise, 0.6)
        gimbal.rotate(define.gimbal_right)
        chassis.rotate_with_time(define.anticlockwise, 0.3)

    led.turn_off(define.armor_all)
    led.gun_led_off();gimbal.stop()
    chassis.stop();gimbal.recenter()
