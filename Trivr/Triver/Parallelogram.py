# -*- coding: utf-8 -*-
from StraightLine import StraightLine
from Vector import Vector
from Point import Point

class Parallelogram(object):
    def __init__(self, line, angle, length, center_g=None):
        """
        init for thje wall class
        """
        self.relative_angle = angle
        self.main_line = line
        self.relative_line = StraightLine(self.main_line.end_point, Vector(length, 180-(angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        self.center_g = center_g
        if self.center_g is not None:
            self.center_g_ratio = center_g
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def __str__(self):
        return 'Parallelogram: \nLine: {} ,\nRelative Line: {},\nLine Two: {} ,\nRelative Two: {} \n)'.format(self.main_line, self.relative_line, self.main_line_2, self.relative_line_2)

    def __repr__(self):
        return 'Line: {}, Relative Line: {})'.format(self.main_line, self.relative_line)


    def change_relative_angle(self, angle):
        self.relative_line.change_angle(180-angle)
        self.main_line_2.change_pos(self.relative_line.end_point)
        self.relative_line_2.change_angle(180-self.relative_line.vector.angle)
        if self.center_g is not None:
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def move_by_units(self, units):
        self.main_line.move_to_new_point_by_units(units)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        if self.center_g is not None:
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def change_pos(self, point):
        """
        change the wall position
        """
        self.main_line.change_pos(point)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        if self.center_g is not None:
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def change_rotation_by_value(self, value):
        self.change_rotation(self.main_line.vector.angle + value)

    def change_rotation(self, angle):
        """
        change the wall angle
        """
        self.main_line.change_angle(angle)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        if self.center_g is not None:
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def change_size(self, side1, side2):
        """
        change the wall size
        """
        self.main_line.changle_length(side1)
        self.relative_line.change_length(side2)
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        if self.center_g is not None:
            temp = self.main_line.start_point.point_by_ratio(self.main_line.end_point, self.center_g_ratio[0])
            temp2 = self.main_line_2.start_point.point_by_ratio(self.main_line_2.end_point, self.center_g_ratio[0])
            self.center_g = temp.point_by_ratio(temp2, self.center_g_ratio[1])

    def get_points(self):
        """
        return the wall vertex positions
        """
        points = []
        points.append(self.main_line.start_point)
        points.append(self.main_line.end_point)
        points.append(self.relative_line.end_point)
        points.append(self.main_line_2.end_point)
        return points

    def get_equation(self):
        equ = []
        equ.append(self.main_line.equ)
        equ.append(self.main_line_2.equ)
        equ.append(self.relative_line.equ)
        equ.append(self.relative_line_2.equ)
        return equ

    def get_point_value(self):
        points = self.get_points()
        for i in range(len(points)):
            points[i] = points[i].get_point()
        return points

    def draw(self, canvas, color):
        points = self.get_point_value()
        canvas.create_polygon(points, fill=color)

    def is_in(self, targets):
        """
        return true if the robot got in the
        """
        funcs = self.get_function()
        for func in funcs:
            for target in targets:
                if not target.is_Colliding(func)[0]:
                    return True
def main():
    """
    Add Documentation here
    """
    v = Vector(5, 30)
    p = Point(200, 200)
    line = StraightLine(p, v)
    p = Parallelogram(line, 90, 5)
    print p.get_points()
    print p.get_equation()
    print p.__str__()


if __name__ == '__main__':
    main()