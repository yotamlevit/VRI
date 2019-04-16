# -*- coding: utf-8 -*-
from Point import Point
from Vector import Vector
# todo update func
class StraightLine:

    def __init__(self, point, vector):
        self.start_point = point
        self.vector = vector
        self.end_point = self.vector.get_end_point(self.start_point)
        self.b = self.start_point.y_int(self.end_point)
        self.fc = self.start_point.line_function(self.end_point)
        #if self.b is not None:
        self.equ = self.start_point.line_equation(self.end_point)
        self.m = self.start_point.slope(self.end_point)
        if self.start_point.x > self.end_point.x:
            self.min_x = self.end_point.x
            self.max_x = self.start_point.x
        else:
            self.min_x = self.start_point.x
            self.max_x = self.end_point.x

    def __str__(self):
        return '(Vector: {}, Start Point: {}, End Point: {}, Vector Function: {})'.format(self.vector, self.start_point, self.end_point, self.equ)

    def __repr__(self):
        return '(Vector: {}, Start Point: {}, End Point: {}, Vector Function: {})'.format(self.vector, self.start_point, self.end_point, self.equ)

    def change_length(self, length):
        self.vector.change_length(length)
        self.end_point = self.vector.get_end_point(self.start_point)
        self.b = self.start_point.y_int(self.end_point)
        self.fc = self.start_point.line_function(self.end_point)
        self.equ = self.start_point.line_equation(self.end_point)
        self.m = self.start_point.slope(self.end_point)
        if self.start_point.x > self.end_point.x:
            self.min_x = self.end_point.x
            self.max_x = self.start_point.x
        else:
            self.min_x = self.start_point.x
            self.max_x = self.end_point.x

    def change_pos(self, point):
        self.start_point = point
        self.end_point = self.vector.get_end_point(self.start_point)
        self.b = self.start_point.y_int(self.end_point)
        self.fc = self.start_point.line_function(self.end_point)
        self.equ = self.start_point.line_equation(self.end_point)
        self.m = self.start_point.slope(self.end_point)
        if self.start_point.x > self.end_point.x:
            self.min_x = self.end_point.x
            self.max_x = self.start_point.x
        else:
            self.min_x = self.start_point.x
            self.max_x = self.end_point.x

    def change_angle(self, angle):
        self.vector.change_angle(angle)
        self.end_point = self.vector.get_end_point(self.start_point)
        self.b = self.start_point.y_int(self.end_point)
        self.fc = self.start_point.line_function(self.end_point)
        self.equ = self.start_point.line_equation(self.end_point)
        self.m = self.start_point.slope(self.end_point)
        if self.start_point.x > self.end_point.x:
            self.min_x = self.end_point.x
            self.max_x = self.start_point.x
        else:
            self.min_x = self.start_point.x
            self.max_x = self.end_point.x

    def move_to_new_point_by_units(self, units):
        dis_to_add = self.vector.skalar_mul_direction(units)
        point_val = self.start_point.get_point()
        self.change_pos(Point(point_val[0] + dis_to_add[0], point_val[1] + dis_to_add[1]))

    def is_Colliding(self, target):
        dm = self.m - target.m
        db = target.b - self.b
        if dm == 0:
            return False, 0
        else:
            answer = db/dm
            if self.min_x > answer or self.max_x < answer:
                return False, answer
            return True, db/dm

def main():
    """
    Add Documentation here
    """
    p1 = Point(100,100)
    v = Vector(5, 53.13)
    p2 = Point(200,200)
    s = StraightLine(p1,v)
    print s
    #s2 = StraightLine(p3,p4)
    #print (s.is_Colliding(s2))


if __name__ == '__main__':
    main()