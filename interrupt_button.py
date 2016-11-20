#!/usr/bin/env python

import RPi.GPIO as gpio

def loop():
  raw_input()

state = 0

def btn_press(pin):
  global state
  input = gpio.input(11)
  if state == input:
    return
  else:
    state = input

  if state == 1:
    print("button turned on")
  else:
    print("button turned off")

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN)
gpio.add_event_detect(11, gpio.RISING, callback=btn_press, bouncetime=200)

loop()

