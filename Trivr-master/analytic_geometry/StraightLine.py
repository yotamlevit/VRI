# -*- coding: utf-8 -*-
from Point import Point
class StraightLine:

    def __init__(self, point1, point2):
        if point1.x > point2.x:
            self.min_x = point2.x
            self.max_x = point1.x
        else:
            self.max_x = point2.x
            self.min_x = point1.x
        self.m = point1.slope(point2)
        self.b = point1.y_int(point2)
        self.fc = point1.line_function(point2)
        self.equ = point1.line_equation(point2)

    def is_Colliding(self, target):
        dm = self.m - target.m
        db = target.b - self.b
        if dm == 0:
            return False,0
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
    p2 = Point(200,200)
    p3 = Point(300,200)
    p4 = Point(100,100)
    s = StraightLine(p1,p2)
    s2 = StraightLine(p3,p4)
    print s.is_Colliding(s2)


if __name__ == '__main__':
    main()