'''Robomaster S1 Comes to Life 4.0'''

# Make Robomaster S1 come to life. Simply copy or download this program example.

# You must copy and paste the program code into your Robomaster app. After that,
# simply click the blue play button, then clap your hands three times to wake him
# up. To make him sleep, simply tap any one of his bottom hit detectors.

# This Robomaster program example uses two powerful random generator options,
# the random.randint() and the random.choice() functions. These two, random
# generator functions are what make the Robomaster S1 come to life.

# To avoid damaging your Robomaster S1, never set any speeds higher than they
# are shown here, especially in smaller play areas. Note: be cautious when setting
# the drive_speed variable higher than 0.2 and the seconds variable, who's default
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
# RGB Colour Dimmer Functions

# User Interaction Features:

# Detection Applause
# Hit Detection

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

wheel_degree=0,180,90,-90,45,-45,135,-135
l1,l2=0,255;blink_rate=2,3,4,5,6,8
scan_speed=40;drive_speed=.2
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
    media.enable_sound_recognition(define.sound_detection_applause)
    armor.set_hit_sensitivity(10)

# Robomster S1 Start Function:
   
    def robomaster_s1_start():
        led.gun_led_off()
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_breath)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_breath)
        gimbal.recenter()

        media.cond_wait(define.cond_sound_recognized_applause_thrice)

        led.set_flash(define.armor_all,1)
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
        media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)

# Robot All Wheel Omni Directional Drive Function:

    def robot_all_wheel_omni_directional_drive():

        def robot_all_wheel_omni_directional_drive_right():
            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)

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
            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)

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

        def gimbal_free_mode_right():
            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        gimbal_free_mode_right()

        def gimbal_free_mode_left():
            robot.set_mode(define.robot_mode_free)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        gimbal_free_mode_left()

# Chassis Follow Gimbal Right Left Function:

    def chassis_follow_gimbal_right_left():

        def chassis_follow_gimbal_right():
            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        chassis_follow_gimbal_right()

        def chassis_follow_gimbal_left():
            robot.set_mode(define.robot_mode_chassis_follow)

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)
                commands_exit=random.randint(a,b)

                if randspeed==20:led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==40:led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==50:led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==60:led.set_flash(define.armor_all,blink_rate[4])
                elif randspeed==80:led.set_flash(define.armor_all,blink_rate[5])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,l2,l1,l1,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,l2,l1,l1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_back,l2,l2,l1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        chassis_follow_gimbal_left()

# Dance Rock Function:

    def dance_rock():

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
    
        led.gun_led_off()
        gimbal.recenter()

# Blaster Fire Function:

    def blaster_fire():

        robot.set_mode(define.robot_mode_free)

        while True:
            randgimbal_speed=random.randint(20,100)
            randup=random.randint(1,55)
            commands_exit=random.randint(a,b)

            gimbal.set_rotate_speed(randgimbal_speed)
            media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

            led.set_flash(define.armor_all,6)
            led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
            led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)

            gimbal.rotate_with_degree(define.gimbal_up,randup)

            led.set_flash(define.armor_all,8)
            led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_flash)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_flash)
            led.gun_led_on()

            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            led.gun_led_off()

            if commands_exit==a:continue
            elif commands_exit==b:
                led.set_flash(define.armor_all,6)
                led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
                led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
                gimbal.recenter();break

# Scan Search Right Left Function:

    def scan_search_right_left():

        def scan_search_right():
            robot.set_mode(define.robot_mode_free)
            gimbal.set_rotate_speed(scan_speed)
            
            led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_breath)
            led.gun_led_on()

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

            robot.set_mode(define.robot_mode_free)
            gimbal.set_rotate_speed(scan_speed)
            
            led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_breath)
            led.gun_led_on()

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
                led_ctrl.gun_led_off();break

        scan_search_left()

# Sleep Function:

    def sleep():
        robot.set_mode(define.robot_mode_free)

        while True:
            randdelay=random.randint(1,4)
            commands_exit=random.randint(a,c)

            led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_right,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_left,l2,l2,l1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_front,l2,l2,l2,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_breath)
            gimbal.recenter();time.sleep(randdelay)

            if commands_exit==a:continue
            elif commands_exit==b:break

