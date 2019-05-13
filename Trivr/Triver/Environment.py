# -*- coding: utf-8 -*-
from Wall import Wall
from Point import Point
from StraightLine import StraightLine
from Vector import Vector
from Parallelogram import Parallelogram

def environment_from_file(env_name):
    with open(env_name + '.txt','r') as file_handle:
        env = file_handle.read()
    env = clear_env_string(env)
    bool_table = {'environment' : False, '/environment': False,
                  'height': False, '/height': False, 'width': False, '/width': False,
                  'robot': False, 'center_of_mass': False, '/center_of_mass': False,
                  'shape': False, '/shape': False, 'wheel': False, '/wheel': False,
                  'motor_1': False, '/motor_1': False, 'motor_2': False, '/motor_2': False,
                  '/robot': False, 'objects': False, '/objects': False}
    if env[0].lower() == 'environment' and env[len(env)-1].lower() == '/environment':
        bool_table['environment'] = True
        bool_table['/environment'] = True
        del env[0]
        del env[len(env)-1]
    i = 0
    while i < len(env):
        bool_table[env[i].lower()] = True
        index = 0
        #for element in env:
            #if element
            #index+=1
        bool_table[env[i+2].lower()] = env[i+1]
        for num in range(i, i+3):
            del env[i]
        i = 0
    if False in bool_table.values():
        print("False")
    else:
        print("true")

def clear_env_string(str):
    env = str.replace(' ', '')
    env = str.replace('\n','')
    env = str.replace('<','')
    env = str.split('>')
    env.pop()
    return env

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