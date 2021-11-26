# -*- coding: utf-8 -*-
from analytic_geometry.Point import Point
from analytic_geometry.Vector import Vector
from analytic_geometry import Point as p, StraightLine
from analytic_geometry import Vector as v
from Error import Error


def line_from_file(root):
    point = (False, None)
    vector = (False, None)

    for child in root:
        tag = child.tag.lower()
        if tag == 'point':
            temp_p = p.point_from_file(child)
            if temp_p[0]:
                point = (True, temp_p[1])
            else:
                return temp_p
        elif tag == 'vector':
            temp_v = v.vector_from_file(child)
            if temp_v[0]:
                vector = (True, temp_v[1])
            else:
                return temp_v
    if point[0] and vector[0]:
        return True, StraightLine(point[1], vector[1])

    elif not point[0] and not vector[0]:
        return False, [Error.error.get('s_0p'), Error.error.get('s_0v')]

    elif not point[0]:
        return False, [Error.error.get('s_0p')]

    else:
        return False, [Error.error.get('s_0v')]


class StraightLine:

    def __init__(self, point, vector):
        """
        Initialize a straight line be using a Vector and a start Point

        @param point: Point - The start point of the straight line
        @param vector: Vector - The Direction vector to set the direction of the line
        """
        self.start_point = point
        self.vector = vector
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

        if self.start_point.y > self.end_point.y:
            self.min_y = self.end_point.y
            self.max_y = self.start_point.y
        else:
            self.min_y = self.start_point.y
            self.max_y = self.end_point.y

    def update_line(self, point: Point, vector: Vector):
        """
        This function reinitialize a straight line be using a Vector and a start Point

        @param point: Point - The start point of the straight line
        @param vector: Vector - The Direction vector to set the direction of the line
        """
        self.start_point = point
        self.vector = vector
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

        if self.start_point.y > self.end_point.y:
            self.min_y = self.end_point.y
            self.max_y = self.start_point.y
        else:
            self.min_y = self.start_point.y
            self.max_y = self.end_point.y

    def __str__(self):
        return '(Vector: {}, Start Point: {}, End Point: {}, Vector Function: {})'.format(self.vector, self.start_point, self.end_point, self.equ)

    def __repr__(self):
        return '(Vector: {}, Start Point: {}, End Point: {}, Vector Function: {})'.format(self.vector, self.start_point, self.end_point, self.equ)

    def change_length(self, length: float):
        """
        This function changes the length of a straight line

        @param length: Float - The new length
        """
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

        if self.start_point.y > self.end_point.y:
            self.min_y = self.end_point.y
            self.max_y = self.start_point.y
        else:
            self.min_y = self.start_point.y
            self.max_y = self.end_point.y

    def change_pos(self, point: Point):
        """
        This function sets a new start point to the line

        @param point: Point - The new point that the line will start from
        """
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

        if self.start_point.y > self.end_point.y:
            self.min_y = self.end_point.y
            self.max_y = self.start_point.y
        else:
            self.min_y = self.start_point.y
            self.max_y = self.end_point.y

    def change_angle(self, angle: float):
        """
        This function changes the angle of the line

        @param angle: Float - The new angle of the line
        """
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

        if self.start_point.y > self.end_point.y:
            self.min_y = self.end_point.y
            self.max_y = self.start_point.y
        else:
            self.min_y = self.start_point.y
            self.max_y = self.end_point.y

    def move_to_new_point_by_units(self, units):
        dis_to_add = self.vector.skalar_mul_direction(units)
        point_val = self.start_point.get_point()
        self.change_pos(Point(point_val[0] + dis_to_add[0], point_val[1] + dis_to_add[1]))

    def is_Colliding(self, target: StraightLine):
        """
        This function checks if one line is colliding with the current line

        @param target: StraightLine - The target line to check the collision with
        @return: True if the lines collide, False if not
        """
        if self.m is not None and target.m is not None:
            dm = self.m - target.m
            db = target.b - self.b
            if dm == 0:
                return False, 0

            else:
                answer = db/dm
                if self.min_x <= answer <= self.max_x and target.min_x <= answer <= target.max_x:
                    return True, db/dm

                return False, answer

        elif self.m is None and target.m is None:
            return False, None

        elif self.m is None:
            if target.min_x <= self.min_x <= target.max_x and self.min_y < target.fc(self.min_x) < self.max_y:
                return True, self.min_x

            return False, None

        else:
            if self.min_x <= target.min_x <= self.max_x and target.min_y < self.fc(target.min_x) < target.max_y:
                return True, target.min_x

            return False, None

    def convert_line_to_txt(self):
        return '<StraightLine>' + self.start_point.convert_point_to_txt() + self.vector.convert_vector_to_txt() + '</StraightLine>'


def main():
    """
    Add Documentation here
    """
    s1 = StraightLine(Point(0,490), Vector(1000,0))
    print(s1.equ)
    #s1.change_angle(130)
    s2 = StraightLine(Point(0,0), Vector(10,90))
    print(s2.equ)
    print(s1.is_Colliding(s2))


if __name__ == '__main__':
    main()