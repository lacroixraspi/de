input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    nombre = randint(0, 6)
    basic.showNumber(nombre)
    basic.pause(2000)
    basic.clearScreen()
    nombre = 0
})
let nombre = 0
basic.showString("Hello!")
