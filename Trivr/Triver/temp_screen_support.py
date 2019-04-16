#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 12, 2019 01:41:10 PM +0200  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def move(lap):
    if lap < 100:
        return 'w'
    elif 100 < lap <= 190:
        return 'd'
    elif 190 < lap <= 400:
        return 'w'
    #if 100 <= lap <2000:
      #  return 'a'
    #if 200 <= lap < 3000:
     #   return 's'
    return None

if __name__ == '__main__':
    import temp_screen
    temp_screen.vp_start_gui()




