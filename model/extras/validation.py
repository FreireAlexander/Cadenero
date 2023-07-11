import re
from .patterns import *

def isAngle(text: str):
    flag = False
    if re.match(p_integer, text):
        flag = True
    if re.match(p_decimal, text):
        flag = True
    if isAzimuth(text):
        flag = True   
    return flag    
    
def isAzimuth(angle):
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

def isBearing(angle):
    flag = False
    if re.match(p_bearing_vertical, angle):
        flag = True
    if re.match(p_bearing_d, angle):    
        flag = True
    if re.match(p_bearing_dm, angle):    
        flag = True
    if re.match(p_bearing_dms, angle):    
        flag = True
    return flag 


