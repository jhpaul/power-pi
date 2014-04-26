import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
power_pin = 11
global power_pin

GPIO.setwarnings(False) ## Disable error messages from GPIO.cleanup
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(power_pin, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

def short():
	GPIO.output(power_pin,0)
	time.sleep(0.5)
	GPIO.output(power_pin,1)
	return "Button Pressed for 1/2 Second"

def long():
	GPIO.output(power_pin,0)
	time.sleep(5)
	GPIO.output(power_pin,1)
	return "Button Pressed for 5 Second"

