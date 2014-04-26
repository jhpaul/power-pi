import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys ## Allows for CLI args
global light_pin
light_pin = 16
GPIO.setwarnings(False) ## Disable error messages from GPIO.cleanup
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(light_pin, GPIO.OUT) ## Setup GPIO light_pin to OUT

# Turn on/off light_pin
def toggle():
    input = GPIO.input(light_pin)
    if (input == 1):
        GPIO.output(light_pin,0)
        return "LIGHT ON"
    else:
        GPIO.output(light_pin,1)
        return "LIGHT OFF"

# Check state of light_pin
def status():
    input = GPIO.input(light_pin)
    if input == 1:
        return "LIGHT OFF"
    if input == 0:
        return "LIGHT ON"

        
# define commandline options (none returns status)
def com(arg):
    if len(arg) > 1:
        if arg[1] in ("toggle","t"):
            return toggle()
        if arg[1] in ("status", "s"):
            return status()
    else:
        return status()

print com(sys.argv)
