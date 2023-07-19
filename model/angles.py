import math
import re
from .declinations import Declination
from .tools import isAngle, isBearing

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

    def __init__(self, value, meridian=0):
        if isAngle(meridian):
            self.meridian = Declination(meridian)
            if isAngle(value):
                super().__init__(value)
                self.type = 'Angle'
            else:
                raise ValueError(f"{value} must be a valid Angle input")
        else:
            raise ValueError(f"{meridian} must be a valid Angle input for reference line")

    
