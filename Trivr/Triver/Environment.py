# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
from Wall import Wall
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
from Parallelogram import Parallelogram
from Motor import Motor
from Robot import Robot
import Robot as rob
from Error import Error


def environment_from_file(file_name='environment.xml'):
    tree = ET.parse(file_name)
    root = tree.getroot()
    height = (False, None)
    width = (False, None)
    robot = (False, None)
    objects = (False, None)
    for child in root:
        print(child.tag)
        tag = child.tag.lower()
        if tag == 'height':
            try:
                height = (True, int(child.text))
            except:
                print(Error.error.get('e_1h'))
            finally:
                return False, [Error.error.get('e_1h')]
        elif tag == 'width':
            width = (True, child.text)
        elif tag == 'robot':
            robot = (True, rob.robot_from_file(child))

class Environment:

    def __init__(self, robot, height, width):
        self.objects = {}
        self.robot = robot
        self.boundaries = Parallelogram(StraightLine(Point(0,0), Vector(width,0)), 90, height)

    def check_robot_in_boundaries(self):
        if self.robot.hit_box.is_Colliding(self.boundaries):
            print("Box is hit")
            if self.robot.shape.is_Colliding(self.boundaries):
                return False
        return True

    def check_object_object_crash(self):
        pass

    def check_obj_robot_crash(self):
        #print("2")
        for obj in self.objects:
            #if self.robot.hit_box.is_Colliding(self.objects[obj].hit_box):
                #print("1")
            if self.robot.shape.is_Colliding(self.objects[obj].shape):
                return True
        return False

    def check_crash(self):
        crash = []
        crash.append(not self.check_robot_in_boundaries())
        crash.append(self.check_obj_robot_crash())
        if True in crash:
            return True
        return False

    def add_obj(self, obj):
        self.objects[str(id(obj))] = obj

    def move_robot(self, action):
        self.robot.move(action)

    def get_key(self, obj_id):
        """
        returns:
            the value for the specified key if key is in dictionary.
            None if the key is not found and value is not specified.
            value if the key is not found and value is specified.
        """
        self.objects.get(str(obj_id))


    def delete_obj(self, obj_id):
        if str(obj_id) in self.objects:
            del self.objects[str(obj_id)]
            return True
        else:
            return False
    def clear_environment(self):
        self.objects.clear()

    def convert_env_to_file(self):
        txt = '<Enviroment>'
        txt += '<height>' + str(self.boundaries.main_line.vector.length) + '</height><width>' +\
               str(self.boundaries.relative_line.vector.length) + '</width>'
        txt += self.robot.convert_robot_to_txt()
        txt+='<Objects>'
        for obj in self.objects:
            ob = self.objects[obj]
            txt += ob.convert_obj_to_txt()
        txt += '</Objects>'
        txt += '</Enviroment>'
        with open('environment.xml', 'w') as file_handle:
            file_handle.write(txt)

    def __str__(self):
        return "The Enviroment is: \nRobot is: {}\n" \
               "Objects are - {}".format(self.robot, self.objects)

def main():
    """
    Add Documentation here
    """
    wheel = 2
    color = "black"
    length = 100
    v_r = Vector(200, 180)
    line = StraightLine(Point(250,500), v_r)
    motor1 = Motor('motor_1', 48, 210, 5, 6)
    motor2 = Motor('motor_2', 48, 210, 5, 6)
    p = Parallelogram(line, 90, length)
    center_v = Vector(1,v_r.angle)
    center_point = p.get_middle_point()
    center_line = StraightLine(center_point, center_v)
    r = Robot(center_line, p, wheel, motor1, motor2)
    v = Vector(100, 0)
    p = Point(200, 200)
    line = StraightLine(p, v)
    p = Parallelogram(line, 120, 200)
    w = Wall(p)
    env = Environment(r, 1000, 1000)
    env.add_obj(w)
    print (env.__str__())
    env.convert_env_to_file()
    environment_from_file()
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()