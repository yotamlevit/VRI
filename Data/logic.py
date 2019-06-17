# -*- coding: utf-8 -*-
global right
global left

def init():
    global right
    global left
    right = False
    left = False

def logic(lap, robot):
    global right
    global left
    #trying to get left and fight equal
    print(lap)
    sen_12_sub = abs(robot.ultrasonic[1].distance) - abs(robot.ultrasonic[2].distance)
    print(sen_12_sub)
    if lap < 2050:
        if right and left:
            right = False
            left = False
            return 'w'
        elif abs(robot.ultrasonic[1].distance) < 3:
            right = True
            return 'd'
        elif abs(robot.ultrasonic[2].distance) < 3:
            left = True
            return 'a'
        #elif robot.ultrasonic[1].distance < 0 and abs(robot.ultrasonic[5].distance) > 10:
        #    return 'w'
        elif sen_12_sub > 3:
            left = True
            return 'a'
        elif sen_12_sub < -3:
            print('1111111111')
            right = True
            return 'd'
        elif abs(robot.ultrasonic[5].distance) > 10:
            right = False
            left = False
            return 'w'
    """
    #fail ai
    sen_12_sub = abs(robot.ultrasonic[1].distance) - abs(robot.ultrasonic[2].distance)
    print(sen_12_sub)
    if right and left:
        right = False
        left = False
        return 'w'
    elif abs(robot.ultrasonic[1].distance) < 3:
        right = True
        return 'd'
    elif abs(robot.ultrasonic[2].distance) < 3:
        left = True
        return 'a'
    #elif robot.ultrasonic[1].distance < 0 and abs(robot.ultrasonic[5].distance) > 10:
    #    return 'w'
    elif sen_12_sub > 3 and (abs(robot.ultrasonic[5].distance) < 70 or robot.ultrasonic[5].distance < 0):
        left = True
        return 'a'
    elif sen_12_sub < -3 and (abs(robot.ultrasonic[5].distance) < 70 or robot.ultrasonic[5].distance < 0):
        print('1111111111')
        right = True
        return 'd'
    elif abs(robot.ultrasonic[5].distance) > 10:
        right = False
        left = False
        return 'w'
    return 'w'
    """
    return None