# -*- coding: utf-8 -*-
global right
global left
right = False
left = False

def logic(lap, robot):
    global right
    global left
    #print(right)
    #print(left)
    print(round(robot.ultrasonic[1].distance))
    print(round(robot.ultrasonic[2].distance))
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
    if lap < 20:
        return 'w'
    if round(robot.ultrasonic[4].distance) == round(robot.ultrasonic[6].distance) and (robot.ultrasonic[5].distance > 10 or robot.ultrasonic[5].distance < 0):
        return 'w'
    elif robot.ultrasonic[1].distance < 5:
        return 'd'
    elif round(robot.ultrasonic[2].distance) > round(robot.ultrasonic[1].distance) and abs(robot.ultrasonic[2].distance - robot.ultrasonic[1].distance) > 3:
        return 'd'
    else:
        return 'w'
    """
    if right or left:
        right = False
        left = False
        return 'w'
    elif round(robot.ultrasonic[4].distance) == round(robot.ultrasonic[6].distance) and (robot.ultrasonic[5].distance > 10 or robot.ultrasonic[5].distance < 0):
            return 'w'
    elif (round(robot.ultrasonic[4].distance) > round(robot.ultrasonic[6].distance) and round(robot.ultrasonic[1].distance) < round(robot.ultrasonic[3].distance))or(round(robot.ultrasonic[4].distance) < round(robot.ultrasonic[6].distance)and round(robot.ultrasonic[1].distance) > round(robot.ultrasonic[3].distance)) and (robot.ultrasonic[5].distance > 10 or robot.ultrasonic[5].distance < 0) :
        return 'w'
    elif robot.ultrasonic[1].distance > robot.ultrasonic[2].distance:
        right = True
        return 'a'
    elif robot.ultrasonic[1].distance < robot.ultrasonic[2].distance:
        left = True
        return 'd'
    """
    #if robot.ultrasonic[1].distance > 10 and robot.ultrasonic[2].distance > 10 and robot.ultrasonic[5].distance < 0:
    #    print(1)
    #return 's'
    # if lap < 160:
    #     return 's'
    # elif 160 < lap <= 250:
    #     return 'd'
    #if 180 <= lap <2000:
     #   return 'w'
    #if 200 <= lap < 3000:
     #   return 's'
    return None