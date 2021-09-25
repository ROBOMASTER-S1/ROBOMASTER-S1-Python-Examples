# Robomaster S1 Python commands

# SYSTEM Python Commands:

robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

robot_ctrl.set_mode(rm_define.robot_mode_free)
'''----------------------------------------------------------------------------------------------------------------------'''
tools.timer_ctrl(rm_define.timer_start)

tools.timer_ctrl(rm_define.timer_stop)

tools.timer_ctrl(rm_define.timer_reset)
'''----------------------------------------------------------------------------------------------------------------------'''
# LED EFFECTS Python Commands:

led_ctrl.set_flash(rm_define.armor_all,2)

led_ctrl.set_flash(rm_define.armor_bottom_front,2)

led_ctrl.set_flash(rm_define.armor_bottom_back,2)

led_ctrl.set_flash(rm_define.armor_bottom_left,2)

led_ctrl.set_flash(rm_define.armor_bottom_right,2)

led_ctrl.set_flash(rm_define.armor_top_left,2)

led_ctrl.set_flash(rm_define.armor_top_right,2)
'''----------------------------------------------------------------------------------------------------------------------'''
led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_flash)
'''----------------------------------------------------------------------------------------------------------------------'''
led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_always_on)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_always_off)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_breath)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_flash)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_marquee)
'''----------------------------------------------------------------------------------------------------------------------'''
led_ctrl.set_single_led(rm_define.armor_top_all,1,rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_all,1,rm_define.effect_always_off)

led_ctrl.set_single_led(rm_define.armor_top_all,[1,3,5,7],rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_all,[1,3,5,7],rm_define.effect_always_off)

led_ctrl.set_single_led(rm_define.armor_top_left,[2,4,6,8],rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_left,[2,4,6,8],rm_define.effect_always_off)
'''----------------------------------------------------------------------------------------------------------------------'''
led_ctrl.turn_off(rm_define.armor_all)
'''----------------------------------------------------------------------------------------------------------------------'''
# Blaster Led on/off

led_ctrl.gun_led_on()

led_ctrl.gun_led_off()
'''----------------------------------------------------------------------------------------------------------------------'''
# CHASSIS Python Commands:

chassis_ctrl.set_pwm_value(rm_define.pwm_all,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm1,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm2,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm3,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm4,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm5,7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm6,7.5)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.enable_stick_overlay()

chassis_ctrl.disable_stick_overlay()
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.set_follow_gimbal_offset(0)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.set_trans_speed(0.5)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.set_rotate_speed(30)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.set_wheel_speed(100,100,100,100)
'''
chassis_ctrl.set_wheel_speed(
100, Front Left
100, Front Right
100, Back Left
100) Back Right
'''
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move(0)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move_with_time(0,1)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move_with_distance(0,1)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move_degree_with_speed(0.5,0)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.rotate(rm_define.clockwise)

chassis_ctrl.rotate(rm_define.anticlockwise)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.rotate_with_time(rm_define.clockwise,0)

chassis_ctrl.rotate_with_time(rm_define.anticlockwise,0)

chassis_ctrl.rotate_with_degree(rm_define.clockwise,0)

chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,0)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.rotate_with_speed(rm_define.clockwise,30)

chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,30)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move_and_rotate(0,rm_define.clockwise)

chassis_ctrl.move_and_rotate(0,rm_define.anticlockwise)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.move_with_speed(0.5,0.5,30)
'''----------------------------------------------------------------------------------------------------------------------'''
chassis_ctrl.stop()
'''----------------------------------------------------------------------------------------------------------------------'''
# GIMBAL Python Commands:

gimbal_ctrl.enable_stick_overlay()

gimbal_ctrl.disable_stick_overlay()
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.set_follow_chassis_offset(0)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.set_rotate_speed(30)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.recenter()

gimbal_ctrl.stop()

gimbal_ctrl.suspend()

gimbal_ctrl.resume()
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.rotate(rm_define.gimbal_up)

