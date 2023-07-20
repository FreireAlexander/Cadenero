import math
import model.angles
from .tools import isAzimuth, isBearing
from .tools import decimalToStandard
from .deflections import Deflection

class Azimuth(model.angles.Angle):
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

    def __repr__(self):
        return f"Azimut({self.Azimuth})"

    def __str__(self):
        return self.Azimuth

    def __add__(self, other):
        if isinstance(other, self.__class__):
            raise TypeError("It has not sense add Azimuth with Azimuth")
        elif isinstance(other, model.angles.Angle(0).__class__):
            res = self.value + other.value
            return Azimuth(decimalToStandard(res))
        elif isinstance(other, (int, float)):
            res = self.value + other
            return Azimuth(decimalToStandard(res))
    
    def __radd__(self, other):
        if isinstance(other, self.__class__):
            raise TypeError("It has not sense add Azimuth with Azimuth")
        elif isinstance(other, model.angles.Angle(0).__class__):
            res = other.value + self.value
            return Azimuth(decimalToStandard(res))
        elif isinstance(other, (int, float)):
            res = other + self.value 
            return Azimuth(decimalToStandard(res))         