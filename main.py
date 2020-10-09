def on_button_pressed_a():
    basic.show_string("Hallo")
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("hi!")
basic.show_number(0)
basic.show_icon(IconNames.HEART)
basic.show_compass(500)

def on_forever():
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
