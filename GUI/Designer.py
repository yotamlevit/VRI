#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Jun 17, 2019 03:42:18 PM +0300  platform: Windows NT

"""
Author: Yotam Levit
Project - VRI
"""

import sys
import os
from Objects.Environment import Environment
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

from GUI import Designer_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Designer (root)
    Designer_support.init(root, top)
    root.mainloop()

w = None


def create_Designer(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Designer (w)
    Designer_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Designer():
    global w
    w.destroy()
    w = None


class Designer:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12 -weight bold -underline 1"  \
            ""

        top.geometry("1200x1000+450+0")
        top.title("VRI - Designer")
        top.configure(background="#45bfe8")

        self.env_canvas = tk.Canvas(top)
        self.env_canvas.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.833)
        self.env_canvas.configure(background="#2b3f77")
        self.env_canvas.configure(borderwidth="2")
        self.env_canvas.configure(insertbackground="black")
        self.env_canvas.configure(relief='ridge')
        self.env_canvas.configure(selectbackground="#c4c4c4")
        self.env_canvas.configure(selectforeground="black")
        self.env_canvas.configure(width=213)

        self.file_name = tk.Entry(top)
        self.file_name.place(relx=0.85, rely=0.18,height=20, relwidth=0.137)
        self.file_name.configure(background="white")
        self.file_name.configure(disabledforeground="#a3a3a3")
        self.file_name.configure(font="TkFixedFont")
        self.file_name.configure(foreground="#000000")
        self.file_name.configure(insertbackground="black")
        self.file_name.insert(0,'environment.xml')

        self.back = tk.Button(top)
        self.back.place(relx=0.85, rely=0.92, height=44, width=167)
        self.back.configure(activebackground="#ececec")
        self.back.configure(activeforeground="#000000")
        self.back.configure(background="#2b3f77")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(foreground="#000000")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="black")
        self.back.configure(pady="0")
        self.back.configure(font=font9)
        self.back.configure(foreground='#ffffff')
        self.back.configure(text='''Exit''')
        self.back.configure(width=167)
        self.back.bind('<Button-1>',lambda e:Designer_support.back())

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.842, rely=0.14, height=27, width=187)
        self.Label1.configure(background="#45bfe8")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Environment file name:''')

        self.ve = tk.Button(top)
        self.ve.place(relx=0.85, rely=0.22, height=44, width=167)
        self.ve.configure(activebackground="#ececec")
        self.ve.configure(activeforeground="#000000")
        self.ve.configure(background="#2b3f77")
        self.ve.configure(disabledforeground="#a3a3a3")
        self.ve.configure(foreground="#000000")
        self.ve.configure(highlightbackground="#d9d9d9")
        self.ve.configure(highlightcolor="black")
        self.ve.configure(pady="0")
        self.ve.configure(font=font9)
        self.ve.configure(foreground='#ffffff')
        self.ve.configure(text='''PreView''')
        self.ve.configure(width=167)
        self.ve.bind('<Button-1>',lambda e:self.view_env(self.file_name.get()))

    def view_env(self, env_file):
        """
        this function draws an environment from a givin file name
        """
        temp_path = sys.argv[0].split('/')
        temp_path.pop()
        temp_path.pop()
        path = temp_path.pop(0)
        for folder in temp_path:
            path += '/' + folder
        path_env = path + '/Data/' + env_file
        print(path_env)
        if os.path.isfile(path_env):
            env = Environment.environment_from_file(env_file)
            env.draw(self.env_canvas)
        else:
            self.Label1.configure(text="can't find file")

if __name__ == '__main__':
    vp_start_gui()





