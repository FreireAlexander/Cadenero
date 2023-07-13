import math
from .angles import Angle
from .extras.validation import isBearing

class Bearing(Angle):
    """
    Estos objetos son Rumbos en toda su definición, 
    Es decir, que es necesario escribir su cuadrante en la notación.
    Norte o Sur + ángulo en grados, minutos y segundos + Este u Oeste.
    De manera similar a los acimutes se tendrían las siguientes maneras de escribirlos, 
    recordando claro que al inicio y al final se debe especificar el cuadrante vertical al inicio y 
    el cuadrante horizontal al final:
    1. [Norte o Sur]numero entero  [Este u Oeste]
    2. [Norte o Sur]numero decimal [Este u Oeste]
    3. [Norte o Sur]numero decimal + ' o ° cualquiera de los dos [Este u Oeste]
    4. [Norte o Sur]numero entero + ' o ° + numero decimal o entero + ° o '  [Este u Oeste]
    5. [Norte o Sur]numero entero + ' o ° + numero entero [entre 0 a 59] + ° o ' + numero decimal o entero entre 0 y 59 + ' o ° o " [Este u Oeste]
    """
    def __init__(self, value):
        if isBearing(value):
            super().__init__(value)
            self.type = 'Bearing'               
        else: 
            raise ValueError(f'Could not convert {value} to Bearing')
    
