# -*- coding: utf-8 -*-

def logic(lap):
    if lap < 160:
        return 's'
    elif 160 < lap <= 250:
        return 'd'
    #if 180 <= lap <2000:
     #   return 'w'
    #if 200 <= lap < 3000:
     #   return 's'
    return None