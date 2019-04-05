# -*- coding: utf-8 -*-
from Vector import *

class Wall:
    def __init__(self, x=0, y=0, vector_1=Vector(100,0), vector_2=Vector(100,270)):
        self.vector_1 = vector_1
        self.vector_2 = vector_2
        self.start_x = x
        self.start_y = y
        self.end_x = x + vector_1.length
        self.end_y = y + vector_2.length

    def change_size(self, width, height):
        self.width = width
        self.height = height

    def change_place(self, x, y):
        self.x = x
        self.y = y

    def show_data(self):
        print "Width: " + self.width.show_data() + " " + "height: " + self.height.show_data() + " " + "y: " + str(self.start_y) + " " + "x: " + str(self.start_x)


def main():
    """
    Add Documentation here
    """
    v = Vector(200,0)
    v2 = Vector(100, 270)
    w = Wall(100,100, v, v2)
    w.show_data()

if __name__ == '__main__':
    main()