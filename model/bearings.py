import math
from .tools import isBearing, setAttributes, decimalToStandard
import model.angles


class Bearing:
    """
    Estos objetos son Rumbos en toda su definición, 
    Es decir, que es necesario escribir su cuadrante en la notación.
    Norte o Sur + ángulo en grados, minutos y segundos + Este u Oeste.
    De manera similar a los acimutes se tendrían las siguientes maneras de escribirlos, 
    recordando claro que al inicio y al final se debe especificar el cuadrante vertical al inicio y 
    el cuadrante horizontal al final:
    1. [Norte o Sur] numero entero  [Este u Oeste]
    2. [Norte o Sur] numero decimal [Este u Oeste]
    3. [Norte o Sur] numero decimal + ' o ° cualquiera de los dos [Este u Oeste]
    4. [Norte o Sur] numero entero + ' o ° + numero decimal o entero + ° o '  [Este u Oeste]
    5. [Norte o Sur] numero entero + ' o ° + numero entero [entre 0 a 59] + ° o ' 
        + numero decimal o entero entre 0 y 59 + ' o ° o " [Este u Oeste]
    """
    def __init__(self, value):
        if isBearing(value):
            attrs = setAttributes(value)
            self.sign               = attrs['sign']
            self.rotations          = attrs['rotations']
            self.rotations_value    = attrs['rotations_value']
            self.degree_decimals    = attrs['degree_decimals']
            self.degree             = attrs['degree']
            self.minutes_decimals   = attrs['minutes_decimals']
            self.minutes            = attrs['minutes']
            self.seconds_decimals   = attrs['seconds_decimals']
            self.seconds            = attrs['seconds']
            self.vertical           = attrs['vertical']
            self.horizontal         = attrs['horizontal']
            self.Standard           = attrs['Standard']
            self.Standard_value     = attrs['Standard_value']
            self.Counter            = attrs['Counter']
            self.Angle              = attrs['Angle']
            self.Angle_decimal      = attrs['Angle_decimal']
            self.value              = attrs['value']
            self.Bearing            = attrs['Bearing']
            self.Bearing_decimal    = attrs['Bearing_decimal']
            self.Bearing_value      = attrs['Bearing_value']
            self.Azimuth            = attrs['Azimuth']
            self.Azimuth_decimal    = attrs['Azimuth_decimal']
            self.Azimuth_value      = attrs['Azimuth_value']
            self.Radians            = attrs['Radians']
            self.type               = 'Angle'
        else:
            raise ValueError(f"{value} must be a valid Angle or Bearing, even integer or float are allowed")
    
    def __repr__(self):
        return f"Angle({self.Angle})"

    def __str__(self):
        return self.Angle

    def __add__(self, other):
        if isinstance(other, self.__class__):
            raise TypeError("It has not sense add Azimuth with Azimuth")
        elif isinstance(other, model.angles.Angle(0).__class__):
            res = other.value + self.Azimuth_value
            print(f"Desde Bearing \n El valor de Res para la suma de angulo y bearing es {res}")
            res = setAttributes(decimalToStandard(res))['Bearing']
            print(f"Supuesto Rumbo")
            return Bearing(res)
        
    
    def __radd__(self, other):
        if isinstance(other, self.__class__):
            raise TypeError("It has not sense add Azimuth with Azimuth")
        elif isinstance(other, model.angles.Angle(0).__class__):
            res = other.value + self.Azimuth_value
            print(f"Desde Bearing \n El valor de Res para la suma de angulo y bearing es {res}")
            res = setAttributes(decimalToStandard(res))['Bearing']
            print(f"Supuesto Rumbo")
            return Bearing(res)
        
