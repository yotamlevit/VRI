# -*- coding: utf-8 -*-
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
import math

class Wall(object):
    def __init__(self, vector, angle,):
        """
        init for thje wall class
        """
        self.vector = vector
        self.relative_vector = vector2

    def __str__(self):
        return 'Vector: {}, Relative Vector: {})'.format(self.vector, self.relative_vector)

    def __repr__(self):
        return 'Vector: {}, Relative Vector: {})'.format(self.vector, self.relative_vector)

    def change_pos(self, point):
        """
        change the wall position
        """
        self.vector.change_pos(point)

    def change_rotation(self,angle):
        """
        change the wall angle
        """
        self.vector.change_angle(angle)

    def change_size(self, side1, side2):
        """
        change the wall size
        """
        self.vector.changle_length(side1)
        self.relative_vector.change_length(side2)

    def get_points(self):
        """
        return the wall vertex positions
        """
        angle_x = self.vector.angle
        side1 = self.vector.length
        points = []
        points.append(self.vector.point)
        if 0 < angle_x < 90:

            points.append(Point(points[0].x + math.cos(math.radians(angle_x))*side1, points[0].y + math.sin(math.radians(angle_x))*side1))

            points.append(Point(points[1].x - math.cos(math.radians(angle_x))*self.width, points[1].y + math.sin(math.radians(angle_x))*self.width))
            points.append(Point(points[2].x - math.cos(math.radians(angle_x))*side1, points[2].y - math.sin(math.radians(angle_x))*side1))
        elif 90 < angle_x < 180:
            angle_x -= 90
            points.append(Point(points[0].x - math.cos(math.radians(angle_x))*side1, points[0].y + math.sin(math.radians(angle_x))*side1))
            points.append(Point(points[1].x - math.cos(math.radians(angle_x))*self.width, points[1].y - math.sin(math.radians(angle_x))*self.width))
            points.append(Point(points[2].x + math.cos(math.radians(angle_x))*side1, points[2].y - math.sin(math.radians(angle_x))*side1))
        elif 180 < angle_x < 270:
            angle_x -= 180
            points.append(Point(points[0].x - math.cos(math.radians(angle_x))*side1, points[0].y + math.sin(math.radians(angle_x))*side1))
            points.append(Point(points[1].x + math.cos(math.radians(angle_x))*self.width, points[1].y + math.sin(math.radians(angle_x))*self.width))
            points.append(Point(points[2].x + math.cos(math.radians(angle_x))*side1, points[2].y - math.sin(math.radians(angle_x))*side1))
        elif 270 < angle_x < 360:
            angle_x -= 270
            points.append(Point(points[0].x + math.cos(math.radians(angle_x))*side1, points[0].y + math.sin(math.radians(angle_x))*side1))
            points.append(Point(points[1].x + math.cos(math.radians(angle_x))*self.width, points[1].y - math.sin(math.radians(angle_x))*self.width))
            points.append(Point(points[2].x - math.cos(math.radians(angle_x))*side1, points[2].y - math.sin(math.radians(angle_x))*side1))
        elif angle_x == 90:
            points.append(Point(points[0].x, points[0].y + side1))
            points.append(Point(points[1].x + self.width, points[1].y))
            points.append(Point(points[2].x, points[2].y - side1))
        elif angle_x == 180:
            points.append(Point(points[0].x - side1, points[0].y))
            points.append(Point(points[1].x, points[1].y + self.width))
            points.append(Point(points[2].x - side1, points[2].y))
        elif angle_x == 270:
            points.append(Point(points[0].x, points[0].y - side1))
            points.append(Point(points[1].x - self.width, points[1].y))
            points.append(Point(points[2].x, points[2].y + side1))
        elif angle_x == 0:
            points.append(Point(points[0].x + side1, points[0].y))
            points.append(Point(points[1].x, points[1].y - self.width))
            points.append(Point(points[2].x + side1, points[2].y))
        return points

    def get_point_value(self):
        points = self.get_points()
        for i in range(len(points)):
            points[i] = points[i].get_point()
        return points

    def draw(self, canvas, color):
        points = self.get_point_value()
        canvas.create_polygon(points, fill=color)

    def get_function(self):
        """
        return the sides functions
        """
        points = self.get_points()
        func = []
        func.append(StraightLine(points[0], points[1]))
        func.append(StraightLine(points[1], points[2]))
        func.append(StraightLine(points[2], points[3]))
        func.append(StraightLine(points[0], points[3]))
        return func

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
    v = Vector(Point(100, 100), 100, 20)
    w = Wall(v, 10)
    w.get_function()
    print w.get_points()

if __name__ == '__main__':
    main()