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
    #pre programed
    """
    if lap < 450:
        return 'w'
    if 450 < lap <= 540:
        return 'd'
    if 540 < lap <= 640:
        return 'w'
    if 640 < lap <= 730:
        return 'd'
    if 730 < lap <= 1180:
        return 'w'
    if 1180 < lap <= 1270:
        return 'a'
    if 1270 < lap <= 1320:
        return 'w'
    if 1320 < lap <= 1365:
        return 'a'
    if 1365 < lap <= 1700:
        return 'w'
    return None
    """
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