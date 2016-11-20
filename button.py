#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  if GPIO.input(12) == False:
    print('Button Pressed')
  time.sleep(0.2)
