# Use these Robomaster S1 led looping templates in your next
# Robomaster S1 Python program.

robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

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

l1,l2,x,y=0,255,1,-1
delay1,delay2,seconds=.1,.2,1

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

# Function 1:
    def rgb_single_red_yellow_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 2:
    def rgb_single_blue_green_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 3:
    def rgb_single_pink_cyan_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# # Function 4:
    def rgb_single_red_yellow_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(8,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 5:
    def rgb_single_blue_green_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(8,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# # Function 6:
    def rgb_single_pink_cyan_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(8,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 7:
    def rgb_double_red_yellow_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 8:
    def rgb_double_blue_green_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 9:
    def rgb_double_pink_cyan_forward():
        while True:
            gun_led_on_off[x]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 10:
    def rgb_double_red_yellow_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(4,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 11:
    def rgb_double_blue_green_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(4,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 12:
    def rgb_double_pink_cyan_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(4,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[0])
                led.set_single_led(define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 13:
    def rgb_quad_Red_Yellow_foward_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(2,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])

                led.set_single_led(define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])

                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 14:
    def rgb_quad_blue_green_foward_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(2,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[0])

                led.set_single_led(define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])

                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 15:
    def rgb_quad_pink_cyan_foward_reverse():
        while True:
            gun_led_on_off[x]()
            for i in range(2,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[0])

                led.set_single_led(define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])

                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[1])
                time.sleep(delay1);gun_led_on_off[l1]()

# Function 16:
    def rgb_red_yellow_flipper():
        while True:
            gun_led_on_off[x]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[1])
            time.sleep(delay2)

            gun_led_on_off[l1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[1])
            time.sleep(delay2)

# Function 17:
    def rgb_blue_green_flipper():
        while True:
            gun_led_on_off[x]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[1])
            time.sleep(delay2)

            gun_led_on_off[l1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[1])
            time.sleep(delay2)

# Function 18:
    def rgb_pink_cyan_flipper():
        while True:
            gun_led_on_off[x]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[1])
            time.sleep(delay2)

            gun_led_on_off[l1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[0])
            led.set_single_led(define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[1])
            time.sleep(delay2)

# Function 19:
    def rgb_colour_changers_forward():
        gun_led_on_off[x]()
        while True:
            for i in range(x,8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(seconds)

# Function 20:
    def rgb_colour_changers_reverse():
        gun_led_on_off[x]()
        while True:
            for i in range(7,l1,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(seconds)

# Function 21:
    def rgb_flash_colour_changers():
        gun_led_on_off[x]()
        while True:
            gun_led_on_off[x]()
            for i in range(x,5):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay1)
            gun_led_on_off[l1]()

            for i in range(3,x,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay1)

# Function 22:
    def rgb_red_yellow_flasher():
        while True:
            gun_led_on_off[x]()
            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+2][0],RGB_COLOURS[i+2][1],RGB_COLOURS[i+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],RGB_COLOURS[i+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+1][0],RGB_COLOURS[i+3][1],RGB_COLOURS[i+2][2],define_effect[1])
                time.sleep(delay1)
            gun_led_on_off[l1]()

            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+1][0],RGB_COLOURS[i+1][1],RGB_COLOURS[i+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+1][0],RGB_COLOURS[i+2][1],RGB_COLOURS[i+2][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+3][0],RGB_COLOURS[i+2][1],RGB_COLOURS[i+2][2],define_effect[1])
                time.sleep(delay1)

# Function 23:
    def rgb_blue_green_flasher():
        while True:
            gun_led_on_off[x]()
            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+4][1],RGB_COLOURS[i+1][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+5][1],RGB_COLOURS[i+5][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+4][2],RGB_COLOURS[i+5][2],define_effect[1])
                time.sleep(delay1)
            gun_led_on_off[l1]()

            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+5][1],RGB_COLOURS[i+5][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+4][1],RGB_COLOURS[i+1][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+4][0],RGB_COLOURS[i+5][2],RGB_COLOURS[i+1][2],define_effect[1])
                time.sleep(delay1)

