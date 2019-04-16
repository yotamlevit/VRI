# -*- coding: utf-8 -*-
from Motor import *
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
from Parallelogram import Parallelogram
from Hit_Box import Hit_Box
from Wall import Wall
import sys
from Object_Builder import ObjectBuilder
ERR_MOTOR_POWER = 'Err - m[1] - power not in range'
FRAME_WEIGHT = 1000


class Robot(ObjectBuilder):
    def __init__(self, center, shape, name='Bob', wheel=2, motor1=Motor('motor_1', 48, 210, 5, 6), motor2=Motor('motor_2', 48, 210, 5, 6)):
        self.name = name
        self.wheel = wheel
        self.motor1 = motor1
        self.motor2 = motor2
        self.center_line = center
        self.robot_weight = FRAME_WEIGHT + self.motor1.weight + self.motor2.weight
        super(Robot, self).__init__(shape)

    def move(self, action):
        if action == 'w':
            self.move_by_units(1)
            self.center_line.move_to_new_point_by_units(1)
        elif action == "d":
            self.rotate(1)
            """
            torque = self.motor1.get_torque(True)
            if torque is not ERR_MOTOR_POWER:
                torque2 = self.motor2.get_torque(True)
                if torque2 is not ERR_MOTOR_POWER:
                    sum_torque = torque + torque2
            else:
                return torque
            """

    def rotate(self, angle):
        self.shape.change_rotation(angle, self.center_line)

    def __str__(self):
        return 'Robot --- : Name: {}, wheel radius: {},\n' \
               '            Motor1: {}, Motor2: {}'.format(self.name, self.wheel, self.motor1, self.motor2)



def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()