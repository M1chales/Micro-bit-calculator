def on_button_pressed_a():
    global Num
    Num += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    global Num
    Num = Num * 2
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_b():
    global Num
    Num += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_logo_down():
    global Num
    Num = Num / 2
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

Num = 0
Num = 5

def on_forever():
    basic.show_number(Num)
basic.forever(on_forever)
