# -*- coding: utf-8 -*-
from Parallelogram import Parallelogram
from Hit_Box import Hit_Box
from Point import Point
import sys

def find_edges(points):
    x_max = -1 * sys.maxint
    y_max = -1 * sys.maxint
    x_min = sys.maxint
    y_min = sys.maxint
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
        if type(self.shape) == Parallelogram:
            edge_points = find_edges(self.shape.get_points())
            self.hit_box = Hit_Box(edge_points[0], edge_points[1])

    def draw(self, canvas, color):
        self.shape.draw(canvas, color)

    def move_by_units(self, units):
        self.shape.move_by_units(units)

    def rotate(self, value):
        self.shape.change_rotation_by_value(value)

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()