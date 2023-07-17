
import re
import math
from .validators import isAngle, isBearing, isAzimuth

precision = 6


def setAngle(value):
        params = {
            'raw_Meridian': value,
            'sign': '',
            'spin_number': 0,
            'spin_number_decimal': 0,
            'decimal': 0, 
            'degree_decimals': 0,
            'degree_standard': 0,
            'degree': 0,
            'minutes_decimals': 0,
            'minutes': 0, 
            'seconds_decimals': 0,
            'seconds': 0,
            'vertical': '',
            'horizontal': '',
            'decimal': 0,
            'DMS': []
        }
        if value == ' ':
            return params
        params['vertical'], params['horizontal'] = getQuadrant(value)
        numbers = value.replace(" ", "").replace("'", "°").replace('"', '°').replace("°", " ").split(' ')
        try:
            numbers.remove('')
        except:
            pass
        degree=float(numbers[0])
        params['spin_number'] = int(abs(degree)// 360)
        params['spin_number_decimal'] = round(abs(degree) / 360, 3)
        params['degree_standard'] = int(math.floor(abs(degree) - 360*params['spin_number']))
        if len(numbers)==1:
            params['degree_decimals'] = abs(degree)
            params['degree'] = int(math.floor(params['degree_decimals']))
            params['minutes_decimals'] = round((params['degree_decimals'] - params['degree'])*60,precision)
            params['minutes'] = int(math.floor(params['minutes_decimals']))
            params['seconds'] = round(float((params['minutes_decimals'] - params['minutes'])*60),precision)
        if len(numbers)==2:
            params['degree_decimals'] = abs(degree)
            params['degree'] = int(math.floor(params['degree_decimals']))
            params['minutes_decimals'] = round(float(numbers[1]),precision)
            params['minutes'] = int(math.floor(params['minutes_decimals']))
            params['seconds'] = round(float((params['minutes_decimals'] - params['minutes'])*60),precision)
        if len(numbers)==3:
            params['degree_decimals'] = abs(degree)
            params['degree'] = int(params['degree_decimals'])
            params['minutes_decimals'] = float(numbers[1])
            params['minutes'] = int(params['minutes_decimals'])
            params['seconds'] = round(float(numbers[2]),precision)
        
        if degree < 0 or numbers[0]=='-0':
            params['sign'] = '-'
            params['decimal'] = (params['degree']+params['minutes']/60+params['seconds']/3600)*-1
        else:
            params['decimal'] = (params['degree']+params['minutes']/60+params['seconds']/3600)
        

        return params



def setSexagesimal(angle):
    if isAngle(angle) or isBearing(angle):
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
    else:
        raise ValueError(f"{meridian} is not valid must be an Angle or bearing")

def toSexagesimal(angle):
    try:
        res = setSexagesimal(angle)
        return f'''{res['sign']}{res['degree']}°{res['minutes']}'{res['seconds']}"'''
    except:
        raise ValueError(f" {angle} must be a int or float")

def getQuadrant(meridian):
    meridian = str(meridian)
    if isAngle(meridian) or isBearing(meridian):
        meridian = meridian.lower().replace(" ", "")
        vertical = ''
        horizontal = ''
        if re.search(r"([sS]{1}|(sur|south))", meridian):
            vertical = 'S'
        if re.search(r"([nN]{1}|(norte|north))", meridian):
            vertical = 'N'
        if re.search(r"([wWoO]{1}|(oeste|west))", meridian):
            horizontal = 'W'
        if re.search(r"([eE]{1}|(este|east))", meridian):
            horizontal = 'E'
        return vertical, horizontal
    else:
        raise ValueError(f"{meridian} is not valid must be an Angle or bearing")

def getValue(value):
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
        raise ValueError(f"{meridian} is not valid must be an Angle or bearing")

def toBearing(decimal):
    numbers = getValue()


def _setQuadrant(decimal):
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

def toAzimuth(decimal, horizontal, vertical):
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


def getDMS(angle):
    angle = str(angle)
    numbers = getValue(angle)
    params = {
            'sign': '',
            'rotations': 0,
            'rotations_decimal': 0,
            'degree_decimals': 0,
            'degree_standard': 0,
            'degree': 0,
            'minutes_decimals': 0,
            'minutes': 0,
            'seconds_decimals': 0,
            'seconds': 0,
            'vertical': '',
            'horizontal': '',
            'decimal': 0,
            'decimal_standard': 0,
            'Angle': None,
            'Bearing': None,
            'Azimuth': None,
            'DMS': []
        }
    
    degree=float(numbers[0])
    params['vertical'], params['horizontal'] = getQuadrant(angle)
    print(degree)
    params['rotations'] = int(abs(degree)// 360)
    params['rotations_decimal'] = round(abs(degree) / 360, 3)
    if len(numbers)==1:
        params['degree_decimals'] = abs(degree)
        params['degree'] = int(math.floor(params['degree_decimals']))
        params['minutes_decimals'] = round((params['degree_decimals'] - params['degree'])*60,precision)
        params['minutes'] = int(math.floor(params['minutes_decimals']))
        params['seconds'] = round(float((params['minutes_decimals'] - params['minutes'])*60),precision)
    if len(numbers)==2:
        params['degree_decimals'] = abs(degree)
        params['degree'] = int(math.floor(params['degree_decimals']))
        params['minutes_decimals'] = round(float(numbers[1]),precision)
        params['minutes'] = int(math.floor(params['minutes_decimals']))
        params['seconds'] = round(float((params['minutes_decimals'] - params['minutes'])*60),precision)
    if len(numbers)==3:
        params['degree_decimals'] = abs(degree)
        params['degree'] = int(params['degree_decimals'])
        params['minutes_decimals'] = float(numbers[1])
        params['minutes'] = int(params['minutes_decimals'])
        params['seconds'] = round(float(numbers[2]),precision)
    
    if degree < 0 or numbers[0]=='-0':
        params['sign'] = '-'
        params['decimal'] = (params['degree']+params['minutes']/60+params['seconds']/3600)*-1
        print(type(params['decimal']))
    else:
        params['decimal'] = params['degree']+params['minutes']/60+params['seconds']/3600
    
    print("todo bien hasta aquí")
    params['decimal_standard'] = params['decimal']
    if params['decimal'] < 0 :
        params['decimal_standard'] = params['decimal'] + 360*(params['rotations']+1)
    if params['decimal'] > 360 :
        params['decimal_standard'] = params['decimal'] - 360*params['rotations']

    if isBearing(angle):
        params['Bearing'] = f'''{params['vertical']} {params['sign']}{params['degree']}°{params['minutes']}'{params['seconds']}" {params['horizontal']}'''
    else:
        bearing, params['vertical'], params['horizontal'] = _setQuadrant(params['decimal_standard'])
        params['Bearing'] = f'''{params['vertical']} {toSexagesimal(bearing)} {params['horizontal']}'''
    
    if isAzimuth(angle):
        params['Azimuth'] = f'''{params['sign']}{params['degree']}°{params['minutes']}'{params['seconds']}"'''
    else:
        azimuth = toAzimuth(params['decimal'], params['horizontal'], params['vertical'])
        params['Azimuth'] = f'''{toSexagesimal(azimuth)}'''

    params['Angle'] = f'''{toSexagesimal(params['decimal_standard'])}'''
    
    print(f"El Angulo Sexagesimal es {params['Angle']}")
    print(f"El rumbo es {params['Bearing']}")
    print(f"El Azimut es {params['Azimuth']}")


    print(f"EL grado en el rango 360° es {toSexagesimal(params['decimal_standard'])}")
    
    return params

    