# Single Led Chassis Follow Gimbal Rotation Right Left Function:

    def single_led_chassis_follow_gimbal_rotation_right_left():

        def single_led_chassis_follow_gimbal_rotation_right():
            robot.set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[1])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                for i in range(1,9):
                    gimbal.rotate(define.gimbal_right)

                    led.set_top_led(define.armor_top_all,
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_on)

                    led.set_bottom_led(define.armor_bottom_all,
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define.effect_always_on)
                    time.sleep(delay2);led.gun_led_off()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        single_led_chassis_follow_gimbal_rotation_right()

        def single_led_chassis_follow_gimbal_rotation_left():
            robot.set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[1])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                for i in range(8,0,-1):
                    gimbal.rotate(define.gimbal_left)
                    led.set_top_led(define.armor_top_all,
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)
                    led.set_single_led(define.armor_top_all,[i],define.effect_always_on)

                    led.set_bottom_led(define.armor_bottom_all,
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define.effect_always_on)
                    time.sleep(delay2);led.gun_led_off()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        single_led_chassis_follow_gimbal_rotation_right()

# Double Led Chassis Follow Gimbal Rotation Right Left Function:

    def double_led_chassis_follow_gimbal_rotation_right_left():

        def double_led_chassis_follow_gimbal_rotation_right():
            robot.set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[4])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                gimbal.rotate(define.gimbal_right)
                for i in range(1,5):
                    led.set_top_led(define.armor_top_all,
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)
                    led.set_single_led(define.armor_top_all,
                    [i,i+4],define.effect_always_on)

                    led.set_bottom_led(define.armor_bottom_all,
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define.effect_always_on)
                    time.sleep(delay2);led.gun_led_off()
                x+=1

                if commands_exit==a:continue
                elif commands_exit==b:break

        double_led_chassis_follow_gimbal_rotation_right()

        def double_led_chassis_follow_gimbal_rotation_left():
            robot.set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[4])

            x=0
            while x<=7:
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                gimbal.rotate(define.gimbal_left)
                for i in range(4,0,-1):
                    led.set_top_led(define.armor_top_all,
                    RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)
                    led.set_single_led(define.armor_top_all,
                    [i,i+4],define.effect_always_on)

                    led.set_bottom_led(define.armor_bottom_all,
                    RGB1[-i][0],RGB1[-i][1],RGB1[-i][2],define.effect_always_on)
                    time.sleep(delay2);led.gun_led_off()
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
            led.gun_led_on()
            gimbal.rotate(define.gimbal_up)
            for i in range(2,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+2,i+4,i+6],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB_RY[-i][0],RGB_RY[-i][1],RGB_RY[-i][2],define.effect_always_on)
                time.sleep(delay2)
            x+=1

        led.set_flash(define.armor_all,blink_rate[4])
        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
        media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)
        gimbal.recenter();led.gun_led_off()

# RGB Colour Trail Chasers Forward Reverse Function:

    def rgb_colour_trail_chasers_forward_reverse():

        def rgb_colour_trail_chasers_forward():
            robot.set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[2])

            for j in range(1,8):
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                gimbal.rotate(define.gimbal_right)
                led.set_top_led(define.armor_top_all,
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define.effect_always_off)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define.effect_flash)

                for i in range(1,9):
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_on)
                    time.sleep(delay2)
                led.gun_led_off()

                for i in range(1,9):
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_off)
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_trail_chasers_forward()

        def rgb_colour_trail_chasers_reverse():
            gimbal.rotate(define.gimbal_left)

            for j in range(1,8):
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                gimbal.rotate(define.gimbal_left)
                led.set_top_led(define.armor_top_all,
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define.effect_always_off)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[j][0],RGB2[j][1],RGB2[j][2],define.effect_flash)

                for i in range(8,0,-1):
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_on)
                    time.sleep(delay2)
                led.gun_led_off()

                for i in range(8,0,-1):
                    led.set_single_led(define.armor_top_all,
                    [i],define.effect_always_off)
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_trail_chasers_reverse()

# RGB Colour Changers Forward Reverse Function:

    def rgb_colour_changers_forward_reverse():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        def rgb_colour_changers_forward():
            for i in range(1,8):
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
                time.sleep(delay1)
                led_ctrl.gun_led_off()

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_changers_forward()

        def rgb_colour_changers_reverse():
            for i in range(7,0,-1):
                commands_exit=random.randint(a,b)
                led.gun_led_on()
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
                time.sleep(delay1)
                led_ctrl.gun_led_off()

                if commands_exit==a:continue
                elif commands_exit==b:break
   
        rgb_colour_changers_reverse()

