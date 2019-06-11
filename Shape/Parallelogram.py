# -*- coding: utf-8 -*-
from analytic_geometry.StraightLine import StraightLine
from analytic_geometry.Vector import Vector
from analytic_geometry.Point import Point
from analytic_geometry import StraightLine as st
import sys
from Error import Error


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
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

    def __str__(self):
        return 'Parallelogram: \nLine: {} ,\nRelative Line: {},\nLine Two: {} ,\nRelative Two: {} \n)'.format(self.main_line, self.relative_line, self.main_line_2, self.relative_line_2)

    def __repr__(self):
        return 'Line: {}, Relative Line: {})'.format(self.main_line, self.relative_line)

    def get_ultrasonic_angle(self, pos):
        if pos == 0:
            return self.relative_line_2.vector.angle + 315
        if pos == 1:
            return self.main_line.vector.angle + 315
        if pos == 2:
            return self.relative_line.vector.angle + 315
        if pos == 3:
            return self.main_line_2.vector.angle + 315
        if pos == 4:
            return self.main_line.vector.angle - 90
        if pos == 5:
            return self.relative_line.vector.angle - 90
        if pos == 6:
            return self.main_line_2.vector.angle - 90
        if pos == 7:
            return self.relative_line_2.vector.angle - 90

    def get_lines(self):
        return [self.main_line, self.main_line_2, self.relative_line, self.relative_line_2]

    def change_relative_angle(self, angle):
        self.relative_line.change_angle(180-angle)
        self.main_line_2.change_pos(self.relative_line.end_point)
        self.relative_line_2.change_angle(180-self.relative_line.vector.angle)
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

    def move_by_units(self, units):
        self.main_line.move_to_new_point_by_units(units)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

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
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

    def change_rotation(self, angle, center_line):
        """
        change the wall angle
        """
        v_angle = self.main_line.start_point.slope_deg(center_line.start_point)
        #print(center_line.start_point)
        #print(v_angle)
        if self.main_line.start_point.x < center_line.start_point.x and self.main_line.start_point.y > center_line.start_point.y or self.main_line.start_point.x < center_line.start_point.x and self.main_line.start_point.y < center_line.start_point.y:
            v_angle = 180 + v_angle
        temp_v = Vector(self.main_line.start_point.distance(center_line.start_point), v_angle + 360)
        temp_line = StraightLine(center_line.start_point, temp_v)
        #print( 'line:   '  + str(temp_line.equ))
        temp_line.change_angle(temp_line.vector.angle + angle)
        #print("new_point:   " + str(temp_line.end_point))
        self.main_line.change_pos(temp_line.end_point)
        new_angle = self.main_line.vector.angle + angle
        self.main_line.change_angle(new_angle)
        self.relative_line = StraightLine(self.main_line.end_point, Vector(self.relative_line.vector.length, 180-(self.relative_angle-self.main_line.vector.angle)))
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

    def change_size(self, side1, side2):
        """
        change the wall size
        """
        self.main_line.changle_length(side1)
        self.relative_line.change_length(side2)
        self.main_line_2 = StraightLine(self.relative_line.end_point, Vector(self.main_line.vector.length, 180+self.main_line.vector.angle))
        self.relative_line_2 = StraightLine(self.main_line_2.end_point, Vector(self.relative_line.vector.length, 180 + self.relative_line.vector.angle))
        self.pos = self.get_points()
        self.pos.append(self.main_line.start_point.halfway(self.main_line.end_point))
        self.pos.append(self.relative_line.start_point.halfway(self.relative_line.end_point))
        self.pos.append(self.main_line_2.start_point.halfway(self.main_line_2.end_point))
        self.pos.append(self.relative_line_2.start_point.halfway(self.relative_line_2.end_point))

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

    def get_edge_points(self):
        points = self.get_points()
        max_x = -1*sys.maxsize
        max_y = -1*sys.maxsize
        min_x = sys.maxsize
        min_y = sys.maxsize
        for point in points:
            if point.x > max_x:
                max_x = point.x
            elif point.x < min_x:
                min_x = point.x
            if point.y > max_y:
                max_y = point.y
            elif point.y < min_y:
                min_y = point.y
        return Point(max_x,max_y),Point(min_x, min_y)

    def convert_shape_to_txt(self):
        return '<Parallelogram>' + self.main_line.convert_line_to_txt() + '<angle>' + str(self.relative_angle) + '</angle>' + '<length>' + str(self.relative_line.vector.length) + '</length></Parallelogram>'

    def is_Colliding(self, shape):
        """
        return true if the robot got in the
        """
        targets = shape.get_lines()
        lines = self.get_lines()
        for line in lines:
            for target in targets:
                if line.is_Colliding(target)[0]:
                    #print(line.equ)
                    #print(target.equ)
                    return True
        return False

    @staticmethod
    def parallelogram_from_file(root):
        line = (False, None)
        angle = (False, None)
        length = (False, None)
        for child in root:
            tag = child.tag.lower()
            if tag == 'straightline':
                temp_l = st.line_from_file(child)
                if temp_l[0]:
                    line = (True, temp_l[1])
                else:
                    return temp_l
            elif tag == 'angle':
                try:
                    angle = (True, int(child.text))
                except ValueError:
                    print(Error.error.get('p_1a'))
                    return False, [Error.error.get('p_1a')]
            elif tag == 'length':
                try:
                    length = (True, int(child.text))
                except ValueError:
                    print(Error.error.get('p_1l'))
                    return False, [Error.error.get('p_1l')]
        if line[0] and angle[0] and length[0]:
            return True, Parallelogram(line[1], angle[1], length[1])
        er = []
        if not line[0]:
            er.append(Error.error.get('p_0line'))
        if not angle[0]:
            er.append(Error.error.get('p_0a'))
        if not length[0]:
            er.append(Error.error.get('p_0l'))
        return False, er

def main():
    """
    Add Documentation here
    """
    v = Vector(20, 180)
    p = Point(490, 495)
    line = StraightLine(p, v)
    p = Parallelogram(line, 90, 10)
    print(p.get_middle_point())
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