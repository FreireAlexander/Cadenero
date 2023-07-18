
import re
import math
from .validators import isAngle, isBearing, isAzimuth

precision = 6


def getQuadrant(value):
    value = str(value)
    if isAngle(value) or isBearing(value):
        value = value.lower().replace(" ", "")
        vertical = ''
        horizontal = ''
        if re.search(r"([sS]{1}|(sur|south))", value):
            vertical = 'S'
        if re.search(r"([nN]{1}|(norte|north))", value):
            vertical = 'N'
        if re.search(r"([wWoO]{1}|(oeste|west))", value):
            horizontal = 'W'
        if re.search(r"([eE]{1}|(este|east))", value):
            horizontal = 'E'
        return vertical, horizontal
    else:
        raise ValueError(f"{value} is not valid must be an Angle or bearing")

def setQuadrant(decimal):
    horizontal, vertical = '', ''
    if decimal == 0 or decimal == 360 :
        bearing = 0
        vertical = 'N'
    if decimal > 0 and decimal <=90 :
        bearing = decimal
        vertical = 'N'
        horizontal = 'E'
    if decimal > 90 and decimal < 180 :
        bearing = 180 - decimal
        vertical = 'S'
        horizontal = 'E'
    if decimal == 180 :
        bearing = 0
        vertical = 'S'
    if decimal > 180 and decimal <= 270 :
        bearing = decimal - 180
        vertical = 'S'
        horizontal = 'W'
    if decimal > 270 and decimal < 360 :
        bearing = 360 - decimal
        vertical = 'N'
        horizontal = 'W'

    return bearing, vertical, horizontal

def BearingToAzimuth(decimal, horizontal, vertical):
    azimuth = 0 
    if vertical == 'N' and horizontal == '':
        azimuth = 0
    if vertical == 'N' and horizontal == 'E':
        azimuth = decimal
    if vertical == 'S' and horizontal == 'E':
        azimuth = 180 - decimal
    if vertical == 'S' and horizontal == '':
        azimuth = 180
    if vertical == 'S' and horizontal == 'W':
        azimuth = decimal + 180
    if vertical == 'N' and horizontal == 'W':
        azimuth = 360 - decimal
    
    return azimuth

def getValues(value):
    value = str(value)
    if isAngle(value) or isBearing(value):
        value = value.lower().replace(" ", "")
        value = value.replace("sur", "").replace("south", "")
        value = value.replace("norte", "").replace("north", "")
        value = value.replace("oeste", "").replace("west", "")
        value = value.replace("este", "").replace("east", "")
        value = value.replace("s", "").replace("n", "").replace("w", "").replace("o", "").replace("e", "")
        value = value.replace(" ", "").replace("'", "°").replace('"', '°').replace("°", " ").split(' ')
        try:
            value.remove('')
        except:
            pass
        return value
    else:
        raise ValueError(f"{value} is not valid must be an Angle or bearing")

def decimalToStandard(angle):
    spin = abs(angle)//360
    if angle < 0 :
        spin = spin + 1
        return 360*spin + angle
    elif angle > 360 :
        return angle - 360*spin
    else:
        return angle

def setSexageximal(angle):
    if isAngle(angle):
        try:
            res = {
                        'sign': '',
                        'degree': 0,
                        'degree_decimal': 0,
                        'minutes': 0,
                        'minutes_decimal': 0,
                        'seconds': 0,
                        'seconds_decimal': 0
                }    
            res['degree_decimal'] = abs(angle)
            res['degree'] = int(math.floor(res['degree_decimal']))
            res['minutes_decimal'] = round((res['degree_decimal'] - res['degree'])*60, precision)
            res['minutes'] = int(math.floor(res['minutes_decimal']))
            res['seconds_decimal']= round((res['minutes_decimal'] - res['minutes'])*60, precision)
            res['seconds']= round(res['seconds_decimal'],3)
            if angle < 0: res['sign']='-'
            return f'''{res['sign']}{res['degree']}°{res['minutes']}'{res['seconds']}"'''
        except:
            raise ValueError(f" {angle} must be a int or float")
    else:
        raise ValueError(f"{angle} is not valid must be an Angle or bearing")

