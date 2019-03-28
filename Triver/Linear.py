# -*- coding: utf-8 -*-
from motor_motion import Motor_Motion
from Point import Point
from StraightLine import StraightLine
from Vector import Vector

class Linear(Motor_Motion):
    def __init__(self, torque, power, shaft_diameter):
        super(Linear, self).__init__(torque, power, shaft_diameter)

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()