gimbal_ctrl.rotate(rm_define.gimbal_down)

gimbal_ctrl.rotate(rm_define.gimbal_left)

gimbal_ctrl.rotate(rm_define.gimbal_right)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,0)

gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,0)

gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,0)

gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,0)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.yaw_ctrl(0)

gimbal_ctrl.pitch_ctrl(0)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.angle_ctrl(0,0)
'''----------------------------------------------------------------------------------------------------------------------'''
gimbal_ctrl.rotate_with_speed(30,30)
'''----------------------------------------------------------------------------------------------------------------------'''
# Blaster Python Commands:

gun_ctrl.set_fire_count(1)
'''----------------------------------------------------------------------------------------------------------------------'''
gun_ctrl.fire_once()
'''----------------------------------------------------------------------------------------------------------------------'''
gun_ctrl.fire_continuous()
'''----------------------------------------------------------------------------------------------------------------------'''
gun_ctrl.stop()
'''----------------------------------------------------------------------------------------------------------------------'''
ir_blaster_ctrl.set_fire_count(1)
'''----------------------------------------------------------------------------------------------------------------------'''
ir_blaster_ctrl.fire_once()
'''----------------------------------------------------------------------------------------------------------------------'''
ir_blaster_ctrl.fire_continuous()
'''----------------------------------------------------------------------------------------------------------------------'''
ir_blaster_ctrl.stop()
'''----------------------------------------------------------------------------------------------------------------------'''
# SMART Python Commands:

vision_ctrl.enable_detection(rm_define.vision_detection_marker)

vision_ctrl.enable_detection(rm_define.vision_detection_pose)

vision_ctrl.enable_detection(rm_define.vision_detection_people)

vision_ctrl.enable_detection(rm_define.vision_detection_car)

vision_ctrl.disable_detection(rm_define.vision_detection_marker)

vision_ctrl.disable_detection(rm_define.vision_detection_pose)

vision_ctrl.disable_detection(rm_define.vision_detection_people)

vision_ctrl.disable_detection(rm_define.vision_detection_car)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.enable_detection(rm_define.vision_detection_line)

vision_ctrl.disable_detection(rm_define.vision_detection_line)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.set_marker_detection_distance(1)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)

vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_blue)

vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_green)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)

vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)

vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)

vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_target)

vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_dice)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_zero)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_four)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_five)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_six)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_seven)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_eight)

vision_ctrl.detect_marker_and_aim(rm_define.marker_number_nine)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_A)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_B)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_C)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_E)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_G)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_H)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_I)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_J)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_K)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_L)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_M)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_N)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_O)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Q)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_R)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_S)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_T)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_U)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_V)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_W)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_X)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Y)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Z)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)

media_ctrl.disable_sound_recognition(rm_define.sound_detection_applause)

media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)

media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_thrice)

media_ctrl.exposure_value_update(rm_define.exposure_value_large)

media_ctrl.exposure_value_update(rm_define.exposure_value_medium)

media_ctrl.exposure_value_update(rm_define.exposure_value_small)
'''----------------------------------------------------------------------------------------------------------------------'''
def vision_recognized_people(msg):
    pass

def vision_recognized_car(msg):
    pass

def vision_recognized_marker_trans_all(msg):
    pass

def vision_recognized_marker_trans_left(msg):
    pass

def vision_recognized_marker_trans_right(msg):
    pass

def vision_recognized_marker_trans_forward(msg):
    pass

def vision_recognized_marker_trans_stop(msg):
    pass

def vision_recognized_marker_trans_red_heart(msg):
    pass

def vision_recognized_marker_trans_target(msg):
    pass

