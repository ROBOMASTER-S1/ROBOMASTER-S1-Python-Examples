'''Robomaster S1 Comes to Life 4.0'''

# Make Robomaster S1 come to life. Simply copy or download this program example.

# You must copy and paste the program code into your Robomaster app. After that,
# simply click the blue play button, then clap your hands three times to wake him
# up. To make him sleep, simply tap any one of his bottom hit detectors.

# This Robomaster S1 program example uses three powerful random generator
# functions. The random.randint(), the random.choice() and the random.choices()
# functions. These three random generator functions are what make the Robomaster
# S1 come to life and appear to have a mind of its own.

# To avoid damaging your Robomaster S1, never set any speeds higher than they
# are shown here, especially in smaller play areas. Note: be cautious when setting
# the drive_speed variable higher than 0.3 and the seconds variable, who's default
# is 2 seconds per drive time distance.

# IMPORTANT! Never pick up or move the Robomaster S1, while its program is
# running. Doing so may cause damage to the unit; you must stop the program first.

# Robomaster S1 feature functions illustrated here are as follows:

# Robomster S1 Start Function
# Robot All Wheel Omn directional Drive Function
# Gimbal Free Mode Right Left Function
# Chassis Follow Gimbal Right Left Function
# Dance Rock Function
# Blaster Fire Function with sound effect
# Scan Search Right Left Function with sound effect
# Sleep Function
# Single Led Chassis Follow Gimbal Rotation Right Left Function
# Double Led Chassis Follow Gimbal Rotation Right Left Function
# Quad Led Gimbal Rotation Up Down Function with sound effect
# RGB Colour Trail Chasers Forward Reverse Function
# RGB Colour Changers Forward Reverse Function
# RGB Flash Colour Changers Function
# RGB Colour Flasher Functions
# RGB Colour Dimmer Functions

# User Interaction Features:

# Detection Applause
# Hit Detection

# Please note: new and improved features and updates will always
# continue to grow as I learn more, each and every day.

# I sure hope other Robomaster S1 people find this program very
# enjoyable and useful. I sure put a lot of time into creating it.
# It sure wasn't no cakewalk when the gimbal and chassis would conflict
# each other during practice execution/runs before I finally figured it
# all out. So please enjoy...

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

led_set_flash=(led_ctrl.set_flash)

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

media_enable_disable=(
    media_ctrl.disable_sound_recognition,
    media_ctrl.enable_sound_recognition)

media_wait=(media_ctrl.cond_wait)

media_play_sound=(media_ctrl.play_sound)

define_detection_applause=(
    rm_define.sound_detection_applause)

define_sound_recognized_twice_thrice=(
    rm_define.cond_sound_recognized_applause_twice,
    rm_define.cond_sound_recognized_applause_thrice)

armor_set_sensitivity=(armor_ctrl.set_hit_sensitivity)

wheel_degree=0,180,90,-90,45,-45,135,-135
l1,l2=0,255;blink_rate=2,3,4,5,6,8
scan_speed=50;drive_speed=.35
rotate_speed=20,30,40,50,60,80
seconds,milli_seconds=2,.1
delay1,delay2=1,.1
a,b,c=1,2,3

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

RGB1=[
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

RGB2=[
    [],         # empty list box
    [l2,l2,l2], # RGB White
    [l2,l1,l1], # RGB Red
    [l2,l2,l1], # RGB Yellow
    [l1,l1,l2], # RGB Blue
    [l1,l2,l1], # RGB Green
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

def start():
    media_enable_disable[1](define_detection_applause)
    armor_set_sensitivity(10)

# Robomster S1 Start Function:

    def robomaster_s1_start():
        gun_led_on_off[0]()
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],l2,l1,l1,define_effect[3])
        gimbal.recenter()

        media_wait(define_sound_recognized_twice_thrice[1])

        led_set_flash(define_armor_all,1)
        led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[4])
        led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[2])
        media_play_sound(define.media_sound_count_down,wait_for_complete_flag=True)

