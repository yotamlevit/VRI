#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Jun 17, 2019 03:42:26 PM +0300  platform: Windows NT

"""
Author: Yotam Levit
Project - VRI
"""

from GUI import Open_window_vri
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


def back():
    """
    opening the open screen
    """
    destroy_window()
    print('opening open screen')
    Open_window_vri.vp_start_gui()


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

if __name__ == '__main__':
    import Designer
    Designer.vp_start_gui()




