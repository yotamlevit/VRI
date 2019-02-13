# -*- coding: utf-8 -*-
import analytic_geometry as ag
class Axis(object):
    def __init__(self, torque, power, shaft_diameter):
        self.torque = torque
        self.power = power
        self.shaft_radius = shaft_diameter/2
        temp = ag.Point(power, torque)
        self.function = temp.line_function(ag.Point(0, 0))

    def get_torque(self, power_precent):
        return self.function(float(self.power*power_precent)/100)



def main():
    """
    Add Documentation here
    """
    a = Axis(42, 5, 6)
    print a.function
    print str(a.get_torque(50))


if __name__ == '__main__':
    main()