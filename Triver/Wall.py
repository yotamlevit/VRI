# -*- coding: utf-8 -*-
import analytic_geometry

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

    def is_in(self, obj):
def main():
    """
    Add Documentation here
    """

if __name__ == '__main__':
    main()