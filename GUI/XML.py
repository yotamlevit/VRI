#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Jun 13, 2019 02:13:55 PM +0300  platform: Windows NT

import sys
import os
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

from GUI import XML_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    XML_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    XML_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+815+198")
        top.title("VRI - XML")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.017, rely=0.067, height=41, width=184)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Historic} -size 14 -weight bold -underline 1")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''XML''')
        self.Label1.configure(width=184)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.033, rely=0.244, height=51, width=534)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''To pass values put the value between the opening and the close of the argumentfor example:''')
        self.Label2.configure(width=534)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.067, rely=0.222, height=21, width=192)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''The xml foramt is tag based written''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.333, rely=0.356, height=21, width=175)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''<argument>value</argument>''')

        self.Back = tk.Button(top)
        self.Back.place(relx=0.067, rely=0.756, height=44, width=107)
        self.Back.configure(activebackground="#d9d9d9")
        self.Back.configure(activeforeground="#000000")
        self.Back.configure(background="#d9d9d9")
        self.Back.configure(disabledforeground="#a3a3a3")
        self.Back.configure(foreground="#000000")
        self.Back.configure(highlightbackground="#d9d9d9")
        self.Back.configure(highlightcolor="black")
        self.Back.configure(pady="0")
        self.Back.configure(text='''Back''')
        self.Back.configure(width=107)
        self.Back.bind('<Button-1>',lambda e:XML_support.back())

        self.open_file = tk.Button(top)
        self.open_file.place(relx=0.55, rely=0.756, height=44, width=247)
        self.open_file.configure(activebackground="#d9d9d9")
        self.open_file.configure(activeforeground="#000000")
        self.open_file.configure(background="#d9d9d9")
        self.open_file.configure(disabledforeground="#a3a3a3")
        self.open_file.configure(foreground="#000000")
        self.open_file.configure(highlightbackground="#d9d9d9")
        self.open_file.configure(highlightcolor="black")
        self.open_file.configure(pady="0")
        self.open_file.configure(text='''Open environment example and base file''')
        self.open_file.configure(width=247)
        self.open_file.bind('<Button-1>',lambda e:self.open_file_pressed())

    def open_file_pressed(self):
        temp_path = sys.argv[0].split('/')
        temp_path.pop()
        temp_path.pop()
        path = temp_path.pop(0)
        for folder in temp_path:
            path += '/' + folder
        path_env = path + '/Data/environment.xml'
        osCommandString = "notepad.exe " + path_env
        os.system(osCommandString)

if __name__ == '__main__':
    vp_start_gui()





