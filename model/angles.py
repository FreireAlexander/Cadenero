import math
import re
from .declinations import Declination
from .tools import isAngle, isBearing, isValid
from .tools import decimalToStandard, setSexageximal, setQuadrant

class Angle(Declination):
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

    def __init__(self, value, orientation=0):
        if isValid(orientation) and isValid(value):
            orientation = Declination(orientation)
            self.orientation = orientation
            magnitude = Declination(value)
            super().__init__(value)
            self.Azimuth_value = decimalToStandard(orientation.Azimuth_value + magnitude.Azimuth_value)
            self.Azimuth_decimal = f"{round(self.Azimuth_value, 4)}°"
            self.Azimuth = setSexageximal(self.Azimuth_value)
            bearing, self.vertical, self.horizontal = setQuadrant(self.Azimuth_value)
            self.Bearing = f'''{self.vertical} {setSexageximal(bearing)} {self.horizontal}'''
            self.Bearing_decimal = f"{self.vertical} {round(bearing,4)}° {self.horizontal}"
            self.Bearing_value = bearing
            self.Radians = math.radians(self.Azimuth_value)
            self.type = 'Angle'
        else:
            raise ValueError(f"{orientation} must be a valid Angle input for reference line")

        def __str__(self):
            return self.Angle

        def __repr__(self):
            return f"Angle({self}, {self.orientation})"