def vision_recognized_marker_trans_dice(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def vision_recognized_marker_number_all(msg):
    pass

def vision_recognized_marker_number_zero(msg):
    pass

def vision_recognized_marker_number_one(msg):
    pass

def vision_recognized_marker_number_two(msg):
    pass

def vision_recognized_marker_number_three(msg):
    pass

def vision_recognized_marker_number_four(msg):
    pass

def vision_recognized_marker_number_five(msg):
    pass

def vision_recognized_marker_number_six(msg):
    pass

def vision_recognized_marker_number_seven(msg):
    pass

def vision_recognized_marker_number_eight(msg):
    pass

def vision_recognized_marker_number_nine(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def vision_recognized_marker_letter_all(msg):
    pass

def vision_recognized_marker_letter_A(msg):
    pass

def vision_recognized_marker_letter_B(msg):
    pass

def vision_recognized_marker_letter_C(msg):
    pass

def vision_recognized_marker_letter_D(msg):
    pass

def vision_recognized_marker_letter_E(msg):
    pass

def vision_recognized_marker_letter_F(msg):
    pass

def vision_recognized_marker_letter_G(msg):
    pass

def vision_recognized_marker_letter_H(msg):
    pass

def vision_recognized_marker_letter_I(msg):
    pass

def vision_recognized_marker_letter_J(msg):
    pass

def vision_recognized_marker_letter_K(msg):
    pass

def vision_recognized_marker_letter_L(msg):
    pass

def vision_recognized_marker_letter_M(msg):
    pass

def vision_recognized_marker_letter_N(msg):
    pass

def vision_recognized_marker_letter_O(msg):
    pass

def vision_recognized_marker_letter_P(msg):
    pass

def vision_recognized_marker_letter_Q(msg):
    pass

def vision_recognized_marker_letter_R(msg):
    pass

def vision_recognized_marker_letter_S(msg):
    pass

def vision_recognized_marker_letter_T(msg):
    pass

def vision_recognized_marker_letter_U(msg):
    pass

def vision_recognized_marker_letter_V(msg):
    pass

def vision_recognized_marker_letter_W(msg):
    pass

def vision_recognized_marker_letter_X(msg):
    pass

def vision_recognized_marker_letter_Y(msg):
    pass

def vision_recognized_marker_letter_Z(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def vision_recognized_pose_all(msg):
    pass

def vision_recognized_pose_victory(msg):
    pass

def vision_recognized_pose_give_in(msg):
    pass

def vision_recognized_pose_capture(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def sound_recognized_applause_twice(msg):
    pass

def sound_recognized_applause_thrice(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_people):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_car):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_all):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_left):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_right):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_forward):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_stop):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_red_heart):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_target):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_trans_dice):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_all):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_zero):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_four):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_five):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_six):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_seven):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_eight):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_nine):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_all):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_A):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_B):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_C):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_D):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_E):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_F):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_G):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_H):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_I):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_J):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_K):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_L):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_M):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_N):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_O):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_P):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_Q):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_R):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_S):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_T):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_U):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_V):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_W):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_X):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_Y):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_Z):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if vision_ctrl.check_condition(rm_define.cond_recognized_pose_victory):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_pose_give_in):
    pass

if vision_ctrl.check_condition(rm_define.cond_recognized_pose_capture):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
if media_ctrl.check_condition(rm_define.cond_sound_recognized_applause_twice):
        pass

if media_ctrl.check_condition(rm_define.cond_sound_recognized_applause_thrice):
        pass
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.cond_wait(rm_define.cond_recognized_people)

vision_ctrl.cond_wait(rm_define.cond_recognized_car)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_all)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_left)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_right)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_forward)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_stop)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_target)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_dice)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_all)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_zero)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_one)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_two)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_three)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_four)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_five)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_six)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_seven)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_eight)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_nine)
'''----------------------------------------------------------------------------------------------------------------------'''
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_all)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_A)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_B)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_C)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_D)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_E)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_F)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_G)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_H)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_I)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_J)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_K)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_L)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_M)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_N)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_O)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_P)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Q)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_R)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_S)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_T)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_U)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_V)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_W)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_X)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Y)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Z)
'''----------------------------------------------------------------------------------------------------------------------'''
# ARMOR Python Commands:

armor_ctrl.set_hit_sensitivity(5)
'''----------------------------------------------------------------------------------------------------------------------'''
if armor_ctrl.check_condition(rm_define.cond_armor_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_front_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_back_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_left_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_right_hit):
  pass
'''----------------------------------------------------------------------------------------------------------------------'''
if armor_ctrl.check_condition(rm_define.cond_armor_top_left_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_top_right_hit):
  pass
'''----------------------------------------------------------------------------------------------------------------------'''
if armor_ctrl.check_condition(rm_define.cond_ir_hit_detection):
  pass
'''----------------------------------------------------------------------------------------------------------------------'''
def armor_hit_detection_all(msg):
    pass

def armor_hit_detection_bottom_front(msg):
    pass

def armor_hit_detection_bottom_back(msg):
    pass

def armor_hit_detection_bottom_left(msg):
    pass

def armor_hit_detection_bottom_right(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def armor_hit_detection_top_left(msg):
    pass

def armor_hit_detection_top_right(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
def ir_hit_detection_event(msg):
    pass

'''----------------------------------------------------------------------------------------------------------------------'''
armor_ctrl.cond_wait(rm_define.cond_armor_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_front_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_left_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_right_hit)
'''----------------------------------------------------------------------------------------------------------------------'''
armor_ctrl.cond_wait(rm_define.cond_armor_top_left_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_top_right_hit)
'''----------------------------------------------------------------------------------------------------------------------'''
armor_ctrl.cond_wait(rm_define.cond_ir_hit_detection)
'''----------------------------------------------------------------------------------------------------------------------'''
# SENSOR Python Commands:

ir_distance_sensor_ctrl.enable_measure(1)

ir_distance_sensor_ctrl.disable_measure(1)
'''----------------------------------------------------------------------------------------------------------------------'''
def ir_distance_1_ge_10_event(msg):
    pass

def ir_distance_1_le_10_event(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
ir_distance_sensor_ctrl.cond_wait("ir_distance_1_ge_10")

ir_distance_sensor_ctrl.cond_wait("ir_distance_1_le_10")
'''----------------------------------------------------------------------------------------------------------------------'''
# SENSOR ADAPTER Python Commands:

sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter1_port1_low_event)

sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter1_port1_high_event)

def sensor_adapter1_port1_high_event(msg):
    pass

def sensor_adapter1_port1_low_event(msg):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# MEDIA Python Commands:

media_ctrl.play_sound(rm_define.media_sound_solmization_1C)

media_ctrl.play_sound(rm_define.media_sound_solmization_1D)

media_ctrl.play_sound(rm_define.media_sound_solmization_1E)

media_ctrl.play_sound(rm_define.media_sound_solmization_1F)

media_ctrl.play_sound(rm_define.media_sound_solmization_1G)

media_ctrl.play_sound(rm_define.media_sound_solmization_1A)

media_ctrl.play_sound(rm_define.media_sound_solmization_1B)

media_ctrl.play_sound(rm_define.media_sound_solmization_2C)

media_ctrl.play_sound(rm_define.media_sound_solmization_2D)

media_ctrl.play_sound(rm_define.media_sound_solmization_2E)

media_ctrl.play_sound(rm_define.media_sound_solmization_2F)

media_ctrl.play_sound(rm_define.media_sound_solmization_2G)

media_ctrl.play_sound(rm_define.media_sound_solmization_2A)

media_ctrl.play_sound(rm_define.media_sound_solmization_2B)

media_ctrl.play_sound(rm_define.media_sound_solmization_3C)

media_ctrl.play_sound(rm_define.media_sound_solmization_3D)

media_ctrl.play_sound(rm_define.media_sound_solmization_3E)

media_ctrl.play_sound(rm_define.media_sound_solmization_3F)

media_ctrl.play_sound(rm_define.media_sound_solmization_3G)

media_ctrl.play_sound(rm_define.media_sound_solmization_3A)

media_ctrl.play_sound(rm_define.media_sound_solmization_3B)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.play_sound(rm_define.media_sound_attacked)

media_ctrl.play_sound(rm_define.media_sound_shoot)

media_ctrl.play_sound(rm_define.media_sound_scanning)

media_ctrl.play_sound(rm_define.media_sound_recognize_success)

media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)