# Robot All Wheel Omni Directional Drive Function:

    def robot_all_wheel_omni_directional_drive():
        robot.set_mode(define.robot_mode_chassis_follow)
        def robot_all_wheel_omni_directional_drive_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=180:
                    led_set_top_bottom[0](define_armor_top_right_left[1],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define_armor_top_right_left[0],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l2,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l2,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l2,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l1,l1,define_effect[1])

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    if randwheel==0:chassis.move_with_time(wheel_degree[1],seconds)
                    elif randwheel==180:chassis.move_with_time(wheel_degree[0],seconds)
                    elif randwheel==90:chassis.move_with_time(wheel_degree[3],seconds)
                    elif randwheel==-90:chassis.move_with_time(wheel_degree[2],seconds)
                    elif randwheel==45:chassis.move_with_time(wheel_degree[7],seconds)
                    elif randwheel==-45:chassis.move_with_time(wheel_degree[6],seconds)
                    elif randwheel==135:chassis.move_with_time(wheel_degree[5],seconds)
                    elif randwheel==-135:chassis.move_with_time(wheel_degree[4],seconds)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        robot_all_wheel_omni_directional_drive_right()

        def robot_all_wheel_omni_directional_drive_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=180:
                    led_set_top_bottom[0](define_armor_top_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define_armor_top_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    led.set_top_led(define_armor_top_bottom_all[0],l2,l2,l1,define_effect[1])
                    led.set_bottom_led(define_armor_bottom_right_left[1],l2,l2,l1,define_effect[1])
                    led.set_bottom_led(define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led.set_bottom_led(define_armor_bottom_right_left[0],l2,l2,l1,define_effect[1])
                    led.set_bottom_led(define_armor_bottom_front_back[1],l2,l1,l1,define_effect[1])

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    if randwheel==0:chassis.move_with_time(wheel_degree[1],seconds)
                    elif randwheel==180:chassis.move_with_time(wheel_degree[0],seconds)
                    elif randwheel==90:chassis.move_with_time(wheel_degree[3],seconds)
                    elif randwheel==-90:chassis.move_with_time(wheel_degree[2],seconds)
                    elif randwheel==45:chassis.move_with_time(wheel_degree[7],seconds)
                    elif randwheel==-45:chassis.move_with_time(wheel_degree[6],seconds)
                    elif randwheel==135:chassis.move_with_time(wheel_degree[5],seconds)
                    elif randwheel==-135:chassis.move_with_time(wheel_degree[4],seconds)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        robot_all_wheel_omni_directional_drive_left()

# Gimbal Free Mode Right Left Function:

    def gimbal_free_mode_right_left():
        robot.set_mode(define.robot_mode_free)
        def gimbal_free_mode_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=90:
                    led_set_top_bottom[0](define_armor_top_right_left[1],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define_armor_top_right_left[0],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        gimbal_free_mode_right()

        def gimbal_free_mode_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=90:
                    led_set_top_bottom[0](define_armor_top_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define_armor_top_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        gimbal_free_mode_left()

# Chassis Follow Gimbal Right Left Function:

    def chassis_follow_gimbal_right_left():
        robot.set_mode(define.robot_mode_chassis_follow)
        def chassis_follow_gimbal_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=90:
                    led_set_top_bottom[0](define.armor_top_left,l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define.armor_top_right,l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define.armor_bottom_left,l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define.armor_bottom_front,l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define.armor_bottom_right,l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define.armor_bottom_back,l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        chassis_follow_gimbal_right()

        def chassis_follow_gimbal_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led_set_flash(define_armor_all,blink_rate[0])
                elif randspeed==30:led_set_flash(define_armor_all,blink_rate[1])
                elif randspeed==40:led_set_flash(define_armor_all,blink_rate[2])
                elif randspeed==50:led_set_flash(define_armor_all,blink_rate[3])
                elif randspeed==60:led_set_flash(define_armor_all,blink_rate[4])
                elif randspeed==80:led_set_flash(define_armor_all,blink_rate[5])

                if randrotate<=90:
                    led_set_top_bottom[0](define_armor_top_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[0](define_armor_top_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l1,l1,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[1])
                    led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l2,l1,define_effect[2])
                    led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l2,l1,define_effect[2])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        chassis_follow_gimbal_left()

# Dance Rock Function:

    def dance_rock():
        robot.set_mode(define.robot_mode_chassis_follow)
        led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l2,l1,define_effect[4])
        led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l2,l1,define_effect[2])
        gun_led_on_off[1]();time.sleep(.5)

        robot.set_mode(define.robot_mode_free)
        gimbal.recenter()
        chassis.set_rotate_speed(120)
        gimbal.set_rotate_speed(120)

        for i in range(2):
            gimbal.rotate(define.gimbal_right)
            chassis.rotate_with_time(define.anticlockwise, 0.3)
            gimbal.rotate(define.gimbal_left)
            chassis.rotate_with_time(define.clockwise, 0.6)
            gimbal.rotate(define.gimbal_right)
            chassis.rotate_with_time(define.anticlockwise, 0.3)
        gun_led_on_off[0]();gimbal.recenter()

# Blaster Fire Function:

    def blaster_fire():
        robot.set_mode(define.robot_mode_free)

        while True:
            randgimbal_speed=random.randint(20,100)
            randup=random.randint(1,55)
            commands_exit=random.randint(a,b)

            gimbal.set_rotate_speed(randgimbal_speed)
            media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

            led_set_flash(define_armor_all,6)
            led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[4])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[2])
            gimbal.rotate_with_degree(define.gimbal_up,randup)

            led.set_flash(define.armor_all,8)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],l1,l2,l2,define_effect[2])
            gun_led_on_off[1]()

            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            gun_led_on_off[0]()

            if commands_exit==a:continue
            elif commands_exit==b:
                led_set_flash(define_armor_all,6)
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[4])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[2])
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
                gimbal.recenter();break

