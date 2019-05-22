# -*- coding: utf-8 -*-
from Shape.Hit_Box import Hit_Box
from analytic_geometry.Point import Point
import sys

def find_edges(points):
    x_max = -1 * sys.maxsize
    y_max = -1 * sys.maxsize
    x_min = sys.maxsize
    y_min = sys.maxsize
    for point in points:
        if point.x > x_max:
            x_max = point.x
        if point.x < x_min:
            x_min = point.x
        if point.y > y_max:
            y_max = point.y
        if point.y < y_min:
            y_min = point.y
    return Point(x_min, y_min), Point(x_max, y_max)


class ObjectBuilder(object):
    def __init__(self, shape):
        self.shape = shape
        self.hit_box = Hit_Box(shape)

    def draw(self, canvas, color):
        self.shape.draw(canvas, color)

    def move_by_units(self, units):
        self.shape.move_by_units(units)
        self.hit_box = Hit_Box(self.shape)

    def rotate(self, value):
        self.shape.change_rotation(value)
        self.hit_box = Hit_Box(self.shape)

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()