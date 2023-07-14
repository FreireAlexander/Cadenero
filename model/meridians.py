import math
import re
from .tools import isAngle, isBearing, isAzimuth

precision = 6

class Meridian:
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
    
    def __init__(self, value):
        if type(value)!=type('letters'):
            value = str(value)
        if isAngle(value) or isBearing(value):
            if isBearing(value): 
                self.type = 'Bearing'
            elif isAngle(value):
                self.type = 'Angle'
            elif isAzimuth(value):
                self.type = 'Azimuth'
            params = Meridian.setMeridian(value)
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
            self.standard = round(Meridian.setStandard(self), precision)
        else:
            raise ValueError(f'{value} is not valid, must be a int, float or valid str form for an angle')
    
    def __repr__(self):
        """
        Estos angulos sexagesimales siempre estaran entre 0 a 360 
        """
        return f'''{self.degree}°{self.minutes}'{round(self.seconds,3)}"'''
        

    def __add__(self, otherMeridian):
        if otherMeridian.type in ['Azimuth', 'Meridian']:
            return Meridian(str(self.decimal+otherMeridian.decimal))
        elif type(otherMeridian) in [type(1), type(3.14)]:
            return Meridian(str(self.decimal+otherMeridian))

    def __radd__(self, other):
        if type(other) in [type(1), type(3.14)]:
            return Meridian(str(self.decimal+other))
        elif other.type in ['Azimuth', 'Meridian']:
            return Meridian(str(self.decimal+other.decimal))

    def setMeridian(value):
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
        }
        if value == ' ':
            return params
        value, params['vertical'], params['horizontal'] = Meridian.getQuadrant(value)
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
    
    def getQuadrant(meridian):
        meridian = meridian.lower().replace(" ", "")
        vertical = ''
        horizontal = ''
        if re.match(r"([sS]{1}|(sur|south))", meridian):
            vertical = 'S'
            meridian = meridian.replace("sur", "").replace("south", "")
        if re.match(r"([nN]{1}|(norte|north))", meridian):
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
    
    def setStandard(self):
        if self.type == 'Bearing':
            return self.decimal
        else: 
            if self.decimal < 0:
                return 360*(abs(self.decimal)//360+1) + self.decimal
            elif self.decimal > 360:
                return self.decimal - 360*(abs(self.decimal)//360)
            else:
                return self.decimal
