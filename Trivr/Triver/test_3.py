# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
"""
tree = ET.parse('environment.xml')
root = tree.getroot()
for ch in root:
    print(ch.tag, ch.attrib)
    for ch2 in ch:
        print(ch2.tag, ch2.attrib)
      """
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("vri_logo.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()


img = tk.PhotoImage(file="vri_logo.png")
        self.Logo = tk.Label(top, image=img)
        self.Logo.photo = img
        self.Logo.pack()
        self.Logo.place(relx=0.042, rely=0.053, height=140, width=480)
        self.Logo.configure(background="#2b3f77")

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()