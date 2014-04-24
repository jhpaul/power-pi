import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
status = []
prev_input = 3
def ledCheck(prev_input):
    input = GPIO.input(15)
    if (prev_input != input) and (input == GPIO.HIGH):
#        print "LED OFF"
        return input
    if (prev_input != input) and (input == GPIO.LOW):
#        print "LED ON"
        return input
    prev_input = input
i = 0
while i < 5:
    status.append(ledCheck(prev_input))
    time.sleep(0.5)
    i = i+1
if sum(status) < 5 and sum(status) > 0:
    print "SYSTEM STANDBY"
if sum(status) == 0:
    print "SYSTEM ON"
if sum(status) == 5:
    print "SYSTEM OFF"

GPIO.cleanup()
