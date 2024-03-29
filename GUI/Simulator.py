#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 17, 2019 02:55:11 PM +0300  platform: Windows NT

"""
Author: Yotam Levit
Project - VRI
"""

import sys
from Objects import Environment
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

from GUI import Simulator_support


def data_path(file_name):
    temp_path = sys.argv[0].split('/')
    temp_path.pop()
    temp_path.pop()
    path = temp_path.pop(0)
    for folder in temp_path:
        path += '/' + folder
    path += '/Data/' + file_name
    return path

def vp_start_gui(env, logic_file, path_log):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Simulator_support.set_Tk_var()
    top = Simulator (env, root)
    Simulator_support.init(root, top, logic_file , path_log)
    root.mainloop()

w = None
def create_Simulator(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Simulator_support.set_Tk_var()
    top = Simulator (w)
    Simulator_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Simulator():
    global w
    w.destroy()
    w = None

class Simulator:
    def __init__(self, env, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1230x1000")
        top.title("VRI - Virtual Robot Interactions")
        top.configure(background="#8aaae5")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.env = env
        self.lap = 0

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkDefaultFont",
                foreground="#000000",
                label="Start",
                command=lambda:self.start())
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkDefaultFont",
                foreground="#000000",
                label="Stop",
                command=lambda:self.stop())
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkDefaultFont",
                foreground="#000000",
                label="Save Current State",
                command=lambda:self.save())
        self.menubar.add_separator(
                background="#d9d9d9")
        self.menubar.add_separator(
                background="#d9d9d9")
        self.menubar.add_separator(
                background="#d9d9d9")
        self.menubar.add_separator(
                background="#d9d9d9")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkDefaultFont",
                foreground="#000000",
                label="Exit",
                command=lambda:Simulator_support.exit())

        self.canvas_sim = tk.Canvas(top)
        self.canvas_sim.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.813)
        self.canvas_sim.configure(background="#2e384c")
        self.canvas_sim.configure(borderwidth="2")
        self.canvas_sim.configure(highlightbackground="#d9d9d9")
        self.canvas_sim.configure(highlightcolor="black")
        self.canvas_sim.configure(insertbackground="black")
        self.canvas_sim.configure(relief="ridge")
        self.canvas_sim.configure(selectbackground="#c4c4c4")
        self.canvas_sim.configure(selectforeground="#000000")
        self.canvas_sim.configure(width=1000)

        self.speed_lable = tk.Label(top)
        self.speed_lable.place(relx=0.813, rely=0.0, height=25, width=61)
        self.speed_lable.configure(activebackground="#f9f9f9")
        self.speed_lable.configure(activeforeground="black")
        self.speed_lable.configure(background="#8aaae5")
        self.speed_lable.configure(disabledforeground="#a3a3a3")
        self.speed_lable.configure(font="-family {Arial} -size 13 -weight bold -underline 1")
        self.speed_lable.configure(foreground="#ffffff")
        self.speed_lable.configure(highlightbackground="#d9d9d9")
        self.speed_lable.configure(highlightcolor="black")
        self.speed_lable.configure(text='''Speed:''')

        self.spped_scale = ttk.Scale(top, from_=0, to=100)
        self.spped_scale.place(relx=0.862, rely=0.04, relwidth=0.0
                , relheight=0.12, width=26, bordermode='ignore')
        #self.spped_scale.configure(variable=Simulator_support.speed_value)
        self.spped_scale.configure(orient="vertical")
        self.spped_scale.configure(value="50")
        self.spped_scale.configure(length="120")
        self.spped_scale.configure(takefocus="")
        self.spped_scale.set(50)

        self.high_lable = tk.Label(top)
        self.high_lable.place(relx=0.829, rely=0.03, height=31, width=32)
        self.high_lable.configure(activebackground="#f9f9f9")
        self.high_lable.configure(activeforeground="black")
        self.high_lable.configure(background="#8aaae5")
        self.high_lable.configure(disabledforeground="#a3a3a3")
        self.high_lable.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.high_lable.configure(foreground="#ffffff")
        self.high_lable.configure(highlightbackground="#d9d9d9")
        self.high_lable.configure(highlightcolor="black")
        self.high_lable.configure(text='''High''')

        self.low_lable = tk.Label(top)
        self.low_lable.place(relx=0.829, rely=0.13, height=41, width=28)
        self.low_lable.configure(activebackground="#f9f9f9")
        self.low_lable.configure(activeforeground="black")
        self.low_lable.configure(background="#8aaae5")
        self.low_lable.configure(disabledforeground="#a3a3a3")
        self.low_lable.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.low_lable.configure(foreground="#ffffff")
        self.low_lable.configure(highlightbackground="#d9d9d9")
        self.low_lable.configure(highlightcolor="black")
        self.low_lable.configure(text='''Low''')
        self.low_lable.configure(width=28)

        self.crach_lable = tk.Label(top)
        self.crach_lable.place(relx=0.821, rely=0.24, height=121, width=214)
        self.crach_lable.configure(background="#8aaae5")
        self.crach_lable.configure(disabledforeground="#a3a3a3")
        self.crach_lable.configure(font="-family {Rockwell Nova Cond} -size 48 -weight bold -underline 1")
        self.crach_lable.configure(foreground="#ff0000")
        self.crach_lable.configure(highlightbackground="#ff0000")
        self.crach_lable.configure(highlightcolor="#ff0000")
        self.crach_lable.configure(width=214)

        self.state_lable = tk.Label(top)
        self.state_lable.place(relx=0.813, rely=0.2, height=25, width=57)
        self.state_lable.configure(background="#8aaae5")
        self.state_lable.configure(disabledforeground="#a3a3a3")
        self.state_lable.configure(font="-family {Arial} -size 13 -weight bold -underline 1")
        self.state_lable.configure(foreground="#ffffff")
        self.state_lable.configure(text='''State:''')
        self.state_lable.configure(width=57)

        self.crach_lable.configure(text='Stop')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.821, rely=0.24, relheight=0.12)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.992, rely=0.24, relheight=0.12)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.821, rely=0.24, relwidth=0.171)

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.821, rely=0.36, relwidth=0.171)

        self.bool_after = True
        self.env.draw(self.canvas_sim)

    def start(self):
        self.crach_lable.configure(text='Start')
        self.bool_after = True
        self.draw()

    def stop(self):
        if self.bool_after:
            self.crach_lable.configure(text='Stop')
            self.bool_after = False

    def crashed(self):
        self.crach_lable.configure(text='''Crashed''')
        self.bool_after = False

    def draw(self):
        #print(self.env.robot.shape)
        #print(self.env.robot.hit_box)
        #print(self.spped_scale.get())
        if self.env.check_crash():
            print ("crash")
            self.crashed()
            self.bool_after = False
        for sen in self.env.robot.ultrasonic:
            if sen is not None:
                sen.update_distance(self.env.objects, self.env.boundaries)
        if self.bool_after:
            action = Simulator_support.move(self.lap, self.env.robot)
            self.env.move_robot(action)
        self.canvas_sim.delete("all")
        for key, value in self.env.objects.items():
            value.draw(self.canvas_sim, 'green')
        self.lap += 1
        self.env.robot.draw(self.canvas_sim, 'black')
        for sen in self.env.robot.ultrasonic:
            if sen is not None:
                sen.draw(self.canvas_sim)
        if self.bool_after:
            self.top.after(int(self.spped_scale.get()),self.draw)

    def save(self):
        file_name = 'saved_state/Current_Status.xml'
        path = data_path(file_name)
        print(path)
        if os.path.isfile(path):
            index = 1
            while os.path.isfile(path):
                file_name = 'saved_state/Current_Status(' + str(index) + ').xml'
                path = data_path(file_name)
                index += 1
        self.env.convert_env_to_file(file_name)


if __name__ == '__main__':
    env = Environment.environment_from_file()
    vp_start_gui(env)