def setAngle(angle):
    angle = str(angle)
    numbers = getValues(angle)
    attrs = {
            'sign': '',
            'rotations': 0,
            'rotations_decimal': 0,
            'degree_decimals': 0,
            'degree': 0,
            'minutes_decimals': 0,
            'minutes': 0,
            'seconds_decimals': 0,
            'seconds': 0,
            'vertical': '',
            'horizontal': '',
            'decimal': 0,
            'decimal_standard': 0,
            'Raw': None,
            'Standard': None,
            'Counter': None,
            'Angle': None,
            'Bearing': None,
            'Azimuth': None
        }
    degree = float(numbers[0])
    attrs['rotations'] = abs(degree)// 360
    attrs['rotations_decimal'] = round(abs(degree) / 360, 3)
    if len(numbers) == 1:
        attrs['degree_decimals'] = abs(degree)
        attrs['degree'] = int(math.floor(attrs['degree_decimals']))
        attrs['minutes_decimals'] = round((attrs['degree_decimals'] - attrs['degree'])*60,precision)
        attrs['minutes'] = int(math.floor(attrs['minutes_decimals']))
        attrs['seconds'] = round(float((attrs['minutes_decimals'] - attrs['minutes'])*60),3)
    if len(numbers) == 2:
        attrs['degree_decimals'] = abs(degree)
        attrs['degree'] = int(math.floor(attrs['degree_decimals']))
        attrs['minutes_decimals'] = round(float(numbers[1]),precision)
        attrs['minutes'] = int(math.floor(attrs['minutes_decimals']))
        attrs['seconds'] = round(float((attrs['minutes_decimals'] - attrs['minutes'])*60),3)
    if len(numbers) == 3:
        attrs['degree_decimals'] = abs(degree)
        attrs['degree'] = int(attrs['degree_decimals'])
        attrs['minutes_decimals'] = float(numbers[1])
        attrs['minutes'] = int(attrs['minutes_decimals'])
        attrs['seconds'] = round(float(numbers[2]),3)
    
    # Los indices de los cuadrantes
    attrs['vertical'], attrs['horizontal'] = getQuadrant(angle)
    
    if degree < 0 or numbers[0]=='-0':
        attrs['sign'] = '-'
        attrs['decimal'] = (attrs['degree']+attrs['minutes']/60+attrs['seconds']/3600)*-1
        print(type(attrs['decimal']))
    else:
        attrs['decimal'] = attrs['degree']+attrs['minutes']/60+attrs['seconds']/3600
    
    standard = decimalToStandard(attrs['decimal'])
    
    attrs['Raw'] =  f'''{attrs['vertical']} {setSexageximal(attrs['decimal'])} {attrs['horizontal']}'''

    if isAzimuth(angle):
        azimuth = attrs['decimal']
        attrs['Azimuth'] = setSexageximal(attrs['decimal'])
    else:
        if isBearing(angle):
            azimuth = BearingToAzimuth(attrs['decimal'], attrs['horizontal'], attrs['vertical'])
            attrs['Azimuth'] = setSexageximal(azimuth)
        if isAngle(angle):
            azimuth = standard
            attrs['Azimuth'] = setSexageximal(azimuth)
    
    if isBearing(angle):
        attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(attrs['decimal'])} {attrs['horizontal']}'''
    else:
        if isAngle(angle):
            bearing, attrs['vertical'], attrs['horizontal'] = setQuadrant(standard)
            attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(bearing)} {attrs['horizontal']}'''
        if isAzimuth(angle):
            bearing, attrs['vertical'], attrs['horizontal'] = setQuadrant(standard)
            attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(bearing)} {attrs['horizontal']}'''
    
    attrs['Standard'] = attrs['Azimuth']
    attrs['Counter'] = setSexageximal(azimuth-360)
    attrs['Angle'] = attrs['Raw']
    
    return attrs

    