# RGB Flash Colour Changers Function:
        
    def rgb_flash_colour_changers():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        for j in range(2):
            led_ctrl.gun_led_on()
            for i in range(1,5):
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
                
                led.set_bottom_led(define.armor_bottom_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
                time.sleep(delay2)
            
            for i in range(3,1,-1):
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
                time.sleep(delay2)
                led_ctrl.gun_led_off()
                
# RGB Colour Dimmer Functions:

    def rgb_white_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,i,i,i,define.effect_always_on) # White
            led.set_bottom_led(define.armor_bottom_all,i,i,i,define.effect_always_on) # White
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,i,i,i,define.effect_always_on) # White
            led.set_bottom_led(define.armor_bottom_all,i,i,i,define.effect_always_on) # White

    def rgb_red_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,i,l1,l1,define.effect_always_on) # Red
            led.set_bottom_led(define.armor_bottom_all,i,l1,l1,define.effect_always_on) # Red
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,i,l1,l1,define.effect_always_on) # Red
            led.set_bottom_led(define.armor_bottom_all,i,l1,l1,define.effect_always_on) # Red

    def rgb_yellow_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,i,i,l1,define.effect_always_on) # Yellow
            led.set_bottom_led(define.armor_bottom_all,i,i,l1,define.effect_always_on) # Yellow
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,i,i,l1,define.effect_always_on) # Yellow
            led.set_bottom_led(define.armor_bottom_all,i,i,l1,define.effect_always_on) # Yellow

    def rgb_blue_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,l1,l1,i,define.effect_always_on) # Blue
            led.set_bottom_led(define.armor_bottom_all,l1,l1,i,define.effect_always_on) # Blue
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,l1,l1,i,define.effect_always_on) # Blue
            led.set_bottom_led(define.armor_bottom_all,l1,l1,i,define.effect_always_on) # Blue

    def rgb_green_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,l1,i,l1,define.effect_always_on) # Green
            led.set_bottom_led(define.armor_bottom_all,l1,i,l1,define.effect_always_on) # Green
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,l1,i,l1,define.effect_always_on) # Green
            led.set_bottom_led(define.armor_bottom_all,l1,i,l1,define.effect_always_on) # Green

    def rgb_pink_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,i,l1,i,define.effect_always_on) # Pink
            led.set_bottom_led(define.armor_bottom_all,i,l1,i,define.effect_always_on) # Pink
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,i,l1,i,define.effect_always_on) # Pink
            led.set_bottom_led(define.armor_bottom_all,i,l1,i,define.effect_always_on) # Pink

    def rgb_cyan_dimmer():
        gimbal.stop()
        robot.set_mode(define.robot_mode_chassis_follow)
        randdimmer=random.randint(0,255)
        led.gun_led_on()
        for i in range(0,randdimmer):
            led.set_top_led(define.armor_top_all,l1,i,i,define.effect_always_on) # Cyan
            led.set_bottom_led(define.armor_bottom_all,l1,i,i,define.effect_always_on) # Cyan
        led.gun_led_off()
        for i in range(randdimmer,0,-1):
            led.set_top_led(define.armor_top_all,l1,i,i,define.effect_always_on) # Cyan
            led.set_bottom_led(define.armor_bottom_all,l1,i,i,define.effect_always_on) # Cyan

    robomaster_s1_start()

    while True:
        randfunc=random.randint(1,100)
        if randfunc==1:robot_all_wheel_omni_directional_drive()
        elif randfunc==2:gimbal_free_mode_right_left()
        elif randfunc==3:chassis_follow_gimbal_right_left()
        elif randfunc==4:dance_rock()
        elif randfunc==5:blaster_fire()
        elif randfunc==100:scan_search_right_left()
        elif randfunc==99:sleep()
        elif randfunc==6:single_led_chassis_follow_gimbal_rotation_right_left()
        elif randfunc==7:double_led_chassis_follow_gimbal_rotation_right_left()
        elif randfunc==8:quad_led_gimbal_rotation_up_down()
        elif randfunc==9:rgb_colour_trail_chasers_forward_reverse()
        elif randfunc==10:rgb_colour_changers_forward_reverse()
        elif randfunc==11:rgb_flash_colour_changers()
        elif randfunc==12:rgb_white_dimmer()
        elif randfunc==13:rgb_red_dimmer()
        elif randfunc==14:rgb_yellow_dimmer()
        elif randfunc==15:rgb_blue_dimmer()
        elif randfunc==16:rgb_green_dimmer()
        elif randfunc==17:rgb_pink_dimmer()
        elif randfunc==18:rgb_cyan_dimmer()

def armor_hit_detection_all(msg):

    media.play_sound(define.media_sound_attacked,wait_for_complete_flag=True)
    
    led.gun_led_off()
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_breath)
    gimbal.recenter()

    media.cond_wait(define.cond_sound_recognized_applause_thrice)

    led.set_flash(define.armor_all,1)
    led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_flash)
    media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)
    gimbal.recenter()
