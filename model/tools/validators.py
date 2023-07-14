import re
from .patterns import *

def isAngle(angle: str):
    flag = False
    if isPositiveAngle(angle):
        flag = True
    if isNegativeAngle(angle):
        flag = True 
    return flag    

def isPositiveAngle(angle: str):
    flag = False
    if re.match(p_integer, angle):
        flag = True
    if re.match(p_decimal, angle):
        flag = True
    if re.match(p_angle_d, angle):
        flag = True
    if re.match(p_angle_dm, angle):
        flag = True
    if re.match(p_angle_dms, angle):
        flag = True
    return flag

def isNegativeAngle(angle: str):
    flag = False
    if re.match(p_integer_n, angle):
        flag = True
    if re.match(p_decimal_n, angle):
        flag = True
    if re.match(p_angle_d_n, angle):
        flag = True
    if re.match(p_angle_dm_n, angle):
        flag = True
    if re.match(p_angle_dms_n, angle):
        flag = True 
    return flag

def isAzimuth(angle):
    flag = False
    if re.match(p_azimuth_integer, angle):
        flag = True
    if re.match(p_azimuth_decimal, angle):
        flag = True
    if re.match(p_azimuth_d, angle):
        flag = True
    if re.match(p_azimuth_dm, angle):
        flag = True
    if re.match(p_azimuth_dms, angle):
        flag = True
    return flag   

def isBearing(angle):
    flag = False
    if re.match(p_bearing_vertical, angle):
        flag = True
    if re.match(p_bearing_dm_vertical, angle):
        flag = True
    if re.match(p_bearing_dms_vertical, angle):
        flag = True
    if re.match(p_bearing_d, angle):    
        flag = True
    if re.match(p_bearing_dm, angle):    
        flag = True
    if re.match(p_bearing_dms, angle):    
        flag = True
    return flag 


