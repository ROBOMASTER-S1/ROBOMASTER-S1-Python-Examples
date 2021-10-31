'''Robomaster S1 Comes to Life 4.0'''

# Make Robomaster S1 come to life. Simply copy or download this program example.

# You must copy and paste the program code into your Robomaster app. After that,
# simply click the blue play button, then clap your hands three times to wake him
# up. To make him sleep, simply tap any one of his bottom hit detectors.

# This Robomaster S1 program example uses four powerful random generator
# functions. The random.randint(), the random.choice(), the random.choices() and
# random.shuffle() functions. These four random generator functions are what make
# the Robomaster S1 come to life and appear to have a mind of its own.

# To avoid damaging your Robomaster S1, never set any speeds higher than they
# are shown here, especially in smaller play areas. Note: be cautious when setting
# the drive_speed variable higher than 0.3 and the seconds variable, who's default
# is 2 seconds per drive time distance.

# IMPORTANT! Never pick up or move the Robomaster S1, while its program is
# running. Doing so may cause damage to the unit; you must stop the program first.

# Robomaster S1 feature functions illustrated here are as follows:

# Robomster S1 Comes to Life Function with sound effect
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
# RGB Colour Flipper Functions
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

robot_set_mode=robot_ctrl.set_mode
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

led_set_flash=led_ctrl.set_flash
led_set_single=led.set_single_led

led_set_top_bottom=(
led_ctrl.set_top_led,
led_ctrl.set_bottom_led)

gun_led_on_off=(
led_ctrl.gun_led_off,
led.gun_led_on)

define_armor_all=rm_define.armor_all

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

media_wait=media_ctrl.cond_wait

media_play_sound=media_ctrl.play_sound

define_detection_applause=(
rm_define.sound_detection_applause)

define_sound_recognized_twice_thrice=(
rm_define.cond_sound_recognized_applause_twice,
rm_define.cond_sound_recognized_applause_thrice)

armor_set_sensitivity=(armor_ctrl.set_hit_sensitivity)

wheel_degree=0,180,90,-90,45,-45,135,-135
l1,l2=0,255;blink_rate=2,3,4,5,6,8
scan_speed=50;drive_speed=.3
rotate_speed=20,30,40,50,60,80
seconds,milli_seconds=2,.2
delay1,delay2,delay3=1,.1,.05
a,b,c,x,y=1,2,3,1,-1

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

def start():
    gun_led_on_off[0]()
    media_enable_disable[1](define_detection_applause)
    armor_set_sensitivity(10)

# Robomster S1 Comes to Life Function:

    def robomaster_s1_comes_to_life():
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],
            RGB_COLOURS[2][0],RGB_COLOURS[2][1],RGB_COLOURS[2][2],define_effect[3])

        media_wait(define_sound_recognized_twice_thrice[1])

        led_set_flash(define_armor_all,3);get_value={1:4,2:2}
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],
            RGB_COLOURS[2][0],RGB_COLOURS[2][1],
            RGB_COLOURS[2][2],define_effect[get_value.get(i+1)])

        media_play_sound(define.media_sound_count_down,
        wait_for_complete_flag=True)

