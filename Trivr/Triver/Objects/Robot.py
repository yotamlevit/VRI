# -*- coding: utf-8 -*-
from Movement import Motor as Mot
from Movement.Motor import *
from analytic_geometry import Point
from analytic_geometry import StraightLine
from analytic_geometry.Vector import Vector
from Shape import Parallelogram
from Error import Error
from Objects.Object_Builder import ObjectBuilder
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
        elif action == 'a':
            self.rotate(-1)
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
               '</center_of_mass><shape>' + self.shape.convert_shape_to_txt() + '</shape><wheel>' + str(self.wheel) + '</wheel><motor_1>' +\
               self.motor1.convert_motor_to_txt() + '</motor_1><motor_2>' + self.motor2.convert_motor_to_txt() + '</motor_2></Robot>'

    @staticmethod
    def robot_from_file(root):
        center_of_mass = (False, None)
        shape = (False, None)
        wheel =(False, None)
        motor1 = (False, None)
        motor2 = (False, None)
        for child in root:
            tag = child.tag.lower()
            if tag == 'center_of_mass':
                for sub_c in child:
                    if sub_c.tag.lower() == 'point':
                        temp_p = Point.point_from_file(sub_c)
                if temp_p[0]:
                    center_of_mass = (True, temp_p[1])
                else:
                    return temp_p
            elif tag == 'shape':
                for sub_c in child:
                    if sub_c.tag.lower() == 'parallelogram':
                        temp_p = Parallelogram.parallelogram_from_file(sub_c)
                if temp_p[0]:
                    shape = (True, temp_p[1])
                else:
                    return temp_p
            elif tag == 'wheel':
                try:
                    wheel = (True, int(child.text))
                except ValueError:
                    print(Error.error.get('r_1w'))
                    return False, [Error.error.get('r_1w')]
            elif tag == 'motor_1':
                temp_m = Motor.motor_from_file(child)
                if temp_m[0]:
                    motor1 = (True, temp_m[1])
                else:
                    return temp_m
            elif tag == 'motor_2':
                temp_m = Motor.motor_from_file(child)
                if temp_m[0]:
                    motor2 = (True, temp_m[1])
                else:
                    return temp_m
        if center_of_mass[0] and shape[0] and wheel[0] and motor1[0] and motor2[0]:
            center_v = Vector(1, shape[1].main_line.vector.angle)
            center_line = StraightLine.StraightLine(center_of_mass[1], center_v)
            return True, Robot(center_line, shape[1], wheel[1], motor1[1], motor2[1])
        er = []
        if not center_of_mass[0]:
            er.append(Error.error.get('r_0c'))
        if not shape[0]:
            er.append(Error.error.get('r_0s'))
        if not wheel[0]:
            er.append(Error.error.get('r_0w'))
        if not motor1[0]:
            er.append(Error.error.get('r_0m1'))
        if not motor2[0]:
            er.append(Error.error.get('r_0m2'))
        return False, er




def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()