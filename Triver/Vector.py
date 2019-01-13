# -*- coding: utf-8 -*-

class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def change_length(self, length):
        self.length = length

    def change_angle(self, angle):
        self.angle = angle

    def show_data(self):
        return "length- " + str(self.length) + ' | ' + 'angle- ' + str(self.angle)
def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()