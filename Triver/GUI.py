import random
import time
from Tkinter import *

root = Tk()

w = Label(root, text="GAME")
w.pack()

frame = Frame(root, width=300, height=300)
frame.pack()

L1 = Label(root, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)


tiles_letter = ['a', 'b', 'c', 'd', 'e']


while len(tiles_letter) > 0:
    rand = random.choice(tiles_letter)
    tile_frame = Label(frame, text=rand)
    tile_frame.pack()
    frame.after(500)
    tiles_letter.remove(rand)  # remove that tile from list of tiles

root.mainloop()