# -*- coding: utf-8 -*-
import analytic_geometry as ag
class Wall:
    def __init__(self, vector, width):
        self.vector = vector
        self.width = width

    def change_pos(self, point):
        self.vector.change_pos(point)

    def change_rotation(self,angle):
        self.vector.change_angle(angle)


    #def change_size(self, hight, width):

def main():
    """
    Add Documentation here
    """

if __name__ == '__main__':
    main()