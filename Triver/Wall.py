# -*- coding: utf-8 -*-
import analytic_geometry as ag
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
import math

class Wall:
    def __init__(self, vector, width):
        """
        init for thje wall class
        """
        self.vector = vector
        self.width = width

    def __str__(self):
        return 'Vector: {}, width: {})'.format(self.vector, self.width)

    def __repr__(self):
        return 'Vector: {}, width: {})'.format(self.vector, self.width)

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

    def change_size(self, hight, width):
        """
        change the wall size
        """
        self.vector.changle_length(hight)
        self.width = width

    def get_points(self):
        """
        return the wall vertex positions
        """
        angle = self.vector.angle
        length = self.vector.length
        points = []
        points.append(self.vector.point)
        if 0 < angle < 90:
            points.append(Point(points[0].x + math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(Point(points[1].x - math.cos(angle*math.pi/180)*self.width, points[1].y + math.sin(angle*math.pi/180)*self.width))
            points.append(Point(points[2].x - math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 90 < angle < 180:
            angle -= 90
            points.append(Point(points[0].x - math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(Point(points[1].x - math.cos(angle*math.pi/180)*self.width, points[1].y - math.sin(angle*math.pi/180)*self.width))
            points.append(Point(points[2].x + math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 180 < angle < 270:
            angle -= 180
            points.append(Point(points[0].x - math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(Point(points[1].x + math.cos(angle*math.pi/180)*self.width, points[1].y + math.sin(angle*math.pi/180)*self.width))
            points.append(Point(points[2].x + math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 270 < angle < 360:
            angle -= 270
            points.append(Point(points[0].x + math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(Point(points[1].x + math.cos(angle*math.pi/180)*self.width, points[1].y - math.sin(angle*math.pi/180)*self.width))
            points.append(Point(points[2].x - math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))

        return points

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
    p = Point(100,100)
    v = Vector(p, 4, 315)
    w = Wall(v, 4)
    w.get_points()
    #p2 = Point(1)
    print w.__str__()

if __name__ == '__main__':
    main()