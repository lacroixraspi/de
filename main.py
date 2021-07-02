def on_gesture_shake():
    global nombre
    nombre = randint(0, 6)
    basic.show_number(nombre)
    basic.pause(2000)
    basic.clear_screen()
    nombre = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

nombre = 0
basic.show_string("Hello!")