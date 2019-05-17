# -*- coding: utf-8 -*-
from Linear import *
from Point import Point
from Error import Error
from StraightLine import StraightLine
from Vector import Vector


ERR_MOTOR_POWER = 'Err - m[1] - power not in range'


def motor_from_file(root):
    name = (False, None)
    torque = (False, None)
    weight = (False, None)
    power = (False, None)
    shaft_diameter = (False, None)
    for child in root:
        tag = child.tag.lower()
        if tag == 'name':
            name = (True, child.text)
        elif tag == 'torque':
            try:
                torque = (True, int(child.text))
            except ValueError:
                print(Error.error.get('m_1t'))
                return False, [Error.error.get('m_1t')]
        elif tag == 'weight':
            try:
                weight = (True, int(child.text))
            except ValueError:
                print(Error.error.get('m_1w'))
                return False, [Error.error.get('m_1w')]
        elif tag == 'power':
            try:
                power = (True, int(child.text))
            except ValueError:
                print(Error.error.get('m_1p'))
                return False, [Error.error.get('m_1p')]
        elif tag == 'shaft_diameter':
            try:
                shaft_diameter = (True, float(child.text))
            except ValueError:
                print(Error.error.get('m_1s'))
                return False, [Error.error.get('m_1s')]
    if name[0] and torque[0] and weight[0] and power[0] and shaft_diameter[0]:
        return True, Motor(name[1], torque[1], weight[1], power[1], shaft_diameter[1])
    er = []
    if not name[0]:
        er.append(Error.error.get('m_0n'))
    if not torque[0]:
        er.append(Error.error.get('m_0t'))
    if not weight[0]:
        er.append(Error.error.get('m_0w'))
    if not power[0]:
        er.append(Error.error.get('m_0p'))
    if not shaft_diameter[0]:
        er.append(Error.error.get('m_0s'))
    return False, er

class Motor(Linear):
    def __init__(self, name, torque, weight, power, shaft_diameter):
        self.name = name
        self.weight = weight
        #self.current_power_precent = 0
        self.move_power_precent = 0
        #self.torque = torque
        #self.power = power
        #self.shaft_radius = shaft_diameter/2
        peak_p = Point(power, torque)
        self.function = peak_p.line_function(Point(0, 0))
        super(Motor, self).__init__(torque, power, shaft_diameter)

    def set_press_power_precent(self, new_power_p):
        self.press_power_precent = new_power_p

    #def set_current_power_precent(self, new_power_p):
    #    self.current_power_precent = new_power_p

    def get_torque(self, forward):
        if forward and -100 <= self.move_power_precent <= 100:
            return self.function(float(self.power*self.move_power_precent)/100)
        elif not forward and -100 <= self.move_power_precent <= 100:
            return self.function(float(self.power*self.move_power_precent)/100) *-1
        return ERR_MOTOR_POWER


    def __str__(self):
        return 'Name: {}, weight: {}, torque: {}, power: {},\n' \
               '            shaft radius: {}\n          '.format(self.name, self.weight, self.torque, self.power, self.shaft_radius)

    def convert_motor_to_txt(self):
        return '<name>' + self.name + '</name><torque>' + str(self.torque) + '</torque><weight>' +\
               str(self.weight) + '</weight><power>' + str(self.power) + '</power><shaft_diameter>' +\
               str(self.shaft_radius*2) + '</shaft_diameter>'

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()