import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys ## Allows for CLI args
pin = 16
global pin
GPIO.setwarnings(False) ## Disable error messages from GPIO.cleanup
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(pin, GPIO.OUT) ## Setup GPIO Pin to OUT

# Turn on/off pin
def toggle():
    input = GPIO.input(pin)
    if (input == 1):
        GPIO.output(16,0)
        return "Light On"
    else:
        GPIO.output(16,1)
        return "Light Off"

# Check state of pin
def status():
    input = GPIO.input(pin)
    if input == 1:
        return "Light Off"
    if input == 0:
        return "Light On"

        
# define commandline options (none returns status)
def com(arg):
    if len(arg) > 1:
        if arg[1] in ("toggle","t"):
            return toggle(pin)
        if arg[1] in ("status", "s"):
            return status(pin)
    else:
        return status()

print com(sys.argv)
