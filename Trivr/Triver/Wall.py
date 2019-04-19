# -*- coding: utf-8 -*-
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
import math
from Parallelogram import Parallelogram
from Hit_Box import Hit_Box
import sys
from Object_Builder import ObjectBuilder

class Wall(ObjectBuilder):
    def __init__(self, shape):
        super(Wall, self).__init__(shape)

    def convert_obj_to_txt(self):
        return '<Wall>' + self.shape.convert_shape_to_txt() + '</Wall>'

def main():
    """
    Add Documentation here
    """
    v = Vector(5, 0)
    p = Point(200, 200)
    line = StraightLine(p, v)
    p = Parallelogram(line, 120, 5)
    w = Wall(p)
    print (w.shape.get_points())
    print (w.shape.get_equation())
    print (w.__str__())

if __name__ == '__main__':
    main()