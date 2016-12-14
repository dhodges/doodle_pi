#!/usr/bin/env python

import RPi.GPIO as gpio
import time
from random import seed, randint

seed()

# ------------------------------------

def lights_on(pin):
  gpio.output(pin, gpio.LOW)

def lights_off(pin):
  gpio.output(pin, gpio.HIGH)

# ------------------------------------
# two strings of LEDs

TREES   = {'name': "Trees",   'number':  3, 'state': False}
RAINBOW = {'name': "Rainbow", 'number': 19, 'state': False}

gpio.setmode(gpio.BOARD)

gpio.setup(TREES['number'],   gpio.OUT)
gpio.setup(RAINBOW['number'], gpio.OUT)

def cycle(leds):
  if leds['state']:
    lights_off(leds['number'])
  else:
    lights_on(leds['number'])
  leds['state'] = not leds['state']

# ------------------------------------

while True:
  if randint(1, 4) == 2:
    cycle(TREES)
  if randint(1, 4) == 2:
    cycle(RAINBOW)

  time.sleep(0.2)
