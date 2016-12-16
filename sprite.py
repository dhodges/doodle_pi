#!/usr/bin/env python

import os
import unicornhat as u
from PIL import Image

class Sprite:

  def __init__(self, *args):
    self.images = []
    self.imageNdx = 0
    self._addImages(args)

  def _addImages(self, imageFilenames):
    for fname in imageFilenames:
      if not os.path.isfile(fname):
        raise Exception("%s does not exist" % fname)
      self.images.append(Image.open(fname))

  def _nextImage(self):
    if self.imageNdx >= len(self.images):
      self.imageNdx = 0
    img = self.images[self.imageNdx]
    self.imageNdx += 1
    return img

  def draw(self, x, y):
    img = self._nextImage()
    for imgX in range(8):
      for imgY in range(8):
        pixel = img.getpixel((imgY, imgX))
        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
        u.set_pixel(x+imgX, y+imgY, r, g, b)
