import math
import re
from .tools import isAngle, isBearing, isAzimuth
from .tools import setAttributes, decimalToStandard
import model.bearings
import model.azimuths

class Angle:
    """
    Esta clase define la diferencia entre el Norte Geografico o Verdadero y el Norte relativo
    Utilizado como orientación de partida para la medición de los ángulos, todas las declinaciones se miden
    desde el norte geográfico. Además, representan la orientación del lado inicial del ángulo.
    Deben ser escritos de la sgte manera.
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
        if isAngle(value):
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
            self.type               = 'Bearing'
        else:
            raise ValueError(f"{value} must be a valid Angle or Bearing, even integer or float are allowed")
    
    def __repr__(self):
        return f"Angle({self.Angle})"

    def __str__(self):
        return self.Angle

    def __add__(self, other):
        if isinstance(other, self.__class__):
            value = self.value + other.value
            return Angle(value)
        elif isinstance(other, model.bearings.Bearing('N0').__class__):
            res = other.value + self.Azimuth_value
            print(f"Desde Angle \n El valor de Res para la suma de angulo y bearing es {res}")
            res = setAttributes(decimalToStandard(res))['Bearing']
            print(f"Supuesto Rumbo")
            return model.bearings.Bearing(res)
        elif isinstance(other, model.azimuths.Azimuth(0).__class__):
            res = self.value + other.value
            return model.azimuths.Azimuth(decimalToStandard(res))
        elif isinstance(other, (int, float)):
            res = self.value + other
            return Angle(res)
    
    def __radd__(self, other):
        if isinstance(other, self.__class__):
            value = other.value + self.value 
            return Angle(value)
        elif isinstance(other, model.bearings.Bearing('N0').__class__):
            res = other.value + self.Azimuth_value
            print(f"Desde Angle \n El valor de Res para la suma de angulo y bearing es {res}")
            res = setAttributes(decimalToStandard(res))['Bearing']
            print(f"Supuesto Rumbo")
            return model.bearings.Bearing(res)
        elif isinstance(other, model.azimuths.Azimuth(0).__class__):
            res = self.value + other.value
            return model.azimuths.Azimuth(decimalToStandard(res))
        elif isinstance(other, (int, float)):
            res = other + self.value 
            return Angle(res)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            value = self.value - other.value
            return Angle(value)
        elif isinstance(other, (int, float)):
            res = self.value - other
            return Angle(res)

    def __rsub__(self, other):
        if isinstance(other, self.__class__):
            value = other.value - self.value
            return Angle(value)
        elif isinstance(other, (int, float)):
            res = other - self.value
            return Angle(res)