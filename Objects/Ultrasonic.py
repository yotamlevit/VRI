# -*- coding: utf-8 -*-

from analytic_geometry.StraightLine import StraightLine
from analytic_geometry.Vector import Vector
from analytic_geometry.Point import Point
import sys
from analytic_geometry import Point as p
from Error import Error

class Ultrasonic(StraightLine):
    def __init__(self, pos, point, angle):
        self.pos = pos
        vec = Vector(200, angle)
        self.distance = sys.maxsize * -1
        super(Ultrasonic, self).__init__(point, vec)

    def update_distance(self, env_obj, bounder):
        bool_senc = False
        for obj in env_obj:
            env_object = env_obj[obj]
            shape_line = env_object.shape.get_lines()
            for line in shape_line:
                collide = self.is_Colliding(line)
                if collide[0]:
                    try:
                        y = self.fc(collide[1])
                    except:
                        y = line.fc(collide[1])
                    p = Point(collide[1], y)
                    temp_dis = self.start_point.distance(p)
                    if not bool_senc:
                        self.distance = temp_dis
                        bool_senc = True
                    elif self.distance > temp_dis:
                        self.distance = temp_dis
        for line in bounder.get_lines():
            collide = self.is_Colliding(line)
            if collide[0]:
                try:
                    y = self.fc(collide[1])
                except:
                    y = line.fc(collide[1])
                p = Point(collide[1], y)
                temp_dis = self.start_point.distance(p)
                if not bool_senc:
                    self.distance = temp_dis
                    bool_senc = True
                elif self.distance > temp_dis:
                    self.distance = temp_dis
        if not bool_senc:
            self.distance = sys.maxsize * -1
    def update_ultrasonic(self, robot_frame):
        self.update_line(robot_frame.pos[self.pos], Vector(200, robot_frame.get_ultrasonic_angle(self.pos)))

    def draw(self, canvas):
        canvas.create_line(self.start_point. x,self.start_point.y, self.end_point.x, self.end_point.y, fill="red")

    def convert_ultrasonic_to_txt(self):
        return '<Ultrasonic><pos>' + str(self.pos) + '</pos></Ultrasonic>'

    @staticmethod
    def ultrasonic_from_file(root, robot):
        pos = (False, None)
        for child in root:
            tag = child.tag.lower()
            if tag == 'pos':
                try:
                    pos = (True, int(child.text))
                except ValueError:
                    print(Error.error.get('us_1pos'))
                    return False, [Error.error.get('us_1pos')]
        if pos[0]:
            point = robot.shape.pos[pos[1]]
            angle = robot.shape.get_ultrasonic_angle(pos[1])
            return True, Ultrasonic(pos[1], point, angle)
        er = []
        if not pos[0]:
            er.append(Error.error.get('us_0pos'))
        return False, er

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()