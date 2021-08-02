# Robomaster S1 Light Showoff Python program example:

# You can create wonderful looping led effects with Python
# list arrays and for-loops to change the colours and the
# spinning led effects. You must set the list array starting
# with an empty list box since the Robomaster S1's leds start
# at 1 through 8, not 0 through 8. Type and execute/run this
# Python program example and see what happens.

robot=robot_ctrl
led=led_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
define=rm_define

rotate_speed=120
l1,l2=0,255
seconds,milli_seconds=1,.05

RGB1=[
    [],         # Empty list box
    [l2,l2,l2], # RGB White
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

RGB2=[
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

    robot.set_mode(define.robot_mode_gimbal_follow)
    
    chassis.set_rotate_speed(rotate_speed)
    led.set_flash(define.armor_all,4)
    chassis.rotate(define.clockwise)

    for j in range(1,8):
        led.gun_led_on()
        led.set_top_led(define.armor_top_all,
        RGB1[j][0],RGB1[j][1],RGB1[j][2],define.effect_always_off)

        led.set_bottom_led(define.armor_bottom_all,
        RGB1[j][0],RGB1[j][1],RGB1[j][2],define.effect_flash)

        for i in range(1,9):
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)
            time.sleep(milli_seconds)

        for i in range(1,9):
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_off)
            time.sleep(milli_seconds)
            led.gun_led_off()

    for j in range(0,2):
        led.gun_led_on()
        for i in range(1,9):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    for j in range(0,3):
        led.gun_led_on()
        for i in range(1,5):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i,i+4],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    for j in range(0,7):
        led.gun_led_on()
        for i in range(1,3):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i,i+2,i+4,i+6],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    chassis.stop()

    for j in range(2):
        led_ctrl.gun_led_on()
        for i in range(1,5):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
            time.sleep(milli_seconds)

        led_ctrl.gun_led_off()
        for i in range(3,1,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            
    chassis.rotate(define.anticlockwise)

    for j in range(0,7):
        led.gun_led_on()
        for i in range(2,0,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i,i+2,i+4,i+6],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    for j in range(0,3):
        led.gun_led_on()
        for i in range(4,0,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i,i+4],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    for j in range(0,2):
        led.gun_led_on()
        for i in range(8,0,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(milli_seconds)
            led.gun_led_off()

    led.set_flash(define.armor_all,4)

    for j in range(1,8):
        led.gun_led_on()
        led.set_top_led(define.armor_top_all,
        RGB1[j][0],RGB1[j][1],RGB1[j][2],define.effect_always_off)

        led.set_bottom_led(define.armor_bottom_all,
        RGB1[j][0],RGB1[j][1],RGB1[j][2],define.effect_flash)

        for i in range(8,0,-1):
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)
            time.sleep(milli_seconds)

        for i in range(8,0,-1):
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_off)
            time.sleep(milli_seconds)
            led.gun_led_off()

    time.sleep(.08)
    chassis.stop()

    led.set_flash(define.armor_all,6)
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
    gimbal_ctrl.rotate(rm_define.gimbal_up)
    media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
    time.sleep(seconds+.5)

    led.set_flash(define.armor_all,8)
    led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)

    led.gun_led_on()
    media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
    media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
    led.turn_off(define.armor_all)
    led.gun_led_off()

    led.set_flash(define.armor_all,6)
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
    gimbal_ctrl.rotate(rm_define.gimbal_down)
    media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

    chassis.stop();gimbal.recenter()
