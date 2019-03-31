# -*- coding: utf-8 -*-
from Point import *
import math


def get_algebraic_vector_from_vector_and_angle(vector, target_length, angle):
    a1 = vector.point.x
    b1 = vector.point.y
    c1 = vector.end_point.x
    k = vector.end_point.y
    d = vector.length
    D = target_length
    T = d*D*math.cos(math.radians(angle)) #bDcos_a
    G = k*(k-b1)
    H = c1*(c1-a1)
    a = k - b1 + (a1**2 - 2*a1*c1 + c1**2)

    b = (2*k * (T-G-H-1)) - 2*b1(T-G-H) - 2*c1*(k*(a1-c1) - b1*(a1-c1))

    c = H**2 + G*(G+2*H) + T*(T-2*G-2*H) - 2*c1*(a1-c1)*(T-G-H) + (a1**2 - 2*a1*c1 + c1**2)*(k**2 + c1**2)


    print a
    print b
    print c
    a = 1
    y_solv = quadratic_equation(a, b, c)
    print y_solv


class Vector:
    def __init__(self, point, length, angle):
        self.length = length
        self.angle = angle
        self.point = point
        self.end_point = Point(self.point.x + math.cos(math.radians(self.angle))*self.length, self.point.y + math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = (self.end_point.x-self.point.x, self.end_point.y-self.point.y)
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
    p = Point(0, 0)
    v = Vector(p, 5, 45)
    print (v.__str__())
    print get_algebraic_vector_from_vector_and_angle(v, 2,135)

if __name__ == '__main__':
    main()