led=led_ctrl
media=media_ctrl
define=rm_define
second,step=1,5
inc=255

def start():
    led.turn_off(define.armor_all)
    time.sleep(second)

    def rgb_red_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            i,0,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,0,0,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            i,0,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,0,0,define.effect_always_on)

    def rgb_yellow_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            i,i,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,i,0,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            i,i,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,i,0,define.effect_always_on)

    def rgb_blue_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            0,0,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,0,i,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            0,0,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,0,i,define.effect_always_on)

    def rgb_green_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            0,i,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,i,0,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            0,i,0,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,i,0,define.effect_always_on)

    def rgb_pink_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            i,0,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,0,i,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            i,0,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            i,0,i,define.effect_always_on)
        
    def rgb_cyan_dimmer():
        for i in range(0,inc,step):
            led.set_top_led(define.armor_top_all,
            0,i,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,i,i,define.effect_always_on)

        for i in range(inc,0,-step):
            led.set_top_led(define.armor_top_all,
            0,i,i,define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            0,i,i,define.effect_always_on)
            
        led.turn_off(define.armor_all)
        time.sleep(second)

    rgb_red_dimmer()
    rgb_yellow_dimmer()
    rgb_blue_dimmer()
    rgb_green_dimmer()
    rgb_pink_dimmer()
    rgb_cyan_dimmer()