media_ctrl.play_sound(rm_define.media_sound_count_down)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.play_sound(rm_define.media_sound_attacked,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_shoot,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_scanning,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_recognize_success,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_count_down,wait_for_complete_flag=True)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

media_ctrl.play_sound(rm_define.media_custom_audio_undefined,wait_for_complete_flag=True)
'''----------------------------------------------------------------------------------------------------------------------'''
# Music Note Python Commands:

media_ctrl.play_sound(rm_define.media_sound_solmization_3B)

media_ctrl.play_sound(rm_define.media_sound_solmization_3A)

media_ctrl.play_sound(rm_define.media_sound_solmization_3G)

media_ctrl.play_sound(rm_define.media_sound_solmization_3F)

media_ctrl.play_sound(rm_define.media_sound_solmization_3E)

media_ctrl.play_sound(rm_define.media_sound_solmization_3D)

media_ctrl.play_sound(rm_define.media_sound_solmization_3C)

media_ctrl.play_sound(rm_define.media_sound_solmization_2B)

media_ctrl.play_sound(rm_define.media_sound_solmization_2A)

media_ctrl.play_sound(rm_define.media_sound_solmization_2G)

media_ctrl.play_sound(rm_define.media_sound_solmization_2F)

media_ctrl.play_sound(rm_define.media_sound_solmization_2E)

media_ctrl.play_sound(rm_define.media_sound_solmization_2D)

media_ctrl.play_sound(rm_define.media_sound_solmization_2C)

media_ctrl.play_sound(rm_define.media_sound_solmization_1B)

media_ctrl.play_sound(rm_define.media_sound_solmization_1A)

media_ctrl.play_sound(rm_define.media_sound_solmization_1G)

media_ctrl.play_sound(rm_define.media_sound_solmization_1F)

media_ctrl.play_sound(rm_define.media_sound_solmization_1E)

media_ctrl.play_sound(rm_define.media_sound_solmization_1D)

media_ctrl.play_sound(rm_define.media_sound_solmization_1C)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.play_sound(rm_define.media_sound_solmization_3ASharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_3GSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_3FSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_3DSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_3CSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_2ASharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_2GSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_2FSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_2DSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_2CSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_1ASharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_1GSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_1FSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_1DSharp)

media_ctrl.play_sound(rm_define.media_sound_solmization_1CSharp)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.capture()
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.zoom_value_update(1)

media_ctrl.zoom_value_update(2)

media_ctrl.zoom_value_update(3)

media_ctrl.zoom_value_update(4)
'''----------------------------------------------------------------------------------------------------------------------'''
media_ctrl.record(1)

media_ctrl.record(0)
'''----------------------------------------------------------------------------------------------------------------------'''
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

blaster=ir_blaster_ctrl

gun=gun_ctrl

led=led_ctrl

armor=armor_ctrl

vision=vision_ctrl

media=media_ctrl

distance=ir_distance_sensor_ctrl

sensor=sensor_adapter_ctrl

define=rm_define
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic time.sleep() function

time.sleep(1)
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic for-loop function

for count in range(10):
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic while-loop

while True:
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic if True/False statements:

if True:
    pass

if False:
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic if else True/False statements:

if True:
    pass
else:
    pass

if False:
    pass
else:
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic while not False statement:

while not False:
    pass
'''----------------------------------------------------------------------------------------------------------------------'''
# Robomaster S1 exit() function:

rmexit()
'''----------------------------------------------------------------------------------------------------------------------'''
# Basic user defined function():

def user_defined_new_func1():
    pass
