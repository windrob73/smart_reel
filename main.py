def on_button_pressed_a():
    global runtime
    runtime += 500
    if runtime == 10500:
        runtime = 2000
    basic.show_number(runtime)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start
    start = not (start)
input.on_button_pressed(Button.B, on_button_pressed_b)

start = False
runtime = 0
runtime = 2000
stoptime = 2000
start = False

def on_forever():
    while start == True:
        basic.show_leds("""
            . . . . .
                        . . # . .
                        . # # # .
                        . . # . .
                        . . . . .
        """)
        basic.pause(runtime)
        basic.clear_screen()
        basic.pause(stoptime)
basic.forever(on_forever)
