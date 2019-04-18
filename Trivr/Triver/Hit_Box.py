# -*- coding: utf-8 -*-
from Parallelogram import Parallelogram
from Vector import Vector
from StraightLine import StraightLine


class Hit_Box(Parallelogram):
    def __init__(self, min_point, max_point):
        v_min = Vector(max_point.y - min_point.y, 270)
        min_line = StraightLine(min_point, v_min)
        width = max_point.x - min_point.x
        super(Hit_Box, self).__init__(min_line, 90, width)



def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()