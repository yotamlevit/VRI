# -*- coding: utf-8 -*-
from StraightLine import StraightLine
from Vector import Vector
from Point import Point

class Parallelogram(object):
    def __init__(self, line, angle, length):
        """
        init for thje wall class
        """
        self.relative_angle = angle
        self.main_line = line
        self.relative_line = StraightLine(self.main_line.end_point, Vector(length, 180-(angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))

    def __str__(self):
        return 'Parallelogram: \nLine: {} ,\nRelative Line: {},\nLine Two: {} ,\nRelative Two: {} \n)'.format(self.main_line, self.relative_line, self.main_line_2, self.relative_line_2)

    def __repr__(self):
        return 'Line: {}, Relative Line: {})'.format(self.main_line, self.relative_line)

    def get_lines(self):
        return [self.main_line, self.main_line_2, self.relative_line, self.relative_line_2]

    def change_relative_angle(self, angle):
        self.relative_line.change_angle(180-angle)
        self.main_line_2.change_pos(self.relative_line.end_point)
        self.relative_line_2.change_angle(180-self.relative_line.vector.angle)

    def move_by_units(self, units):
        self.main_line.move_to_new_point_by_units(units)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))

    def get_middle_point(self):
        return self.main_line.start_point.halfway(self.main_line.end_point).halfway(self.main_line_2.start_point.halfway(self.main_line_2.end_point))

    def change_pos(self, point):
        """
        change the wall position
        """
        self.main_line.change_pos(point)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))

    def change_rotation(self, angle, center_line):
        """
        change the wall angle
        """
        v_angle = self.main_line.start_point.slope_deg(center_line.start_point)
        temp_v = Vector(self.main_line.start_point.distance(center_line.start_point), v_angle + 360)
        temp_line = StraightLine(center_line.start_point, temp_v)
        temp_line.change_angle(temp_line.vector.angle + angle)
        self.main_line.change_pos(temp_line.end_point)
        self.main_line.change_angle(self.main_line.vector.angle + angle)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))

    def change_size(self, side1, side2):
        """
        change the wall size
        """
        self.main_line.changle_length(side1)
        self.relative_line.change_length(side2)
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))

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

    def is_Colliding(self, shape):
        """
        return true if the robot got in the
        """
        targets = shape.get_lines()
        lines = self.get_lines()
        for line in lines:
            for target in targets:
                if line.is_Colliding(target)[0]:
                    return True
        return False
def main():
    """
    Add Documentation here
    """
    v = Vector(5, 90)
    p = Point(200, 200)
    line = StraightLine(p, v)
    p = Parallelogram(line, 90, 5)
    print(p.get_equation())
    s2 = StraightLine(Point(199,0), Vector(1000,90))
    print(s2)
    t = []
    t.append(s2)
    print(p.is_Colliding(t))
    """
    print (p.get_points())
    print (p.get_equation())
    print (p.__str__())
    """

if __name__ == '__main__':
    main()