import machine, time

redLedPin = 15
yellowLedPin = 14
greenLedPin = 13

redLed = machine.Pin(redLedPin, machine.Pin.OUT)
yellowLed = machine.Pin(yellowLedPin, machine.Pin.OUT)
greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)