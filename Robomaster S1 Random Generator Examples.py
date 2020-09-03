# Gimbal Follow Chassis Right, Left Random Rotations and Random Speed Settings Example:

# Make the gimbal follow the chassis at random rotations and random speed settings.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
chassis=chassis_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

rotate_speed=(20,30,50,100,200)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)

def start():

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
        
    while True:
        gimbal_follow_chassis()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Chassis Follow Gimbal Right, Left Random Rotations, Random Speed Settings and Drive Example:

# Make the chassis follow the gimbal at random rotations, random speed settings and drive.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

rotate_speed=(20,30,50,100,200)
drive_speed=(0.2)
wheel_degree=(0,180,90,-90,45,-45,135,-135)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)
seconds=1

def start():
    
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

    while True:
        chassis_follow_gimbal()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Gimbal Free Mode Right, Left Random Rotations and Random Speed Settings Example:

# Make the gimbal rotate back and forth at random rotations and random speed settings.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
gimbal=gimbal_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

rotate_speed=(20,30,50,100,200)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)

def start():
    
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

    while True:
        gimbal_free_mode()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Chassis Free Mode Right, Left Random Rotations and Random Speed Settings Example:

# Make the chassis rotate back and forth at random rotations and random speed settings.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
chassis=chassis_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

rotate_speed=(20,30,50,100,200)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)

def start():
    
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
        
    while True:
        chassis_free_mode()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Scan Search Right, Left Random Rotations Example:

# Make the Robomaster S1 scan search at random rotations.
# place two sound effects "media_sound_gimbal_rotate" and "media_sound_scanning" sounds.
# invoke the "wait_for_complete_flag=False)" to allow the sound effects and the gimbal to work
# at the same time.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
gimbal=gimbal_ctrl
media=media_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

scan_speed=(40)
led1,led2=(0,255);blink_rate=(1,3,5,8,10)

def start():
    
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
                    led.gun_led_off()
                    break

        scan_search_left()
        
    while True:        
        scan_search()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Blaster Fire Up, Down Random Example:

# Make the Robomaster S1 fire his blaster up and down at random.
# place two sound effects "media_sound_gimbal_rotate" and "media_sound_shoot" sounds.
# invoke the "wait_for_complete_flag=False)" to allow the sound effects and the gimbal to
# work at the same time. Also invoke the "wait_for_complete_flag=True)" to make the gimbal
# stop moving up and down, while the "media_sound_shoot" sound effect plays.

# Create some strings to shorten some of the long Robomaster S1 commands, such as those
# long led commands. Note: only these strings below can be used to shorten most Robomaster
# S1 commands. Also give these strings similar names to the ones used for parts of Robomaster
# S1's commands.

# Example:

# led_ctrl.set_bottom_led(rm_define.armor_bottom_right,255,0,0,rm_define.effect_always_on)

# led.set_bottom_led(define.armor_bottom_right,255,0,0,define.effect_always_on)

robot=robot_ctrl
gimbal=gimbal_ctrl
media=media_ctrl
led=led_ctrl
define=rm_define

# Create some more strings to keep your Python code efficient.

led1,led2=(0,255);blink_rate=(1,3,5,8,10)

def start():
    
    def blaster_fire():

        def blaster_fire_up():

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
                    break

        blaster_fire_up()
                
        def blaster_fire_down():
            
            while True:
                randgimbal_speed=random.randint(20,100)
                randdown=random.randint(1,55)

                gimbal.set_rotate_speed(randgimbal_speed)
                media.play_sound(define.media_sound_gimbal_rotate,wait_for_complete_flag=False)

                led.set_flash(define.armor_all,6)
                led.set_top_led(define.armor_top_all,led2,led1,led1,define.effect_marquee)
                led.set_bottom_led(define.armor_bottom_all,led2,led1,led1,define.effect_flash)

                gimbal.rotate_with_degree(define.gimbal_down,randdown)

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
                    break

        blaster_fire_down()
            
    while True:    
        blaster_fire()

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''
