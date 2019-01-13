# -*- coding: utf-8 -*-

class StraightLine:

    def __init__(self, point1, point2):
        if point1.x > point2.x:
            self.min_x = point2.x
            self.max_x = point1.x
        else:
            self.max_x = point2.x
            self.min_x = point1.x
        self.m = point1.slop(point2)
        self.b = point1.y_int(point2)
        self.fx = point1.line_function(point2)
        self.equ = point1.line_equation(point2)

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()