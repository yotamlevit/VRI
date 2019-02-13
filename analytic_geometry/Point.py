# -*- coding: utf-8 -*-
import math

def slope(dx, dy):
    return (float(dy) / float(dx)) if dx else None

def quadratic_equation(a, b, c):
    d = (b**2) - (4*a*c)
    return (-b - d ** 0.5) / (a * 2), (-b + d ** 0.5) / (a * 2) if d >= 0 else (None, None)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def halfway(self, target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)

    def distance(self, find_point, target=None, vector=None, distance=None):
        if not find_point:
            dx = target.x - self.x
            dy = target.y - self.y
            return (dx * dx + dy * dy) ** 0.5
        else:
            print "Error"
            """
            if 90 != vector.angle and vector.angle and 180 and vector.angle != 270 and vector.angle != 0:
                tag = math.tan(vector.angle * math.pi/180)
                a = 1 + tag
                b = (-2 * vector.point.y * tag) - (2 * vector.point.x)
                c = (vector.point.x ** 2) + (vector.point.y ** 2) - distance
                solution = quadratic_equation(a, b, c)
                print solution
                if not all(solution):
                    if 0 < vector.angle < 90 or 270 < vector.angle <= 359:
                        for s in solution:
                            if s > vector.x:
                                solve = s
                    elif 90 < vector.angle < 270:
                        for s in solution:
                            if s < vector.x:
                                solve = s
            else:
                return
            """



    def reflect_x(self):
        return Point(-self.x,self.y)

    def reflect_y(self):
        return Point(self.x, -self.y)

    def reflect_x_y(self):
        return Point(-self.x, -self.y)

    def slope_from_origin(self):
        return slope(self.x, self.y)

    def slope(self, target):
        return slope(target.x - self.x, target.y - self.y)

    def y_int(self, target):       # <= here's the magic
        return self.y - self.slope(target)*self.x

    def line_equation(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)
        if y_int < 0:
            y_int = -y_int
            sign = '-'
        else:
            sign = '+'

        return 'y = {}x {} {}'.format(slope, sign, y_int)

    def line_function(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)
        def fn(x):
            return slope*x + y_int
        return fn

def main():
    """
    Add Documentation here
    """
    print quadratic_equation(1,-4,4)
    p = Point(100, 100)
    p2 = Point(300,200)
    print p.__str__()
    a = p.line_function(p2)
    print a(300)

if __name__ == '__main__':
    main()