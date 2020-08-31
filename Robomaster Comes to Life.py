# Make Robomaster come to life. Simply copy or download this program example.

# You must copy and paste the program code into your Robomaster app. After that,
# simply click the blue play button, then clap your hands three times to wake him up.
# To make him sleep, simply clap your hands twice.

# This Robomaster program example uses two powerful random generator options,
# the random.randint() and the random.choice() functions. These two, random
# generator functions are what make the Robomaster S1 come to life.

# To avoid damaging your Robomaster S1, never set any speeds higher than they
# are shown here, especially in smaller play areas. Note: be cautious when setting
# the drive_speed variable higher than 0.2 and the seconds variable, who's default
# is 1 second per drive time distance.

# IMPORTANT! Never pick up or move the Robomaster S1, while its program is
# running. Doing so may cause damage to the unit; you must stop the program first.

# Robomaster S1 features illustrated here are as follows:

# Gimbal Follow Chassis
# Chassis Follow Gimbal
# Gimbal Free Mode
# Chassis Free Mode
# Scan Search with sound effect
# Blaster Fire with sound effect
# Sleep Mode
# Detection Applause

# I sure hope other Robomaster people find this program very enjoyable and useful. I sure
# put a lot of time into creating it. It sure wasn't no cakewalk when the gimbal and chassis
# would conflict each other during practice execution/runs before I finally figured it all out.

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
led=led_ctrl
define=rm_define

rotate_speed=(20,30,50,100,200)
scan_speed=(40);drive_speed=(0.2)
wheel_degree=(0,180,90,-90,45,-45,135,-135)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)
seconds=1

def start():

# Gimbal Follow Chassis:

    def gimbal_follow_chassis():

        robot.set_mode(define.robot_mode_gimbal_follow)

        def gimbal_follow_chassis_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,180)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.clockwise,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        gimbal_follow_chassis_right()

        def gimbal_follow_chassis_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,180)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.anticlockwise,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        gimbal_follow_chassis_left()

# Chassis Follow Gimbal:

    def chassis_follow_gimbal():

        robot.set_mode(define.robot_mode_chassis_follow)

        def chassis_follow_gimbal_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_top_led(define.armor_top_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    led.set_top_led(define.armor_top_all,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,led2,led1,led1,define.effect_always_on)

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        chassis_follow_gimbal_right()

        def chassis_follow_gimbal_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randwheel=random.choice(wheel_degree)
                randrotate=random.randint(1,180)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=180:
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)
                    led.set_top_led(define.armor_top_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,led2,led2,led1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    led.set_top_led(define.armor_top_all,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_front,led2,led1,led1,define.effect_always_on)

                    chassis.set_trans_speed(drive_speed)
                    chassis.move_with_time(randwheel,seconds)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        chassis_follow_gimbal_left()

# Gimbal Free Mode:

    def gimbal_free_mode():

        robot.set_mode(define.robot_mode_free)

        def gimbal_free_mode_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        gimbal_free_mode_right()

        def gimbal_free_mode_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        gimbal_free_mode_left()

# Chassis Free Mode:

    def chassis_free_mode():

        robot.set_mode(define.robot_mode_free)

        def chassis_free_mode_right():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.clockwise,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        chassis_free_mode_right()

        def chassis_free_mode_left():

            while True:
                randspeed=random.choice(rotate_speed)
                randrotate=random.randint(1,90)

                if randspeed==20:
                    led.set_flash(define.armor_all,blink_rate[0])
                elif randspeed==30:
                    led.set_flash(define.armor_all,blink_rate[1])
                elif randspeed==50:
                    led.set_flash(define.armor_all,blink_rate[2])
                elif randspeed==100:
                    led.set_flash(define.armor_all,blink_rate[3])
                elif randspeed==200:
                    led.set_flash(define.armor_all,blink_rate[4])

                if randrotate<=90:
                    led.set_top_led(define.armor_top_right,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_left,led2,led1,led1,define.effect_always_on)
                    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_always_on)
                    led.set_top_led(define.armor_top_left,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_flash)
                    led.set_bottom_led(define.armor_bottom_front,led2,led2,led1,define.effect_flash)

                    chassis.set_rotate_speed(randspeed)
                    chassis.rotate_with_degree(define.anticlockwise,randrotate)

                    commands_exit=random.randint(1,2)
                    if commands_exit==1:
                        continue
                    elif commands_exit==2:
                        break

        chassis_free_mode_left()

