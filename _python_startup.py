#!/usr/bin/env python

import time
import unicornhat as u
from draw_png import draw_png

try:
  from PIL import Image
except ImportError:
  exit("This script requires the pillow module\nInstall with: sudo pip install pillow")


u.set_layout(u.HAT)
u.rotation(0)
u.brightness(0.2)
