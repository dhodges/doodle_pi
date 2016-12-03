#!/usr/bin/env python

import RPi.GPIO as gpio
import time
from random import seed, randint

OUTPUT_PIN = 11

# -----------------------------------

seed()

gpio.setmode(gpio.BOARD)
gpio.setup(OUTPUT_PIN, gpio.OUT)

def low():
  gpio.output(OUTPUT_PIN, gpio.LOW)

def high():
  gpio.output(OUTPUT_PIN, gpio.HIGH)

def flicker():
  if (randint(1, 10) % 2 == 0): #even
    low()
  else:
    high()

# -----------------------------------

while True:
  flicker()

  time.sleep(0.2)
