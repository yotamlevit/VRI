# -*- coding: utf-8 -*-
from Point import *
import math


class Vector:
    def __init__(self, length, angle):
        self.length = length
        if angle >= 360:
            angle -= 360
        self.angle = angle
        print self.angle
        temp = (math.cos(math.radians(self.angle))* self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def __str__(self):
        return 'length: {} , angle: {} , '.format(self.length, self.angle) + 'Way Vector ' + self.algebraic_vector.__repr__()

    def change_length(self, length):
        self.length = length

    def change_angle(self, angle):
        self.angle = angle
        temp = (math.cos(math.radians(self.angle))*self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def get_end_point(self, point):
        return Point(point.x + self.algebraic_vector.x, point.y + self.algebraic_vector.y)

    def skalar_mul_direction(self, uni):
        dirc = self.algebraic_vector.get_point()
        dirc = (dirc[0]/self.length, dirc[1]/self.length)
        return dirc[0]*uni, dirc[1]*uni




def main():
    """
    Add Documentation here
    """
    v = Vector(4, 60)
    print (v.__str__())

if __name__ == '__main__':
    main()