#!/usr/bin/env python

import RPi.GPIO as gpio
import morse_talk as mtalk
import time
from random import seed, randint

seed()

BUTTON_STATE = 0

LASER     = 3
LED       = 5
BUTTON    = 7

MESSAGE   = "Resistance is futile. Have a nice day."
SEQUENCE  = mtalk.encode(MESSAGE, encoding_type = 'binary')
CHAR_NDX  = -1

gpio.setmode(gpio.BOARD)

gpio.setup(LED,    gpio.OUT)
gpio.setup(LASER,  gpio.OUT)
gpio.setup(BUTTON, gpio.IN)

# ------------------------------------

def laser_on():
  global LASER
  gpio.output(LASER, gpio.LOW)

def laser_off():
  global LASER
  gpio.output(LASER, gpio.HIGH)

def led_on():
  global LED
  gpio.output(LED, gpio.LOW)

def led_off():
  global LED
  gpio.output(LED, gpio.HIGH)

def nextChar():
  global MESSAGE, SEQUENCE, CHAR_NDX
  CHAR_NDX += 1
  if (CHAR_NDX >= len(MESSAGE)):
    CHAR_NDX = 0
  return SEQUENCE[CHAR_NDX]

def flicker_morse_led():
  if (nextChar() == "0"):
    led_off()
  else:
    led_on()

def toggle_laser():
  global BUTTON_STATE
  if BUTTON_STATE == 0:
    laser_off()
  else:
    laser_on()

def print_button_state():
  global BUTTON_STATE
  if BUTTON_STATE == 0:
    print('Button Pressed Off')
  else:
    print('Button Pressed On')


def init():
  laser_off()
  led_off()

# ------------------------------------

init()

while True:
  flicker_morse_led()

  input = gpio.input(BUTTON)
  if input != BUTTON_STATE:
    BUTTON_STATE = input
    toggle_laser()
    print_button_state()

  time.sleep(0.2)
