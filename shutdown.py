import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(5, GPIO.IN)

while True:
	if not (GPIO.input(5)):
		GPIO.output(7, False)
		time.sleep(.1)
		GPIO.output(7, True)
		time.sleep(.1)
		GPIO.output(7, False)
		time.sleep(.1)
		GPIO.output(7, True)

		os.system("sudo shutdown -h now")
		#print("shutdown")

	time.sleep(.5)
