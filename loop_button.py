#!/usr/bin/env python

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN)

state = 0

while True:
  input = gpio.input(11)
  if input == state:
    continue

  state = input

  if state == 0:
    print('Button Pressed Off')
  else:
    print('Button Pressed On')

  time.sleep(0.2)