# Robot All Wheel Omni Directional Drive Function:

    def robot_all_wheel_omni_directional_drive():
        def robot_all_wheel_omni_directional_drive_right():
            robot_set_mode(define.robot_mode_chassis_follow)
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
                    get_value={1:2,2:1}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                    RGB_COLOURS[3][2],define_effect[1])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                        RGB_COLOURS[3][2],define_effect[1])
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+1][2],define_effect[1])

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

        def robot_all_wheel_omni_directional_drive_left():
            robot_set_mode(define.robot_mode_chassis_follow)
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
                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_left,randrotate)

                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                    RGB_COLOURS[3][2],define_effect[1])
                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                        RGB_COLOURS[3][2],define_effect[1])
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+1][2],define_effect[1])

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

        func_list=[robot_all_wheel_omni_directional_drive_right,robot_all_wheel_omni_directional_drive_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# Gimbal Free Mode Right Left Function:

    def gimbal_free_mode_right_left():
        def gimbal_free_mode_right():
            robot_set_mode(define.robot_mode_free)
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
                    get_value={1:2,2:1}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        def gimbal_free_mode_left():
            robot_set_mode(define.robot_mode_free)
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
                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        func_list=[gimbal_free_mode_right,gimbal_free_mode_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# Chassis Follow Gimbal Right Left Function:

    def chassis_follow_gimbal_right_left():
        def chassis_follow_gimbal_right():
            robot_set_mode(define.robot_mode_chassis_follow)
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
                    get_value={1:2,2:1}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.gimbal_right,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        def chassis_follow_gimbal_left():
            robot_set_mode(define.robot_mode_chassis_follow)
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
                    get_value={1:1,2:2}
                    for i in range(2):
                        led_set_top_bottom[0](define_armor_top_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_right_left[i],
                        RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],
                        RGB_COLOURS[i+2][2],define_effect[get_value.get(i+1)])

                    for i in range(2):
                        led_set_top_bottom[1](define_armor_bottom_front_back[i],
                        RGB_COLOURS[1][0],RGB_COLOURS[1][1],
                        RGB_COLOURS[i+1][2],define_effect[get_value.get(i+1)])

                    gimbal.set_rotate_speed(randspeed)
                    gimbal.rotate_with_degree(define.chassis_left,randrotate)

                    if commands_exit==a:continue
                    elif commands_exit==b:break

        func_list=[chassis_follow_gimbal_right,chassis_follow_gimbal_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# Dance Rock Function:

    def dance_rock():
        robot_set_mode(define.robot_mode_chassis_follow)
        get_value={1:4,2:2}
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],
            RGB_COLOURS[5][0],RGB_COLOURS[5][1],
            RGB_COLOURS[5][2],define_effect[get_value.get(i+1)])
        gun_led_on_off[1]();time.sleep(.5)

        robot_set_mode(define.robot_mode_free)
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
        robot_set_mode(define.robot_mode_free)
        while True:
            randgimbal_speed=random.randint(20,100)
            randup=random.randint(1,55)
            commands_exit=random.randint(a,b)

            gimbal.set_rotate_speed(randgimbal_speed)
            media.play_sound(define.media_sound_gimbal_rotate,
            wait_for_complete_flag=False)

            get_value={1:4,2:2}
            led_set_flash(define_armor_all,6)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],
                RGB_COLOURS[2][0],RGB_COLOURS[2][1],
                RGB_COLOURS[2][2],define_effect[get_value.get(i+1)])
            gimbal.rotate_with_degree(define.gimbal_up,randup)

            led_set_flash(define.armor_all,8)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],
                RGB_COLOURS[7][0],RGB_COLOURS[7][1],
                RGB_COLOURS[7][2],define_effect[2])
            gun_led_on_off[1]()

            for i in range(2):
                media.play_sound(define.media_sound_shoot,
                wait_for_complete_flag=True)
            gun_led_on_off[0]()

            if commands_exit==a:continue
            elif commands_exit==b:
                led_set_flash(define_armor_all,6)
                get_value={1:4,2:2}
                for i in range(2):
                    led_set_top_bottom[i](define_armor_top_bottom_all[i],
                    RGB_COLOURS[2][0],RGB_COLOURS[2][1],
                    RGB_COLOURS[2][2],define_effect[get_value.get(i+1)])
                media.play_sound(define.media_sound_gimbal_rotate,
                wait_for_complete_flag=False);gimbal.recenter();break

# Scan Search Right Left Function:

    def scan_search_right_left():
        robot_set_mode(define.robot_mode_free)
        def scan_search_right():
            gimbal.set_rotate_speed(scan_speed)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],
                RGB_COLOURS[5][0],RGB_COLOURS[5][1],
                RGB_COLOURS[5][2],define_effect[3])
            gun_led_on_off[1]()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(1,250)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                media.play_sound(define.media_sound_scanning,
                wait_for_complete_flag=False)
                gimbal.set_rotate_speed(randgimbal_speed)
                gimbal.set_rotate_speed(scan_speed)
                gimbal.angle_ctrl(randrotate,randangle)

                if commands_exit==a:continue
                elif commands_exit==b:break

        def scan_search_left():
            gimbal.set_rotate_speed(scan_speed)
            for i in range(2):
                led_set_top_bottom[i](define_armor_top_bottom_all[i],
                RGB_COLOURS[5][0],RGB_COLOURS[5][1],
                RGB_COLOURS[5][2],define_effect[3])
            gun_led_on_off[1]()

            while True:
                randgimbal_speed=random.randint(20,100)
                randrotate=random.randint(-250,1)
                randangle=random.randint(-15,35)
                commands_exit=random.randint(a,b)

                media.play_sound(define.media_sound_scanning,
                wait_for_complete_flag=False)
                gimbal.set_rotate_speed(randgimbal_speed)
                gimbal.set_rotate_speed(scan_speed)
                gimbal.angle_ctrl(randrotate,randangle)

                if commands_exit==a:continue
                elif commands_exit==b:break

        func_list=[scan_search_right,scan_search_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()
        gimbal.recenter()

# Sleep Function:

    def sleep():
        robot_set_mode(define.robot_mode_chassis_follow)
        while True:
            randdelay=random.randint(1,30)
            commands_exit=random.randint(a,b)
            for i in range(2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                RGB_COLOURS[3][2],define_effect[3])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[3][0],RGB_COLOURS[3][1],
                RGB_COLOURS[3][2],define_effect[3])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],
                RGB_COLOURS[i+1][2],define_effect[3])
            gimbal.recenter();time.sleep(randdelay)

            if commands_exit==a:continue
            elif commands_exit==b:break

