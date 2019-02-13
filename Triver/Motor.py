# -*- coding: utf-8 -*-
from Linear import *

class Motor(Linear):
    def __init__(self, name, toque, weight, power, shaft_diameter):
        self.name = name
        self.weight = weight
        super(Motor, self).__init__(toque, power, shaft_diameter)


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()