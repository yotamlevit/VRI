# -*- coding: utf-8 -*-
from Motor import *
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
from Wall import Wall

FRAME_WEIGHT = 1000
class Robot(Wall):

    def __init__(self, name='Bob', wheel=2, vector=Vector(Point(500, 500), 100, 90), length=100, motor1=Motor('motor_1', 48, 210, 5, 6), motor2=Motor('motor_2', 48, 210, 5, 6)):
        self.name = name
        self.wheel = wheel
        self.motor1 = motor1
        self.motor2 = motor2
        self.power_p = 0
        self.robot_weight = FRAME_WEIGHT + self.motor1.weight + self.motor2.weight
        super(Robot, self).__init__(vector, length)

    def set_power_p(self, new_power_p):
        self.power_p = new_power_p

    def move(self, action):
        if action == 'w':
            self.motor1.move(action, self.power_p)

    def __str__(self):
        return 'Robot --- : Name: {}, wheel radius: {},\n' \
               '            Motor1: {}, Motor2: {}'.format(self.name, self.wheel, self.motor1, self.motor2)



def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()