# -*- coding: utf-8 -*-
from Wall import Wall
import analytic_geometry as ag
class Environment:

    def __init__(self):
        self.objects = {}

    def add_obj(self, obj):
        self.objects[str(id(obj))] = obj

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

    def __str__(self):
        return "Objects are: {}".format(self.objects)

def main():
    """
    Add Documentation here
    """
    v = ag.Vector(ag.Point(100,100), 100, 20)
    w = Wall(v, 10)
    e = Environment()
    e.add_obj(w)
    print e.__str__()
    e.delete_obj(id(w))
    print e.__str__()
    print id(w)
    e.add_obj(w)
    e.clear_environment()
    print e.__str__()
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()