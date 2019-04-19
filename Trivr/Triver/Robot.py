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
    def __init__(self, center_of_mass, shape, wheel=2, motor1=Motor('motor_1', 48, 210, 5, 6), motor2=Motor('motor_2', 48, 210, 5, 6)):
        self.wheel = wheel
        self.motor1 = motor1
        self.motor2 = motor2
        self.center_line = center_of_mass
        self.robot_weight = FRAME_WEIGHT + self.motor1.weight + self.motor2.weight
        super(Robot, self).__init__(shape)

    def move(self, action):
        if action == 'w':
            self.move_by_units(1)
            self.center_line.move_to_new_point_by_units(1)
        elif action == "d":
            self.rotate(1)
        elif action == 's':
            self.move_by_units(-1)
            self.center_line.move_to_new_point_by_units(-1)
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
        self.center_line.change_angle(self.center_line.vector.angle + angle)

    def __str__(self):
        return 'Robot --- : wheel radius: {},\n' \
               '            Motor1: {}, Motor2: {}'.format(self.wheel, self.motor1, self.motor2)

    def convert_robot_to_txt(self):
        return '<Robot><center_of_mass>' + self.center_line.start_point.convert_point_to_txt() +\
               '</center_of_mass>' + self.shape.convert_shape_to_txt() + '<wheel>' + str(self.wheel) + '</wheel><motor_1>' +\
               self.motor1.convert_motor_to_txt() + '</motor_1><motor_2>' + self.motor2.convert_motor_to_txt() + '</motor_2></Robot>'



def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()