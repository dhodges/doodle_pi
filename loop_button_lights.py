#!/usr/bin/env python

import RPi.GPIO as gpio
import time

BUTTON_STATE = 0

LASER        =  3
LED          = 21
BUTTON       = 11

gpio.setmode(gpio.BOARD)

gpio.setup(LASER,  gpio.OUT)
gpio.setup(LED,    gpio.OUT)
gpio.setup(BUTTON, gpio.IN)

# ------------------------------------

def laser_on():
  gpio.output(LASER, gpio.LOW)

def laser_off():
  gpio.output(LASER, gpio.HIGH)

def led_on():
  gpio.output(LED, gpio.LOW)

def led_off():
  gpio.output(LED, gpio.HIGH)

def print_button_state():
  if BUTTON_STATE == 0:
    print('Button Pressed Off')
  else:
    print('Button Pressed On')


def init():
  laser_off()
  led_on()

# ------------------------------------

init()

while True:
  input = gpio.input(BUTTON)
  if input == BUTTON_STATE:
    continue

  BUTTON_STATE = input

  if BUTTON_STATE == 0:
    laser_off()
    led_on()
  else:
    led_off()
    laser_on()

  print_button_state()

  time.sleep(0.2)