# Scan Search:

    def scan_search():

        robot.set_mode(define.robot_mode_free)

        def scan_search_right():

            gimbal.set_rotate_speed(scan_speed)
            led.set_top_led(define.armor_top_all,led1,led2,led1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,led1,led2,led1,define.effect_breath)
            led.gun_led_on()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(1,250)
                randangle=random.randint(-15,35)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)

                commands_exit=random.randint(1,2)
                if commands_exit==1:
                    continue
                elif commands_exit==2:
                    gimbal.recenter()
                    led.gun_led_off()
                    break

        scan_search_right()

        def scan_search_left():

            gimbal.set_rotate_speed(scan_speed)
            led.set_top_led(define.armor_top_all,led1,led2,led1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_all,led1,led2,led1,define.effect_breath)
            led.gun_led_on()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(-250,1)
                randangle=random.randint(-15,35)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                gimbal.set_rotate_speed(scan_speed)
                media.play_sound(define.media_sound_scanning,wait_for_complete_flag=False)
                gimbal.angle_ctrl(randrotate,randangle)

                commands_exit=random.randint(1,2)
                if commands_exit==1:
                    continue
                elif commands_exit==2:
                    gimbal.recenter()
                    led.gun_led_off()
                    break

        scan_search_left()

# Blaster Fire:

    def blaster_fire():

        robot.set_mode(define.robot_mode_free)

        while True:
            randgimbal_speed=random.randint(20,100)
            randup=random.randint(1,55)

            gimbal.set_rotate_speed(randgimbal_speed)
            media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

            led.set_flash(define.armor_all,6)
            led.set_top_led(define.armor_top_all,led2,led1,led1,define.effect_marquee)
            led.set_bottom_led(define.armor_bottom_all,led2,led1,led1,define.effect_flash)

            gimbal.rotate_with_degree(define.gimbal_up,randup)

            led.set_flash(define.armor_all,8)
            led.set_top_led(define.armor_top_all,led1,led2,led2,define.effect_flash)
            led.set_bottom_led(define.armor_bottom_all,led1,led2,led2,define.effect_flash)

            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)
            media.play_sound(define.media_sound_shoot,wait_for_complete_flag=True)

            commands_exit=random.randint(1,2)
            if commands_exit==1:
                continue
            elif commands_exit==2:
                led.set_flash(define.armor_all,6)
                led.set_top_led(define.armor_top_all,led2,led1,led1,define.effect_marquee)
                led.set_bottom_led(define.armor_bottom_all,led2,led1,led1,define.effect_flash)
                gimbal.recenter()
                break

# Sleep_mode:

    def sleep_mode():

        robot.set_mode(define.robot_mode_free)

        while True:
            randdelay=random.randint(1,2)

            led.set_top_led(define.armor_top_all,led2,led2,led1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_breath)
            led.set_bottom_led(define.armor_bottom_front,led2,led1,led1,define.effect_breath)
            gimbal.recenter()
            time.sleep(randdelay)

            commands_exit=random.randint(1,2)
            if commands_exit==1:
                continue
            elif commands_exit==2:
                break

    while True:
        randfunc=random.randint(1,6)
        randloop=random.randint(1,2)
        randscan=random.randint(1,30)

        if randfunc==1:
            gimbal_follow_chassis()

        elif randfunc==2:
            for i in range(randloop):
                chassis_follow_gimbal()

        elif randfunc==3:
            gimbal_free_mode()
        elif randfunc==4:
            chassis_free_mode()
        elif randfunc==5:
            blaster_fire()
        elif randfunc==6:
            sleep_mode()

        if randscan==29:
            scan_search()

led.set_top_led(define.armor_top_all,led2,led2,led1,define.effect_breath)
led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_breath)
led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_breath)
led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_breath)
led.set_bottom_led(define.armor_bottom_front,led2,led1,led1,define.effect_breath)
gimbal.recenter()

media.enable_sound_recognition(define.sound_detection_applause)
media.cond_wait(define.cond_sound_recognized_applause_thrice)

led.set_flash(define.armor_all,1)
led.set_top_led(define.armor_top_all,led2,led1,led1,define.effect_marquee)
led.set_bottom_led(define.armor_bottom_all,led2,led1,led1,define.effect_flash)
media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)

def sound_recognized_applause_twice(msg):

    robot.set_mode(define.robot_mode_free)

    led.gun_led_off()
    led.set_top_led(define.armor_top_all,led2,led2,led1,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_left,led2,led2,led1,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_right,led2,led2,led1,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_back,led2,led2,led2,define.effect_breath)
    led.set_bottom_led(define.armor_bottom_front,led2,led1,led1,define.effect_breath)
    gimbal.recenter()

    media.cond_wait(define.cond_sound_recognized_applause_thrice)

    led.set_flash(define.armor_all,1)
    led.set_top_led(define.armor_top_all,led2,led1,led1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,led2,led1,led1,define.effect_flash)
    media.play_sound(define.media_sound_count_down,wait_for_complete_flag=True)
    gimbal.recenter()
