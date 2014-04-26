#!/usr/bin/python2

import RPi.GPIO as GPIO ## Import GPIO library
# import time ## Import 'time' library. Allows us to use 'sleep'

def clean():
	GPIO.setwarnings(False) ## Disable error messages from GPIO.cleanup
	GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
	GPIO.cleanup
	print "Clean"

# clean()