# Function 24:
    def rgb_pink_cyan_flasher():
        while True:
            gun_led_on_off[x]()
            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+6][0],RGB_COLOURS[i+6][1],RGB_COLOURS[i+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+5][0],RGB_COLOURS[i+5][1],RGB_COLOURS[i+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+5][0],RGB_COLOURS[i+5][1],RGB_COLOURS[i+6][2],define_effect[1])
                time.sleep(delay1)
            gun_led_on_off[l1]()

            for i in range(2):
                led_set_top_bottom[0](define_armor_top_right_left[i],
                RGB_COLOURS[i+5][0],RGB_COLOURS[i+5][1],RGB_COLOURS[i+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_right_left[i],
                RGB_COLOURS[i+6][0],RGB_COLOURS[i+6][1],RGB_COLOURS[i+6][2],define_effect[1])
                led_set_top_bottom[1](define_armor_bottom_front_back[i],
                RGB_COLOURS[i+3][0],RGB_COLOURS[i+6][1],RGB_COLOURS[i+6][2],define_effect[1])
                time.sleep(delay1)

# Function 25:
    def rgb_colour_trail_chasers_forward():
        while True:
            for i in range(x,8):
                gun_led_on_off[x]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(x,9):
                    led.set_single_led(define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay1)

                for j in range(x,9):
                    led.set_single_led(define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay1);gun_led_on_off[l1]()

# Function 26:
    def rgb_colour_trail_chasers_reverse():
        while True:
            for i in range(x,8):
                gun_led_on_off[x]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(8,l1,y):
                    led.set_single_led(define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay1)

                for j in range(8,l1,y):
                    led.set_single_led(define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay1);gun_led_on_off[l1]()

# Function 27:
    def rgb_white_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,i,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,i,define_effect[1])

# Function 28:
    def rgb_red_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,l1,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,l1,l1,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,l1,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,l1,l1,define_effect[1])

# Function 29:
    def rgb_yellow_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,l1,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,l1,define_effect[1])

# Function 30:
    def rgb_blue_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l1,i,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,l1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,l1,i,define_effect[1])

# Function 31:
    def rgb_green_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,i,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,i,l1,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,i,l1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,i,l1,define_effect[1])

# Function 32:
    def rgb_pink_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,l1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,l1,i,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,l1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,l1,i,define_effect[1])

# Function 33:
    def rgb_cyan_dimmer():
        while True:
            gun_led_on_off[x]()
            for i in range(l1,l2):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,i,i,define_effect[1])
            gun_led_on_off[l1]()

            for i in range(l2,y,y):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],l1,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],l1,i,i,define_effect[1])

# Store all 26 function callers inside a dictionary called funcs_dict{...}
# Note: do not invoke the function Parentheses () inside the dictionary.

    funcs_dict={
        1:rgb_single_red_yellow_forward,
        2:rgb_single_blue_green_forward,
        3:rgb_single_pink_cyan_forward,

        4:rgb_single_red_yellow_reverse,
        5:rgb_single_blue_green_reverse,
        6:rgb_single_pink_cyan_reverse,

        7:rgb_double_red_yellow_forward,
        8:rgb_double_blue_green_forward,
        9:rgb_double_pink_cyan_forward,

        10:rgb_double_red_yellow_reverse,
        11:rgb_double_blue_green_reverse,
        12:rgb_double_pink_cyan_reverse,

        13:rgb_quad_Red_Yellow_foward_reverse,
        14:rgb_quad_blue_green_foward_reverse,
        15:rgb_quad_pink_cyan_foward_reverse,

        16:rgb_red_yellow_flipper,
        17:rgb_blue_green_flipper,
        18:rgb_pink_cyan_flipper,

        19:rgb_colour_changers_forward,
        20:rgb_colour_changers_reverse,

        21:rgb_flash_colour_changers,

        22:rgb_red_yellow_flasher,
        23:rgb_blue_green_flasher,
        24:rgb_pink_cyan_flasher,

        25:rgb_colour_trail_chasers_forward,
        26:rgb_colour_trail_chasers_reverse,

        27:rgb_white_dimmer,
        28:rgb_red_dimmer,
        29:rgb_yellow_dimmer,
        30:rgb_blue_dimmer,
        31:rgb_green_dimmer,
        32:rgb_pink_dimmer,
        33:rgb_cyan_dimmer}

# From the funcs_dict functions dictionary above type
# a specified number, then execute/run the program.

# function caller parentheses () are invoked at the end of
# the dictionary's get value.

    funcs_dict.get(22)()
