# -*- coding: utf-8 -*-
from Point import Point
from StraightLine import StraightLine
from Vector import Vector

ERR_MOTOR_POWER = 'Err - m[1] - power not in range'


class Motor_Motion(object):
    def __init__(self, torque, power, shaft_diameter):
        self.torque = torque
        self.power = power
        self.shaft_radius = shaft_diameter/2
        peak_p = Point(power, torque)
        self.function = peak_p.line_function(Point(0, 0))

    def get_torque(self, power_precent):
        if -100 < power_precent < 100:
            return self.function(float(self.power*power_precent)/100)
        return ERR_MOTOR_POWER



def main():
    """
    Add Documentation here
    """
    a = Motor_Motion(42, 5, 6)
    print (a.function)
    print (str(a.get_torque(150)))


if __name__ == '__main__':
    main()