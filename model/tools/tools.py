
import re
from .validators import isAngle, isBearing

def setSexagesimal(angle):
    try:
        res = {
                    'sign': '',
                    'degree': 0,
                    'degree_decimal': 0,
                    'minutes': 0,
                    'minutes_decimal': 0,
                    'seconds': 0,
                    'seconds_decimals': 0
            }
        if angle < 0:
            res['sign']='-'
            angle *= -1
        res['degree'] = int(angle)
        res['degree_decimal'] = float(angle)
        res['minutes'] = int((res['degree_decimal'] - res['degree'])*60)
        res['minutes_decimal'] = (res['degree_decimal'] - res['degree'])*60
        res['seconds']= round(float(((angle - res['degree'])*60 - res['minutes'])*60),6)
        res['seconds_decimal']= round(float(((angle - res['degree'])*60 - res['minutes'])*60),6)
        return res
    except:
        raise ValueError(f" {angle} must be a int or float")

def toSexagesimal(angle):
    try:
        res = setSexagesimal(angle)
        return f'''{res['sign']}{res['degree']}°{res['minutes']}'{res['seconds']}"'''
    except:
        raise ValueError(f" {angle} must be a int or float")

def getQuadrant(meridian):
    if isAngle(meridian) or isBearing(meridian):
        meridian = meridian.lower().replace(" ", "")
        vertical = ''
        horizontal = ''
        if re.search(r"([sS]{1}|(sur|south))", meridian):
            vertical = 'S'
            meridian = meridian.replace("sur", "").replace("south", "")
        if re.search(r"([nN]{1}|(norte|north))", meridian):
            vertical = 'N'
            meridian = meridian.replace("norte", "").replace("north", "")
        if re.search(r"([wWoO]{1}|(oeste|west))", meridian):
            horizontal = 'W'
            meridian = meridian.replace("oeste", "").replace("west", "")
        if re.search(r"([eE]{1}|(este|east))", meridian):
            horizontal = 'E'
            meridian = meridian.replace("este", "").replace("east", "")
        
        meridian = meridian.replace("s", "").replace("n", "").replace("w", "").replace("o", "").replace("e", "")
        return meridian, vertical, horizontal
    else:
        raise ValueError(f"{meridian} is not valid must be an angle or bearing")

