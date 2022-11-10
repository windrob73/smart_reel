input.onButtonPressed(Button.A, function () {
    runtime += 500
    if (runtime == 10500) {
        runtime = 2000
    }
    basic.showNumber(runtime)
})
input.onButtonPressed(Button.B, function () {
    start = !(start)
})
let start = false
let runtime = 0
runtime = 1500
let stoptime = 2000
start = false
basic.forever(function () {
    while (start == true) {
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(runtime)
        basic.clearScreen()
        basic.pause(stoptime)
    }
})
