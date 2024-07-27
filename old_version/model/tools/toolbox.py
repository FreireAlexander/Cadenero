
import re
import math
from .validators import isAngle, isBearing, isAzimuth

precision = 6

def getQuadrant(value):
    """
    Esta función permite extraer el cuadrante del valor
    digitado, si no es un Rumbo, regresará dos cadenas vacias
    """
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
        raise ValueError(f"{value} is not valid must be an Angle or Bearing")

def setQuadrant(decimal):
    if type(decimal) in [type(1), type(2.3)]:
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
    else:
        raise ValueError(f"{decimal} is not valid, it must be an Angle or Bearing input") 

def getAzimuthFromBearing(decimal, horizontal, vertical):
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

def _getValues(angle):
    """
    Esta función separa los valores de los grados, minutos y segundos 
    digitados por el usuario
    """
    angle = str(angle)
    if isAngle(angle) or isBearing(angle):
        angle = angle.lower().replace(" ", "")
        angle = angle.replace("sur", "").replace("south", "")
        angle = angle.replace("norte", "").replace("north", "")
        angle = angle.replace("oeste", "").replace("west", "")
        angle = angle.replace("este", "").replace("east", "")
        angle = angle.replace("s", "").replace("n", "").replace("w", "").replace("o", "").replace("e", "")
        angle = angle.replace(" ", "").replace("'", "°").replace('"', '°').replace("°", " ").split(' ')
        try:
            angle.remove('')
        except:
            pass
        return angle
    else:
        raise ValueError(f"{angle} is not valid, it must be an Angle or Bearing input")

def decimalToStandard(angle):
    try:
        spin = abs(angle)//360
        if angle < 0 :
            spin = spin + 1
            return 360*spin + angle
        elif angle > 360 :
            return angle - 360*spin
        else:
            return angle
    except:
        raise ValueError(f"{angle} is not valid, it must be an intteger or float")

def setSexageximal(angle):
    if type(angle) in [type(1), type(2.3)]:
        res = {
                    'sign': '',
                    'degree': 0,
                    'degree_value': 0,
                    'minutes': 0,
                    'minutes_value': 0,
                    'seconds': 0,
                    'seconds_value': 0
            }    
        res['degree_value'] = abs(angle)
        res['degree'] = int(math.floor(res['degree_value']))
        res['minutes_value'] = round((res['degree_value'] - res['degree'])*60, precision)
        res['minutes'] = int(math.floor(res['minutes_value']))
        res['seconds_value']= round((res['minutes_value'] - res['minutes'])*60, precision)
        res['seconds']= round(float(res['seconds_value']),3)
        if angle < 0: res['sign']='-'
        return f'''{res['sign']}{res['degree']}°{res['minutes']}'{res['seconds']}"'''
    else:
        raise ValueError(f"{angle} must be an integer or float")


def setAttributes(angle):
    """
    Esta Función permite calcular los atributos de un ángulo, 
    desde, azimuths, rumbos, angulo en sentido de las manecillas del reloj, 
    equivalente en radianes entre otro.
    """
    numbers = _getValues(angle)  
    attrs = {
            'sign': '',
            'rotations': 0,
            'rotations_value': 0,
            'degree_decimals': 0,
            'degree': 0,
            'minutes_decimals': 0,
            'minutes': 0,
            'seconds_decimals': 0,
            'seconds': 0,
            'vertical': '',
            'horizontal': '',
            'Standard': None,
            'Standard_value': 0,
            'Counter': None,
            'Counter_value': 0,
            'Angle': None,
            'Angle_decimal': None,
            'value': 0,
            'Bearing': None,
            'Bearing_decimal': None,
            'Bearing_value': 0,
            'Azimuth': None,
            'Azimuth_decimal': None,
            'Azimuth_value': 0,
            'Radians': 0
            }
    degree = round(float(numbers[0]),6)
    attrs['rotations'] = abs(degree)// 360
    attrs['rotations_value'] = round(abs(degree) / 360, 3)
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
        attrs['value'] = (attrs['degree']+attrs['minutes']/60+attrs['seconds']/3600)*-1
    else:
        attrs['value'] = attrs['degree']+attrs['minutes']/60+attrs['seconds']/3600
    
    attrs['Angle'] = f'''{attrs['vertical']} {setSexageximal(attrs['value'])} {attrs['horizontal']}'''
    attrs['Angle_decimal'] = f'''{attrs['vertical']} {round(attrs['value'],4)}° {attrs['horizontal']}'''
    standard = decimalToStandard(attrs['value'])

    if isAzimuth(angle):
        azimuth = attrs['value']
        attrs['Azimuth'] = setSexageximal(attrs['value'])
    else:
        if isBearing(angle):
            azimuth = getAzimuthFromBearing(attrs['value'], attrs['horizontal'], attrs['vertical'])
            attrs['Azimuth'] = setSexageximal(azimuth)
        if isAngle(angle):
            azimuth = standard
            attrs['Azimuth'] = setSexageximal(azimuth)
    
    attrs['Radians'] = math.radians(azimuth)
    attrs['Azimuth_value'] = azimuth
    attrs['Azimuth_decimal'] = f"{round(azimuth, 4)}°"

    if isBearing(angle):
        bearing = attrs['value']
        attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(attrs['value'])} {attrs['horizontal']}'''
        attrs['value'] = attrs['Azimuth_value']
    else:
        if isAngle(angle):
            bearing, attrs['vertical'], attrs['horizontal'] = setQuadrant(standard)
            attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(bearing)} {attrs['horizontal']}'''
            
        if isAzimuth(angle):
            bearing, attrs['vertical'], attrs['horizontal'] = setQuadrant(standard)
            attrs['Bearing'] = f'''{attrs['vertical']} {setSexageximal(bearing)} {attrs['horizontal']}'''
            
    
    attrs['Bearing_value'] = bearing
    attrs['Bearing_decimal'] = f"{attrs['vertical']} {round(bearing,4)}° {attrs['horizontal']}"
    
    attrs['Standard'] = attrs['Azimuth']
    attrs['Standard_value'] = standard
    attrs['Counter'] = setSexageximal(azimuth-360)
    
    
    return attrs