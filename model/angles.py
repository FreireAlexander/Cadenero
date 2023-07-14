import math
import re
from .meridians import Meridian
from .tools import isAngle, isBearing

class Angle:
    """
    Estos objetos son ángulos en el sentido de las manecillas del reloj a partir del Norte, 
    Es decir, son exclusivamentes azimutes por el momento, pueden ser escritos de la sgte manera.
    Siguiendo la notación de los ángulos en grados, minutos y segundos o de forma numeríca, para
    la separación entre grados minutos o segundos se puede utilizar lso caracteres de ° o ' para 
    los grados o los minutos y el caracter de " para los segundos, es obligatorio ponerlo si o sí 
    para que el programa identifique si se trata de un ángulo con grados, grados y minutos o grados, 
    minutos y segundos.
    1. numero entero 
    2. numero decimal
    3. numero decimal + ' o ° cualquiera de los dos
    4. numero entero + ' o ° + numero decimal o entero + ° o ' 
    5. numero entero + ' o ° + numero entero [entre 0 a 59] + ° o ' + numero decimal o entero entre 0 y 59 + ' o ° o "
    """
    value = None

    def __init__(self, value, meridian=Meridian(0)):
        self.rotation = meridian 
        if isAngle(value) or isBearing(value):
            if isAngle(value): self.type = 'Angle'
            if isBearing(value): self.type = 'Bearing'
            params = Angle.setAngle(value)
            self.sign = params['sign']
            self.spin_number = params['spin_number']
            self.spin_number_decimal = params['spin_number_decimal']   
            self.degree_decimals = params['degree_decimals']
            self.degree = params['degree']
            self.degree_standard = params['degree_standard']
            self.minutes_decimals = params['minutes_decimals']
            self.minutes = params['minutes']
            self.seconds = params['seconds']
            self.vertical = params['vertical']
            self.horizontal = params['horizontal']
            self.decimal = params['decimal']
            self.standard = Angle.setStandard(self)
        else:
            raise ValueError(f'Could not convert {value} to Angle')
    
    def __repr__(self):
        """
        Esta función imprime de manera organizada el Azimut en el formato de 
        grados, minutos y segundos. 
        """
        if self.type in ['Azimuth', 'Angle']:
            return f'''{self.sign}{self.degree}°{self.minutes}'{round(self.seconds,3)}"'''
        if self.type == 'Bearing':
            return f'''{self.vertical}{self.degree}°{self.minutes}'{round(self.seconds,3)}{self.horizontal}"'''

    def __add__(self, otherAngle):
        if otherAngle.type in ['Azimuth', 'Angle']:
            return Angle(str(self.decimal+otherAngle.decimal))
        elif type(otherAngle) in [type(1), type(3.14)]:
            return Angle(str(self.decimal+otherAngle))

    def __radd__(self, other):
        if type(other) in [type(1), type(3.14)]:
            return Angle(str(self.decimal+other))
        elif other.type in ['Azimuth', 'Angle']:
            return Angle(str(self.decimal+other.decimal))

    def setAngle(angle):
        precision = 6
        params = {
            'raw_angle': angle,
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
        }
        if angle == ' ':
            return params
        angle, params['vertical'], params['horizontal'] = Angle.getQuadrant(angle)
        numbers = angle.replace(" ", "").replace("'", "°").replace('"', '°').replace("°", " ").split(' ')
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
    
    def getQuadrant(angle):
        angle = angle.lower().replace(" ", "")
        vertical = ''
        horizontal = ''
        if re.match(r"([sS]{1}|(sur|south))", angle):
            vertical = 'S'
            angle = angle.replace("sur", "").replace("south", "")
        if re.match(r"([nN]{1}|(norte|north))", angle):
            vertical = 'N'
            angle = angle.replace("norte", "").replace("north", "")
        if re.search(r"([wWoO]{1}|(oeste|west))", angle):
            horizontal = 'W'
            angle = angle.replace("oeste", "").replace("west", "")
        if re.search(r"([eE]{1}|(este|east))", angle):
            horizontal = 'E'
            angle = angle.replace("este", "").replace("east", "")
        
        angle = angle.replace("s", "").replace("n", "").replace("w", "").replace("o", "").replace("e", "")
        return angle, vertical, horizontal
    
    def setStandard(self):
        """
        Esta función imprime de manera organizada el Azimut en el formato de 
        grados, minutos y segundos. 
        """
        if self.type in ['Azimuth', 'Angle']:
            return f'''{self.sign}{self.degree_standard}°{self.minutes}'{self.seconds}"'''
        if self.type == 'Bearing':
            return f'''{self.vertical}{self.degree_standard}°{self.minutes}'{self.seconds}{self.horizontal}"'''