# Single Led Chassis Follow Gimbal Rotation Right Left Function:

    def single_led_chassis_follow_gimbal_rotation_right_left():
        robot_set_mode(define.robot_mode_chassis_follow)
        def single_led_chassis_follow_gimbal_rotation_right():
            gimbal.set_rotate_speed(rotate_speed[1])
            while True:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                for i in range(x,9):
                    gimbal.rotate(define.gimbal_right)

                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RYBG[i][0],RGB_RYBG[i][1],RGB_RYBG[i][2],define_effect[0])
                    led_set_single(define.armor_top_all,[i],define.effect_always_on)

                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RYBG[-i][0],RGB_RYBG[-i][1],RGB_RYBG[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        def single_led_chassis_follow_gimbal_rotation_left():
            gimbal.set_rotate_speed(rotate_speed[1])
            while True:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                for i in range(8,0,y):
                    gimbal.rotate(define.gimbal_left)
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RYBG[i][0],RGB_RYBG[i][1],RGB_RYBG[i][2],define_effect[0])

                    led_set_single(define.armor_top_all,[i],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RYBG[-i][0],RGB_RYBG[-i][1],RGB_RYBG[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        func_list=[
        single_led_chassis_follow_gimbal_rotation_right,
        single_led_chassis_follow_gimbal_rotation_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# Double Led Chassis Follow Gimbal Rotation Right Left Function:

    def double_led_chassis_follow_gimbal_rotation_right_left():
        robot_set_mode(define.robot_mode_chassis_follow)
        def double_led_chassis_follow_gimbal_rotation_right():
            gimbal.set_rotate_speed(rotate_speed[4])
            while True:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_right)
                for i in range(x,5):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RYBG[i][0],RGB_RYBG[i][1],RGB_RYBG[i][2],define_effect[0])

                    led_set_single(define.armor_top_all,[i,i+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RYBG[-i][0],RGB_RYBG[-i][1],RGB_RYBG[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        def double_led_chassis_follow_gimbal_rotation_left():
            gimbal.set_rotate_speed(rotate_speed[4])
            while True:
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_left)
                for i in range(4,0,y):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RYBG[i][0],RGB_RYBG[i][1],RGB_RYBG[i][2],define_effect[0])

                    led_set_single(define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_RYBG[-i][0],
                    RGB_RYBG[-i][1],RGB_RYBG[-i][2],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        double_led_chassis_follow_gimbal_rotation_left()

        func_list=[double_led_chassis_follow_gimbal_rotation_right,double_led_chassis_follow_gimbal_rotation_left]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# Quad Led Gimbal Rotation Up Down Function:

    def quad_led_gimbal_rotation_up_down():
        robot_set_mode(define.robot_mode_free)
        gimbal.set_rotate_speed(rotate_speed[0])
        media.play_sound(define.media_sound_gimbal_rotate,
        wait_for_complete_flag=False)

        for i in range(6):
            gun_led_on_off[1]()
            gimbal.rotate(define.gimbal_up)
            for j in range(2,0,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[j][0],RGB_RY[j][1],RGB_RY[j][2],define_effect[0])

                led_set_single(define_armor_top_bottom_all[0],[j,j+2,j+4,j+6],define_effect[1])

                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[-j][0],RGB_RY[-j][1],RGB_RY[-j][2],define_effect[1])
                time.sleep(delay2);gun_led_on_off[0]()

        led_set_flash(define_armor_all,blink_rate[4])
        for i in range(2):
            led_set_top_bottom[i](define_armor_top_bottom_all[i],l2,l1,l1,define_effect[2])
        media.play_sound(define.media_sound_gimbal_rotate,
        wait_for_complete_flag=False);gimbal.recenter();gun_led_on_off[0]()

# RGB Colour Trail Chasers Forward Reverse Function:

    def rgb_colour_trail_chasers_forward_reverse():
        def rgb_colour_trail_chasers_forward():
            robot_set_mode(define.robot_mode_chassis_follow)
            gimbal.set_rotate_speed(rotate_speed[2])
            for i in range(x,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_right)
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(x,9):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                for j in range(x,9):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        def rgb_colour_trail_chasers_reverse():
            gimbal.rotate(define.gimbal_left)

            for i in range(x,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                gimbal.rotate(define.gimbal_left)
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(8,0,y):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay2);gun_led_on_off[0]()

                for j in range(8,0,y):
                    led_set_single(define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay2)

                if commands_exit==a:continue
                elif commands_exit==b:break

        func_list=[
        rgb_colour_trail_chasers_forward,
        rgb_colour_trail_chasers_reverse]

        randloop=random.randint(0,4)
        for i in range(randloop):
            random.shuffle(func_list)
            func_list[0]()

# RGB Colour Changers Forward Reverse Function:

    def rgb_colour_changers_forward_reverse():
        gimbal.stop()
        def rgb_colour_changers_forward():
            for i in range(x,8):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_changers_forward()

        def rgb_colour_changers_reverse():
            for i in range(7,0,y):
                commands_exit=random.randint(a,b)
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[0]()

                if commands_exit==a:continue
                elif commands_exit==b:break

        rgb_colour_changers_reverse()

# RGB Flash Colour Changers Function:

    def rgb_flash_colour_changers():
        gun_led_on_off[1]()
        for i in range(2):
            for j in range(x,5):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[j][0],RGB_COLOURS[j][1],RGB_COLOURS[j][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[j][0],RGB_COLOURS[j][1],RGB_COLOURS[j][2],define_effect[1])
                time.sleep(delay2)

            for j in range(3,1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[j][0],RGB_COLOURS[j][1],RGB_COLOURS[j][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[j][0],RGB_COLOURS[j][1],RGB_COLOURS[j][2],define_effect[1])
                time.sleep(delay2)
        gun_led_on_off[0]()

# RGB Colour Flasher Functions:

    def rgb_red_yellow_flasher():
        randloop=random.randint(0,5)
        gun_led_on_off[1]()
        for i in range(randloop):
            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+2][0],
                RGB_COLOURS[j+2][1],RGB_COLOURS[j+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+1][0],RGB_COLOURS[j+1][1],
                RGB_COLOURS[j+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+1][0],RGB_COLOURS[j+3][1],
                RGB_COLOURS[j+2][2],define_effect[1])
                time.sleep(delay3)

            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+1][0],
                RGB_COLOURS[j+1][1],RGB_COLOURS[j+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+1][0],RGB_COLOURS[j+2][1],
                RGB_COLOURS[j+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+3][0],RGB_COLOURS[j+2][1],
                RGB_COLOURS[j+2][2],define_effect[1])
                time.sleep(delay3)
        gun_led_on_off[0]()

    def rgb_blue_green_flasher():
        randloop=random.randint(0,5)
        gun_led_on_off[1]()
        for i in range(randloop):
            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+4][0],
                RGB_COLOURS[j+4][1], RGB_COLOURS[j+1][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+4][0],RGB_COLOURS[j+5][1],
                RGB_COLOURS[j+5][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+4][0],RGB_COLOURS[j+4][2],
                RGB_COLOURS[j+5][2],define_effect[1])
                time.sleep(delay3)

            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+4][0],
                RGB_COLOURS[j+5][1],RGB_COLOURS[j+5][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+4][0],RGB_COLOURS[j+4][1],
                RGB_COLOURS[j+1][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+4][0],RGB_COLOURS[j+5][2],
                RGB_COLOURS[j+1][2],define_effect[1])
                time.sleep(delay3)
        gun_led_on_off[0]()

    def rgb_pink_cyan_flasher():
        randloop=random.randint(0,5)
        gun_led_on_off[1]()
        for i in range(randloop):
            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+6][0],
                RGB_COLOURS[j+6][1],RGB_COLOURS[j+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+5][0],RGB_COLOURS[j+5][1],
                RGB_COLOURS[j+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+5][0],RGB_COLOURS[j+5][1],
                RGB_COLOURS[j+6][2],define_effect[1])
                time.sleep(delay3)

            for j in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[j],RGB_COLOURS[j+5][0],
                RGB_COLOURS[j+5][1],RGB_COLOURS[j+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[j],
                RGB_COLOURS[j+6][0],RGB_COLOURS[j+6][1],
                RGB_COLOURS[j+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[j],
                RGB_COLOURS[j+3][0],RGB_COLOURS[j+6][1],
                RGB_COLOURS[j+6][2],define_effect[1])
                time.sleep(delay3)
        gun_led_on_off[0]()

# RGB Colour Flipper Functions:

    def rgb_red_yellow_flipper():
        randloop=random.randint(0,5)
        for i in range(randloop):
            for j in range(2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],
                [1,2,3,4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[1])
                time.sleep(milli_seconds)

                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],
                [5,6,7,8],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[1])
                time.sleep(milli_seconds)

    def rgb_blue_green_flipper():
        randloop=random.randint(0,5)
        for i in range(randloop):
            for j in range(2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],
                [1,2,3,4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[1])
                time.sleep(milli_seconds)

                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],
                [5,6,7,8],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[1])
                time.sleep(milli_seconds)

    def rgb_pink_cyan_flipper():
        randloop=random.randint(0,5)
        for i in range(randloop):
            for j in range(2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],
                [1,2,3,4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[1])
                time.sleep(milli_seconds)

                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[0])
                led_set_single(define_armor_top_bottom_all[0],
                [5,6,7,8],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[1])
                time.sleep(milli_seconds)

