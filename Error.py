# -*- coding: utf-8 -*-

class Error(object):
        error = {'p_0x': 'Point err: x-value is missing', 'p_0y': 'Point err: y-value is missing',
                 'p_1x' : 'Point err: invalid x-value', 'p_1y' : 'Point err: invalid y-value',
                 'v_0l' : 'Vector err: length is missing', 'v_0a' : 'Vector err: angle is missing',
                 'v_1l' : 'Vector err: invalid length`s value', 'v_1a' : 'Vector err: invalid angle`s value',
                 's_0p' : 'Line err: point is missing', 's_0v' : 'Line err: vector is missing',
                 'p_0line' : 'Para err: line is missing', 'p_0a' : 'Para err: angle is missing',
                 'p_0l' : 'Para err: length is missing', 'p_1a' : 'Para err: invalid angle value',
                 'p_1l' : 'Para err: invalid length value', 'r_1w' : 'Robot err: invalid wheel value',
                 'm_1t' : 'Motor err: invalid torque value', 'm_1w' : 'Motor err: invalid weight value',
                 'm_1p' : 'Motor err: invalid power value', 'm_1s' : 'Motor err: invalid shaft_diameter value',
                 'm_0n' : 'Motor err: missing name', 'm_0t' : 'Motor err: missing torque',
                 'm_0w' : 'Motor err: missing weight', 'm_0p' : 'Motor err: missing power',
                 'm_0s' : 'Motor err: missing shaft_diameter', 'r_0c' : 'Robot err: missing center_of_mass',
                 'r_0s' : 'Robot er: missing shape', 'r_0w' : 'Robot er: missing wheel',
                 'r_0m1' : 'Robot er: missing motor1', 'r_0m2' : 'Robot er: missing motor2',
                 'e_1h' : 'Env err: invalid height', 'e_1w' : 'Env err: invalid width',
                 'w_0s' : 'Wall err: missing shape', 'e_0h' : 'Env err: missing height',
                 'e_0w': 'Env err: missing width', 'e_0r' : 'Env err: missing robot',
                 'gd_cfef' : 'Environment: cannot found file'}


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()