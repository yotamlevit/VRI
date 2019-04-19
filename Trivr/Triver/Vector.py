# -*- coding: utf-8 -*-
from Point import *
import math

TAB = '    '

class Vector:
    def __init__(self, length, angle):
        """
        this class describes a polar vector with it's way-vector as algebraic description
        ;length: the vector's length
        ;angle: the vector's angle from the positive side of the x and y
        """
        self.length = length
        if angle >= 360:
            angle -= 360
        self.angle = angle
        if self.angle == 90 or self.angle == 270:
            temp = (0,math.sin(math.radians(self.angle))*self.length)
        elif self.angle == 180:
            temp = (math.cos(math.radians(self.angle))* self.length,0)
        else:
            temp = (math.cos(math.radians(self.angle))* self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def __str__(self):
        """
        describes the vector in words
        ;return: a string that contains all the information on the vector
        """
        return 'length: {} , angle: {} , '.format(self.length, self.angle) + 'Way Vector ' + self.algebraic_vector.__repr__()

    def change_length(self, length):
        """
        this function changes the vector's length and update the vector's argument
        ;length: the new length
        """
        self.length = length
        if self.angle == 90 or self.angle == 270:
            temp = (0,math.sin(math.radians(self.angle))*self.length)
        elif self.angle == 180:
            temp = (math.cos(math.radians(self.angle))* self.length,0)
        else:
            temp = (math.cos(math.radians(self.angle))* self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def change_angle(self, angle):
        """
        this function changes the vector's angle and update the vector's argument
        ;angle: the new angle
        """
        self.angle = angle
        if self.angle == 90 or self.angle == 270:
            temp = (0,math.sin(math.radians(self.angle))*self.length)
        elif self.angle == 180:
            temp = (math.cos(math.radians(self.angle))* self.length,0)
        else:
            temp = (math.cos(math.radians(self.angle))* self.length,math.sin(math.radians(self.angle))*self.length)
        self.algebraic_vector = Point(temp[0], temp[1])

    def get_end_point(self, point):
        return Point(point.x + self.algebraic_vector.x, point.y + self.algebraic_vector.y)

    def skalar_mul_direction(self, uni):
        dirc = self.algebraic_vector.get_point()
        dirc = (dirc[0]/self.length, dirc[1]/self.length)
        return dirc[0]*uni, dirc[1]*uni


    def convert_vector_to_txt(self):
        return '<Vector><length>' + str(self.length) + '</length><angle>' + str(self.angle) + '</angle>'

def main():
    """
    Add Documentation here
    """
    v = Vector(4, 90)
    print(v.algebraic_vector)
    v.change_angle(91)
    print (v.__str__())

if __name__ == '__main__':
    main()