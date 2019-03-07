# -*- coding: utf-8 -*-
from Axis import *
from Point import Point
from StraightLine import StraightLine
from Vector import Vector

class Linear(Axis):
    def __init__(self, torque, power, shaft_diameter):
        super(Linear, self).__init__(torque, power, shaft_diameter)

    def get_torque(self, power_precent):
        return super(Linear, self).get_torque(power_precent) * -1
def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()
