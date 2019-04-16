# -*- coding: utf-8 -*-
from Point import *
import math

"""
def get_algebraic_vector_from_vector_and_angle(vector, target_length, angle):
    a1 = float(vector.point.x)
    b1 = float(vector.point.y)
    c1 = float(vector.end_point.x)
    k = float(vector.end_point.y)
    d = float(vector.length)
    D = float(target_length)
    T = d*D*math.cos(math.radians(angle)) #bDcos_a
    G = k*(k-b1)
    H = c1*(c1-a1)
    print type(c1)
    a = k - b1 + (a1**2 - 2*a1*c1 + c1**2)

    b = (2*k * (T-G-H-1)) - 2*b1*(T-G-H) - 2*c1*(k*(a1-c1) - b1*(a1-c1))

    c = H**2 + G*(G+2*H) + T*(T-2*G-2*H) - 2*c1*(a1-c1)*(T-G-H) + (a1**2 - 2*a1*c1 + c1**2)*(k**2 + c1**2)


    print a
    print b
    print c
    a = 1
    y_solv = quadratic_equation(a, b, c)
    print y_solv
"""


class Vector:
    def __init__(self, length, angle):
        self.length = length
        if angle >= 360:
            angle -= 360
        self.angle = angle
        temp = (math.cos(math.radians(self.angle))*self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def __str__(self):
        return 'length: {} , angle: {} , '.format(self.length, self.angle) + 'Way Vector ' + self.algebraic_vector.__repr__()

    def change_length(self, length):
        self.length = length
        temp = (math.cos(math.radians(self.angle))*self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def change_angle(self, angle):
        self.angle = angle
        if self.angle >= 360:
            self.angle -= 360
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