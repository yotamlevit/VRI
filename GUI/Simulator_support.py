#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 17, 2019 02:52:22 PM +0300  platform: Windows NT

from GUI import Open_window_vri
import importlib.util
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

def set_Tk_var():
    global speed_value
    speed_value = tk.DoubleVar()

def init(top, gui, logic_file , path_log , *args, **kwargs):
    global w, top_level, root
    global spec
    spec = importlib.util.spec_from_file_location(logic_file, path_log)
    global logic
    logic = importlib.util.module_from_spec(spec)

    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def exit():
    destroy_window()
    print('opening Open Screen')
    Open_window_vri.vp_start_gui()

def move(lap, robot):
    spec.loader.exec_module(logic)
    return logic.logic(lap, robot)
    #return sys.path[len(sys.path)-1].logic(lap)

if __name__ == '__main__':
    from GUI import Simulator
    Simulator.vp_start_gui()




