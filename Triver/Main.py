# -*- coding: utf-8 -*-
from Environment import Environment
from Robot import Robot
import analytic_geometry as ag
from Wall import Wall
from Point import Point
from StraightLine import StraightLine
from Vector import Vector

def main():
    """
    Add Documentation here
    """
    r = Robot()
    v = Vector(Point(100, 100), 100, 20)
    w = Wall(v, 10)
    e = Environment(r,1000,1000)
    e.add_obj(w)
    print (e.__str__())


if __name__ == '__main__':
    main()