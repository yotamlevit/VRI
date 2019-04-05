# -*- coding: utf-8 -*-
import Point


class Vector:
    def __init__(self, point, length, angle):
        self.length = length
        self.angle = angle
        self.point = point

    def __str__(self):
        return 'length: {} , angle: {} , '.format(self.length, self.angle) + 'Start ' + self.point.__repr__()

    def change_length(self, length):
        self.length = length

    def change_angle(self, angle):
        self.angle = angle

    def change_pos(self, point):
        self.poinbt = point

def main():
    """
    Add Documentation here
    """
    p = Point(100, 100)
    v = Vector(p, 200, 0)
    print v.__str__()

if __name__ == '__main__':
    main()