# RGB Colour Dimmer Functions:

    def rgb_white_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,i,i,define_effect[1]) # White
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,i,i,define_effect[1]) # White

    def rgb_red_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,l1,l1,define_effect[1]) # Red
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,l1,l1,define_effect[1]) # Red

    def rgb_yellow_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,i,l1,define_effect[1]) # Yellow
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,i,l1,define_effect[1]) # Yellow

    def rgb_blue_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()

        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,l1,i,define_effect[1]) # Blue
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,l1,i,define_effect[1]) # Blue

    def rgb_green_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,i,l1,define_effect[1]) # Green
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,i,l1,define_effect[1]) # Green

    def rgb_pink_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,l1,i,define_effect[1]) # Pink
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],i,l1,i,define_effect[1]) # Pink

    def rgb_cyan_dimmer():
        gimbal.stop()
        randdimmer=random.randint(0,x)
        gun_led_on_off[1]()
        for i in range(randdimmer):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,i,i,define_effect[1]) # Cyan
        gun_led_on_off[0]()

        for i in range(randdimmer,y,y):
            for j in range(2):
                led_set_top_bottom[j](
                define_armor_top_bottom_all[j],l1,i,i,define_effect[1]) # Cyan

    robomaster_s1_comes_to_life()

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
        rgb_red_yellow_flipper,rgb_blue_green_flipper,rgb_pink_cyan_flipper,
        rgb_white_dimmer,rgb_red_dimmer,rgb_yellow_dimmer,
        rgb_blue_dimmer,rgb_green_dimmer,rgb_pink_dimmer,
        rgb_cyan_dimmer]

    while True:
        gun_led_on_off[0]()
        randweights_list=random.choices(
        functions_list,weights=[100,100,100,50,100,50,5,10,10,
        100,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],k=1)

        randweights_list[0]()

def armor_hit_detection_all(msg):
    media.play_sound(
    define.media_sound_attacked,
    wait_for_complete_flag=True)

    gun_led_on_off[0]()
    for i in range(2):
        led_set_top_bottom[i](define_armor_top_bottom_all[i],
        RGB_COLOURS[2][0],RGB_COLOURS[2][1],
        RGB_COLOURS[2][2],define_effect[3]);gimbal.recenter()

    media_wait(define_sound_recognized_twice_thrice[1])

    led_set_flash(define.armor_all,1)
    get_value={1:4,2:2}
    for i in range(2):
        led_set_top_bottom[i](define_armor_top_bottom_all[i],
        RGB_COLOURS[2][0],RGB_COLOURS[2][1],
        RGB_COLOURS[2][2],define_effect[get_value.get(i+1)])
    media.play_sound(define.media_sound_count_down,
    wait_for_complete_flag=True);gimbal.recenter()
