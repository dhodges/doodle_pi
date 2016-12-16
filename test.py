#!/usr/bin/env python

import time
import unicornhat as u
from draw_png import draw_png
from sprite import Sprite

u.set_layout(u.HAT)
u.rotation(90)
u.brightness(0.8)
u.clear()

sprite1 = Sprite('sprites_8x8/invader_01a.png',
                 'sprites_8x8/invader_01b.png')

sprite3 = Sprite('sprites_8x8/invader_03a.png',
                 'sprites_8x8/invader_03b.png')

def scrollSprite(s):
  for x in range(0, 8, 1):
    s.draw(0, x)
    u.show()
    time.sleep(0.3)

while True:
  for s in [sprite1, sprite3]:
    scrollSprite(s)
    time.sleep(0.3)
