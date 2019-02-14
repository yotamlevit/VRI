# -*- coding: utf-8 -*-
from Linear import *

class Motor(Linear):
    def __init__(self, name, torque, weight, power, shaft_diameter):
        self.name = name
        self.weight = weight
        super(Motor, self).__init__(torque, power, shaft_diameter)

    def __str__(self):
        return 'Name: {}, weight: {}, torque: {}, power: {},\n' \
               '            shaft radius: {}\n          '.format(self.name, self.weight, self.torque, self.power, self.shaft_radius)

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()