# Scan Search Right Left Function:

    def scan_search_right_left():
        robot.set_mode(define.robot_mode_free)
        def scan_search_right():
            gimbal.set_rotate_speed(scan_speed)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],l1,l2,l1,define_effect[3])
            gun_led_on_off[1]()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(1,250)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)

                if commands_exit==a:continue
                elif commands_exit==b:break

        scan_search_right()

        def scan_search_left():
            gimbal.set_rotate_speed(scan_speed)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],l1,l2,l1,define_effect[3])
            gun_led_on_off[1]()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(-250,1)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)

                if commands_exit==a:continue
                elif commands_exit==b:gimbal.recenter()
                gun_led_on_off[0]();break

        scan_search_left()

# Sleep Function:

    def sleep():
        gimbal.recenter()
        while True:
            randdelay=random.randint(1,180)
            commands_exit=random.randint(a,c)
            
            led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l2,l1,define_effect[3])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],l2,l2,l1,define_effect[3])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],l2,l2,l1,define_effect[3])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],l2,l2,l2,define_effect[3])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],l2,l1,l1,define_effect[3])
            time.sleep(randdelay)

            if commands_exit==a:continue
            elif commands_exit==b:break

# Single Led Chassis Follow Gimbal Rotation Right Left Function:

    def single_led_chassis_follow_gimbal_rotation_right_left():
        robot.set_mode(define.robot_mode_chassis_follow)
        def single_led_chassis_follow_gimbal_rotation_right():
            gimbal.set_rotate_speed(rotate_speed[1])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                for i in range(1,9):
                    gimbal.rotate(define.gimbal_right)

                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define_effect[0])
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_on)

                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        single_led_chassis_follow_gimbal_rotation_right()

        def single_led_chassis_follow_gimbal_rotation_left():
            gimbal.set_rotate_speed(rotate_speed[1])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                for i in range(8,0,-1):
                    gimbal.rotate(define.gimbal_left)
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define_effect[0])
                    led.set_single_led(define.armor_top_all,[i],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        single_led_chassis_follow_gimbal_rotation_left()

# Double Led Chassis Follow Gimbal Rotation Right Left Function:

    def double_led_chassis_follow_gimbal_rotation_right_left():
        robot.set_mode(define.robot_mode_chassis_follow)
        def double_led_chassis_follow_gimbal_rotation_right():
            gimbal.set_rotate_speed(rotate_speed[4])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_right)
                for i in range(1,5):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define_effect[0])
                    led.set_single_led(define.armor_top_all,[i,i+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        double_led_chassis_follow_gimbal_rotation_right()

        def double_led_chassis_follow_gimbal_rotation_left():
            gimbal.set_rotate_speed(rotate_speed[4])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_left)
                for i in range(4,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define_effect[0])
                    led.set_single_led(define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        double_led_chassis_follow_gimbal_rotation_left()

# Quad Led Gimbal Rotation Up Down Function:

    def quad_led_gimbal_rotation_up_down():
        robot.set_mode(define.robot_mode_free)
        gimbal.set_rotate_speed(rotate_speed[0])
        media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

        x=0
        while x<=6:
            gun_led_on_off[1]()
            gimbal.rotate(define.gimbal_up)

            for i in range(2,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[-i][0],RGB_RY[-i][1],RGB_RY[-i][2],define_effect[1])
                time.sleep(delay2);gun_led_on_off[0]()
            x+=1

        led_set_flash(define_armor_all,blink_rate[4])
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],l2,l1,l1,define_effect[2])
        media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
        gimbal.recenter();gun_led_on_off[0]()

# RGB Colour Trail Chasers Forward Reverse Function:

    def rgb_colour_trail_chasers_forward_reverse():
        robot.set_mode(define.robot_mode_chassis_follow)
        def rgb_colour_trail_chasers_forward():
            gimbal.set_rotate_speed(rotate_speed[2])

            for j in range(1,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_right)
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define_effect[2])

                for i in range(1,9):
                    led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                for i in range(1,9):
                    led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[0])
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_trail_chasers_forward()

        def rgb_colour_trail_chasers_reverse():
            gimbal.rotate(define.gimbal_left)

            for j in range(1,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_left)
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define_effect[2])

                for i in range(8,0,-1):
                    led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                for i in range(8,0,-1):
                    led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[0])
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_trail_chasers_reverse()

