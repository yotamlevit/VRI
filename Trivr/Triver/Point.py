# -*- coding: utf-8 -*-
import math

def slope(dx, dy):
    """
    calculates the slope between two points with their dx and dy
     dx: the difference between the x values of the points
     dy: he difference between the y values of the points
    """
    return (float(dy) / float(dx)) if dx else None

def quadratic_equation(a, b, c):
    """

    """
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

    def get_point(self):
        return self.x, self.y


    def halfway(self, target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)

    def distance(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        return (dx * dx + dy * dy) ** 0.5


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

    def slope_deg(self, target):
        return math.degrees(math.atan(self.slope(target)))

    def y_int(self, target):       # <= here's the magic
        return self.y - self.slope(target)*self.x if self.slope(target) is not None else None

    def line_equation(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)
        if slope is None and y_int is None:
            return 'x = {}'.format(self.x)
        elif y_int < 0:
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
    print Point(0,2).slope_deg(Point(1,1))
    """
    print (quadratic_equation(1,-4,4))
    p = Point(100, 100)
    p2 = Point(300,200)
    print (p.__str__())
    a = p.line_function(p2)
    print (a(300))
    """
if __name__ == '__main__':
    main()