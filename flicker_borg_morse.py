#!/usr/bin/env python

import RPi.GPIO as gpio
import morse_talk as mtalk
import time
from random import seed, randint

FLICKER_PIN = 3

MESSAGE  = "Resistance is futile. Have a nice day."
SEQUENCE = mtalk.encode(MESSAGE, encoding_type = 'binary')
CHAR_NDX = -1

seed()

# -----------------------------------

gpio.setmode(gpio.BOARD)
gpio.setup(FLICKER_PIN, gpio.OUT)

def low():
  gpio.output(FLICKER_PIN, gpio.LOW)

def high():
  gpio.output(FLICKER_PIN, gpio.HIGH)

def nextChar():
  global CHAR_NDX
  CHAR_NDX += 1
  if (CHAR_NDX >= len(MESSAGE)):
    CHAR_NDX = 0
  return SEQUENCE[CHAR_NDX]

def flicker():
  if (nextChar() == "0"):
    low()
  else:
    high()

# -----------------------------------

while True:
  flicker()

  time.sleep(0.1)
