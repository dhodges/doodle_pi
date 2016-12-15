#!/usr/bin/env python

import time
import unicornhat as unicorn

# char_array should look something like:
# [
#   "  X  X  ",
#   "        ",
#   "X      X",
#   " XXXXXX ",
#   "        "
# ]


def draw_ascii(char_array, r, g, b):
  width  = len(char_array[0])
  height = len(char_array)

  for y in range(height):
    for x in range(width):
      chr = char_array[y][x]
      if chr == ' ':
        unicorn.set_pixel(x, y, 0, 0, 0)
      else:
        unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()


def draw_ascii_scrolling_left(char_array, r, g, b):
  for i in range(len(char_array[0])):
    draw_ascii(char_array, r, g, b)
    char_array = scroll_chars_left(char_array)
    time.sleep(0.3)


def scroll_chars_left(char_array):
  new_array = []
  for ndx in range(len(char_array)):
    new_array.append(char_array[ndx][1:] + ' ')
  return new_array


def scroll_chars_right(char_array):
  new_array = []
  for ndx in range(len(char_array)):
    new_array.append(' ' + char_array[ndx][:-1])
  return new_array


def add_char_arrays(char_array1, *args):
  new_array = []
  for ndx in range(len(char_array1)):
    line = char_array1[ndx]
    for arg in args:
      line += arg[ndx]
    new_array.append(line)
  return new_array

