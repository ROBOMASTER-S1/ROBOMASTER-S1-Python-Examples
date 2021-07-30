# Here is the Robomaster S1 Line Follower Python program
# example. I found this code on the dji Robomaster S1 app,
# via cell phone only; not from my PC. I hope this code works.
# I have aluminium bumpers on my Robomaster S1 and it
# does not work for me. However, I did try to tweak what I
# have here, I just hope it can work for others...

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
vision=vision_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

pid=rm_ctrl.PIDCtrl()

def start():
    robot.set_mode(define.robot_mode_chassis_follow)
    gimbal.rotate_with_degree(define.gimbal_down,20)
    vision.enable_detection(define.vision_detection_line)
    vision.line_follow_color_set(define.line_follow_color_blue)
    vision.set_marker_detection_distance(1)

    pid.set_ctrl_params(330,0,28)
    while True:
        LineList=RmList(vision_ctrl.get_line_detection_info())
        if len(LineList) == 42:
            if LineList[2] >= 1:
                robot_ctrl.set_mode(define.robot_mode_chassis_follow)
                variable_x = LineList[19]
                pid.set_error(variable_x - 0.5)
                gimbal.rotate_with_speed(pid.get_output(),0)
                chassis.set_trans_speed(.2)
                chassis.move(0)
