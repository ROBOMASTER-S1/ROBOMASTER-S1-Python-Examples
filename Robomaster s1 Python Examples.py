# More future Robomaster s1 Python examples still to come.

while True:
    chassis_ctrl.set_wheel_speed(50,50,50,50)
    led_ctrl.set_top_led(rm_define.armor_top_right, 255, 0, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [1,3,5,7], rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_left, 0, 255, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_left, [1,3,5,7], rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 255, rm_define.effect_always_on)
    time.sleep(.095)

    led_ctrl.set_top_led(rm_define.armor_top_right, 0, 255, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [2,4,6,8], rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_left, 255, 0, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_left, [2,4,6,8], rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 255, rm_define.effect_always_on)
    time.sleep(.095)
