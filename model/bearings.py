import math
from .declinations import Declination
from .azimuths import Azimuth
from .angles import Angle
from .tools import isBearing

class Bearing(Declination):
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
            super().__init__(value)
            self.type = 'Bearing'
        else:
            raise ValueError(f"{value} must be an Bearing valid input")

    def __str__(self):
        return self.Bearing 

    def __repr__(self):
        return f"Bearing({self.Bearing})"
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            resta = self.Azimuth_value - other
            return Angle(resta)
        elif isinstance(other, (self.__class__, Azimuth(0).__class__)):
            value = self.Azimuth_value - other.Azimuth_value
            meridian = other.Azimuth_value
            return Angle(value, meridian)
        
    