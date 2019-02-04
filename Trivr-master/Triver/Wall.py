# -*- coding: utf-8 -*-
import analytic_geometry as ag
import math

class Wall:
    def __init__(self, vector, width):
        self.vector = vector
        self.width = width

    def change_pos(self, point):
        self.vector.change_pos(point)

    def change_rotation(self,angle):
        self.vector.change_angle(angle)

    def change_size(self, hight, width):
        self.vector.changle_length(hight)
        self.width = width

    def get_points(self):
        angle = self.vector.angle
        length = self.vector.length
        points = []
        points.append(self.vector.point)
        if 0 < angle < 90:
            points.append(ag.Point(points[0].x + math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(ag.Point(points[1].x - math.cos(angle*math.pi/180)*self.width, points[1].y + math.sin(angle*math.pi/180)*self.width))
            points.append(ag.Point(points[2].x - math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 90 < angle < 180:
            angle -= 90
            points.append(ag.Point(points[0].x - math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(ag.Point(points[1].x - math.cos(angle*math.pi/180)*self.width, points[1].y - math.sin(angle*math.pi/180)*self.width))
            points.append(ag.Point(points[2].x + math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 180 < angle < 270:
            angle -= 180
            points.append(ag.Point(points[0].x - math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(ag.Point(points[1].x + math.cos(angle*math.pi/180)*self.width, points[1].y + math.sin(angle*math.pi/180)*self.width))
            points.append(ag.Point(points[2].x + math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))
        elif 270 < angle < 360:
            angle -= 270
            points.append(ag.Point(points[0].x + math.cos(angle*math.pi/180)*length, points[0].y + math.sin(angle*math.pi/180)*length))
            points.append(ag.Point(points[1].x + math.cos(angle*math.pi/180)*self.width, points[1].y - math.sin(angle*math.pi/180)*self.width))
            points.append(ag.Point(points[2].x - math.cos(angle*math.pi/180)*length, points[2].y - math.sin(angle*math.pi/180)*length))

        return points

    def get_function(self):
        points = self.get_points()
        func = []
        func.append(ag.StraightLine(points[0], points[1]))
        func.append(ag.StraightLine(points[1], points[2]))
        func.append(ag.StraightLine(points[2], points[3]))
        func.append(ag.StraightLine(points[0], points[3]))
        return func

    def is_in(self, targets):
        funcs = self.get_function()
        for func in funcs:
            for target in targets:
                if not target.is_Colliding(func)[0]:
                    return True

def main():
    """
    Add Documentation here
    """
    p = ag.Point(100,100)
    v = ag.Vector(p, 4, 315)
    w = Wall(v, 4)
    w.get_points()
    p2 = ag.Point(1)

if __name__ == '__main__':
    main()