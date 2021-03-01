led=led_ctrl
media=media_ctrl
define=rm_define
blink_rate=4
l1,l2=0,55
second,delay=1,.1

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
    [l2,l1,l2], # RGB Pink
    [l1,l2,l2], # RGB Cyan
    ]

RGB2=[
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
    
led.set_flash(define.armor_all,blink_rate)
led.turn_off(define.armor_all)
time.sleep(second)

def start():
    def rgb_colour_trail_forward():
        for i in range(1,7):
            led.set_top_led(define.armor_top_all,
            RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)

            led.set_bottom_led(define.armor_bottom_all,
            RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_flash)

            for i in range(1,9):
                led.gun_led_on()
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_on)
                time.sleep(delay)

            for i in range(1,9):
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_off)
                time.sleep(delay)
                led.gun_led_off()
                
    def rgb_colour_trail_reverse():
        for i in range(1,7):
            led.set_top_led(define.armor_top_all,
            RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_always_off)

            led.set_bottom_led(define.armor_bottom_all,
            RGB1[i][0],RGB1[i][1],RGB1[i][2],define.effect_flash)

            for i in range(8,0,-1):
                led.gun_led_on()
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_on)
                time.sleep(delay)

            for i in range(8,0,-1):
                led.set_single_led(define.armor_top_all,
                [i],define.effect_always_off)
                time.sleep(delay)
                led.gun_led_off()
                
    def rgb_single_colour_chasers_forward():        
        led_ctrl.gun_led_on()
        for i in range(1,9):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(delay)
            led_ctrl.gun_led_off()          

    def rgb_single_colour_chasers_reverse():        
        led_ctrl.gun_led_on()            
        for i in range(8,0,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
            time.sleep(delay)
            led_ctrl.gun_led_off()

    def rgb_double_colour_chasers_forward():
        x=0
        while x<=1:   
            led_ctrl.gun_led_on()
            for i in range(1,5):
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+4],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
                time.sleep(delay)
                led_ctrl.gun_led_off()
            x+=1

    def rgb_double_colour_chasers_reverse():
        x=0
        while x<=1:         
            led_ctrl.gun_led_on()
            for i in range(4,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+4],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB2[-i][0],RGB2[-i][1],RGB2[-i][2],define.effect_always_on)
                time.sleep(delay)
                led_ctrl.gun_led_off()
            x+=1

    def rgb_quad_colour_chasers_forward():
        x=0
        while x<=2:        
            led_ctrl.gun_led_on()
            for i in range(1,3):
                led.set_top_led(define.armor_top_all,
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+2,i+4,i+6],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB_RY[-i][0],RGB_RY[-i][1],RGB_RY[-i][2],define.effect_always_on)
                time.sleep(delay)
                led_ctrl.gun_led_off()
            x+=1

    def rgb_quad_colour_chasers_reverse():
        x=0
        while x<=2:
            led_ctrl.gun_led_on()
            for i in range(2,0,-1):
                led.set_top_led(define.armor_top_all,
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define.effect_always_off)
                led.set_single_led(define.armor_top_all,
                [i,i+2,i+4,i+6],define.effect_always_on)

                led.set_bottom_led(define.armor_bottom_all,
                RGB_RY[-i][0],RGB_RY[-i][1],RGB_RY[-i][2],define.effect_always_on)
                time.sleep(delay)
                led_ctrl.gun_led_off()
            x+=1

    def rgb_flash_colour_changers():
        led_ctrl.gun_led_on()
        for i in range(1,5):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
            time.sleep(delay)

        led_ctrl.gun_led_off()
        for i in range(3,1,-1):
            led.set_top_led(define.armor_top_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB2[i][0],RGB2[i][1],RGB2[i][2],define.effect_always_on)
            time.sleep(delay)
    
    while True:
        rgb_colour_trail_forward()
        rgb_single_colour_chasers_forward()
        rgb_double_colour_chasers_forward()
        rgb_quad_colour_chasers_forward()
        rgb_flash_colour_changers()
        rgb_quad_colour_chasers_reverse()
        rgb_double_colour_chasers_reverse()
        rgb_single_colour_chasers_reverse()
        rgb_colour_trail_reverse()
