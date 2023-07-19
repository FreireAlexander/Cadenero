import math
from .declinations import Declination
from .tools import isAzimuth, isBearing
from .angles import Angle

class Azimuth(Declination):
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
        if isAzimuth(value):
            super().__init__(value)
            self.type = 'Azimuth'
        else:
            raise ValueError(f"{value} must be an Azimuth valid input")

    def __str__(self):
        return self.Azimuth 

    def __repr__(self):
        return f"Azimut({self.Azimuth})"

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            resta = self.Azimuth_value - other
            return Angle(resta)
        elif isinstance(other, (self.__class__)) or isBearing(str(other)):
            value = self.Azimuth_value - other.Azimuth_value
            meridian = other.Azimuth_value
            return Angle(value, meridian)