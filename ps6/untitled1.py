#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:58:52 2018

@author: seongjaegyeong
"""

def find_net_force(list_ins_force):
    total_horizontal = 0
    total_vertical = 0
    for force in list_ins_force:
            total_horizontal += force.get_horizontal() 
            total_vertical += force.get_vertical() 
    find_net_force.magnitude = round((total_horizontal ** 2 + total_vertical ** 2) ** 0.5 ,1 )    
    
    def get_angle():
        angle = round(degrees(atan2(total_vertical, total_horizontal)), 1)
        return angle