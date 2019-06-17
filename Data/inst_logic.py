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