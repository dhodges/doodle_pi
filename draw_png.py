#!/usr/bin/env python

import unicornhat as u

try:
  from PIL import Image
except ImportError:
  exit("PIL missing: run 'sudo pip install pillow'")


"draw the first 8x8 pixels of the given image"
def draw_png(filename, x=0, y=0):
  img = Image.open(filename)

  for imgX in range(8):
    for imgY in range(8):
      pixel = img.getpixel((imgY, imgX))
      print(pixel)
      r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
      u.set_pixel(x+imgX, y+imgY, r, g, b)

