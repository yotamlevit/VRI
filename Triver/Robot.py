# -*- coding: utf-8 -*-
from Motor import *

FRAME_WEIGHT = 1000
class Robot:

    def __init__(self, name='Bob', wheel=2, motors=[Motor('motor_1', 48, 210, 'no_function', 'linear'), Motor('motor_2', 48, 210, 'no_function', 'linear')]):
        self.name = name
        self.wheel = wheel
        self.motors = motors
        self.robot_weight = FRAME_WEIGHT
        for motor in motors:
            self.robot_weight += motor.weight
        self.fre



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