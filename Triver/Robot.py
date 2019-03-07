# -*- coding: utf-8 -*-
from Motor import *
import analytic_geometry as ag
from Point import Point
from StraightLine import StraightLine
from Vector import Vector

FRAME_WEIGHT = 1000
class Robot:

    def __init__(self, name='Bob', wheel=2, motor1=Motor('motor_1', 48, 210, 5, 6), motor2=Motor('motor_2', 48, 210, 5, 6)):
        self.name = name
        self.wheel = wheel
        self.motor1 = motor1
        self.motor2 = motor2
        self.robot_weight = FRAME_WEIGHT + self.motor1.weight + self.motor2.weight

    def __str__(self):
        return 'Robot --- : Name: {}, wheel radius: {},\n' \
               '            Motor1: {}, Motor2: {}'.format(self.name, self.wheel, self.motor1, self.motor2)



def main():
    """
    Add Documentation here
    """
    r = Robot()

    print r.motors
    print r.name
    print r.wheel


if __name__ == '__main__':
    main()