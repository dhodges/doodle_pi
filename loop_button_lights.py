#!/usr/bin/env python

import RPi.GPIO as gpio
import time

button_state = 0

laser_pin    =  3
led_pin      = 21
button_pin   = 11

gpio.setmode(gpio.BOARD)

gpio.setup(laser_pin,  gpio.OUT)
gpio.setup(led_pin,    gpio.OUT)
gpio.setup(button_pin, gpio.IN)

# ------------------------------------

def laser_on():
  gpio.output(laser_pin, gpio.LOW)

def laser_off():
  gpio.output(laser_pin, gpio.HIGH)

def led_on():
  gpio.output(led_pin, gpio.LOW)

def led_off():
  gpio.output(led_pin, gpio.HIGH)

def print_button_state():
  if button_state == 0:
    print('Button Pressed Off')
  else:
    print('Button Pressed On')


def init():
  laser_off()
  led_on()

# ------------------------------------

init()

while True:
  input = gpio.input(button_pin)
  if input == button_state:
    continue

  button_state = input

  if button_state == 0:
    laser_off()
    led_on()
  else:
    led_off()
    laser_on()

  print_button_state()

  time.sleep(0.2)
