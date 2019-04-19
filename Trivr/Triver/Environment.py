# -*- coding: utf-8 -*-
from Wall import Wall
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
from Parallelogram import Parallelogram

def Enviroment_from_file():
    pass

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
        for obj in self.objects:
            #print(self.objects[obj])
            if self.robot.hit_box.is_Colliding(self.objects[obj].hit_box) and\
                    self.robot.shape.is_Colliding(self.objects[obj].shape):
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
        with open('environment.txt', 'w') as file_handle:
            file_handle.write(txt)

    def __str__(self):
        return "The Enviroment is: \nRobot is: {}\n" \
               "Objects are - {}".format(self.robot, self.objects)

def main():
    """
    Add Documentation here
    """
    v = Vector(Point(100,100), 100, 20)
    w = Wall(v, 10)
    e = Environment()
    e.add_obj(w)
    print (e.__str__())
    e.delete_obj(id(w))
    print (e.__str__())
    print (id(w))
    e.add_obj(w)
    e.clear_environment()
    print (e.__str__())
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()