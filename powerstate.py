import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
global state_pin
state_pin = 15

GPIO.setwarnings(False) ## Disable error messages from GPIO.cleanup
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(state_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def setprev(n):
    global prev_input
    prev_input = n

def ledCheck():
    input = GPIO.input(state_pin)
    prev = prev_input
    if (prev != input) and (input == GPIO.HIGH):
#        print "LED OFF"
        return input
    if (prev != input) and (input == GPIO.LOW):
#        print "LED ON"
        return input
    global prev_input
    setprev(input)
def status():
    status = []
    i = 0
    setprev(3)
    while i < 5:
        status.append(ledCheck())
        time.sleep(0.5)
        i = i+1
    if sum(status) < 5 and sum(status) > 0:
        return "SYSTEM STANDBY"
    if sum(status) == 0:
        return "SYSTEM ON"
    if sum(status) == 5:
        return "SYSTEM OFF"
print status()