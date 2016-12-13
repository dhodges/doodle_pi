#!/usr/bin/env python

import time
import unicornhat as u

from random import randint


u.set_layout(u.PHAT)

def pixel(x,y,r,g,b):
    u.set_pixel(x,y,r,g,b)
    u.show()

def red(x, y):   pixel(x,y, 255, 0, 0)

def green(x,y):  pixel(x,y, 0, 255, 0)

def blue(x,y):   pixel(x,y, 0, 0, 255)

def white(x,y):  pixel(x,y, 255,255,255)

def blank(x,y,): pixel(x,y, 0,0,0)

def clear_all():
    u.clear()
    u.brightness(0.2)
    u.show()

def draw_xmas_tree():
    green(1,3)
    green(2,3)
    green(2,2)
    green(3,3)
    green(3,2)
    green(3,1)
    green(4,3)
    green(4,2)
    green(4,1)
    green(4,0)
    red(5,3)
    red(5,2)
    red(6,3)
    red(6,2)
    white(7,3)
    white(7,2)
    white(7,1)
    white(7,0)

class Snowflake:
    def __init__(self):
        self.x = 0
        self.y = randint(0, 3)
        self.last = u.get_pixel(self.x, self.y)

    def drop(self):
        u.set_pixel(self.x, self.y, self.last[0], self.last[1], self.last[2])
        self.x += 1
        self.last = u.get_pixel(self.x, self.y)
        u.set_pixel(self.x, self.y, 255, 255, 255)
        u.show()

class Snow:
    def __init__(self):
        self.flakes = []

    def loop(self):
        if randint(1, 4) == 4:
            self.flakes.append(Snowflake())
        for flake in self.flakes:
            flake.drop()
        self.flakes = [f for f in self.flakes if f.x <= 7]

clear_all()
draw_xmas_tree()

snow = Snow()

while True:
    snow.loop()
    time.sleep(0.5)
