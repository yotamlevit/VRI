# -*- coding: utf-8 -*-
import pygame
import time

pygame.init()
pygame.joystick.init()
count = pygame.joystick.get_count()
print "Joystick count:",count
if count>0:
    j=pygame.joystick.Joystick(0)
    j.init()
    if j.get_init():
        print "Joystick name: ",j.get_name()
        n=j.get_numbuttons()
        print j.get_numaxes()
        while True:
            pygame.event.pump()
            #print j.get_axis(0)
            #print j.get_axis(1)
            print j.get_axis(2)
            time.sleep(1)
    """
    while 1:
        pygame.event.pump()
        for i in range(n):
            if j.get_button(i):
                print "Joystick, pressed: ",i
                """
else:
    print "No joystick, BYE!! \a \a"
pygame.quit()
def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()