# RGB Colour Changers Forward Reverse Function:

    def rgb_colour_changers_forward_reverse():
        gimbal.stop()
        def rgb_colour_changers_forward():
            for i in range(1,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_changers_forward()

        def rgb_colour_changers_reverse():
            for i in range(7,0,-1):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_changers_reverse()

# RGB Flash Colour Changers Function:

    def rgb_flash_colour_changers():
        gun_led_on_off[1]()
        for j in range(2):
            for i in range(1,5):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                time.sleep(delay2)

            for i in range(3,1,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define_effect[1])
                time.sleep(delay2)
        gun_led_on_off[0]()

# RGB Colour Flasher Functions:

    def rgb_red_yellow_flasher():
        randloop=random.randint(1,20)
        gun_led_on_off[1]()
        for i in range(randloop):
            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            time.sleep(delay2)

            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[2][0],RGB2[2][1],RGB2[2][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[3][0],RGB2[3][1],RGB2[3][2],define_effect[1])
            time.sleep(delay2)
        gun_led_on_off[0]()

    def rgb_blue_green_flasher():
        randloop=random.randint(1,20)
        gun_led_on_off[1]()
        for i in range(randloop):
            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            time.sleep(delay2)

            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[4][0],RGB2[4][1],RGB2[4][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[5][0],RGB2[5][1],RGB2[5][2],define_effect[1])
            time.sleep(delay2)
        gun_led_on_off[0]()

    def rgb_pink_cyan_flasher():
        randloop=random.randint(1,20)
        gun_led_on_off[1]()
        for i in range(randloop):
            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            time.sleep(delay2)

            led_set_top_bottom[0](define_armor_top_right_left[0],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],RGB2[6][0],RGB2[6][1],RGB2[6][2],define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],RGB2[7][0],RGB2[7][1],RGB2[7][2],define_effect[1])
            time.sleep(delay2)
        gun_led_on_off[0]()

# RGB Colour Dimmer Functions:

    def rgb_white_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,i,i,define_effect[1]) # White
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,i,i,define_effect[1]) # White

    def rgb_red_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,l1,l1,define_effect[1]) # Red
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,l1,l1,define_effect[1]) # Red

    def rgb_yellow_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,i,l1,define_effect[1]) # Yellow
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,i,l1,define_effect[1]) # Yellow

    def rgb_blue_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,l1,i,define_effect[1]) # Blue
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,l1,i,define_effect[1]) # Blue

    def rgb_green_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,i,l1,define_effect[1]) # Green
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,i,l1,define_effect[1]) # Green

    def rgb_pink_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,l1,i,define_effect[1]) # Pink
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],i,l1,i,define_effect[1]) # Pink

    def rgb_cyan_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,l2)
        gun_led_on_off[1]()
        for i in range(0,randdimmer):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,i,i,define_effect[1]) # Cyan
        gun_led_on_off[0]()
        for i in range(randdimmer,0,-1):
            for j in range(2):
                led_set_top_bottom[j](define_armor_top_bottom_all[j],l1,i,i,define_effect[1]) # Cyan

    robomaster_s1_start()

    functions_list=[
        robot_all_wheel_omni_directional_drive,
        gimbal_free_mode_right_left,chassis_follow_gimbal_right_left,
        dance_rock,blaster_fire,scan_search_right_left,
        sleep,single_led_chassis_follow_gimbal_rotation_right_left,
        double_led_chassis_follow_gimbal_rotation_right_left,
        quad_led_gimbal_rotation_up_down,
        rgb_colour_trail_chasers_forward_reverse,
        rgb_colour_changers_forward_reverse,
        rgb_flash_colour_changers,rgb_red_yellow_flasher,
        rgb_blue_green_flasher,rgb_pink_cyan_flasher,
        rgb_white_dimmer,rgb_red_dimmer,rgb_yellow_dimmer,
        rgb_blue_dimmer,rgb_green_dimmer,rgb_pink_dimmer,
        rgb_cyan_dimmer]

    while True:
        randweights_list=random.choices(
            functions_list,weights=[
            100,100,100,50,100,50,5,10,10,100,10,
            10,10,10,10,10,10,10,10,10,10,10,10],k=1)

        randweights_list[0]()

def armor_hit_detection_all(msg):

    media.play_sound(define.media_sound_attacked,wait_for_complete_flag=True)

    gun_led_on_off[0]()
    for i in range(2):
        led_set_top_bottom[i](define_armor_top_bottom_all[i],l2,l1,l1,define_effect[3])
    gimbal.recenter()

    media_wait(define_sound_recognized_twice_thrice[1])

    led.set_flash(define.armor_all,1)
    led_set_top_bottom[0](define_armor_top_bottom_all[0],l2,l1,l1,define_effect[4])
    led_set_top_bottom[1](define_armor_top_bottom_all[1],l2,l1,l1,define_effect[2])
    media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)
    gimbal.recenter()
