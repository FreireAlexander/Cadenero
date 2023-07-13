import math
from .angles import Angle
from .extras.validation import isAzimuth

class Azimuth(Angle):
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

    def __init__(self, value):
        if isAzimuth(value):
            super().__init__(value, 0)
            self.type = 'Azimuth' 
            self.degree = Azimuth.setAzimuth(self)              
        else:
            raise ValueError(f'Could not convert {value} to Azimuth')
    
    def __add__(self, otherAngle):
        if otherAngle.type in ['Azimuth', 'Angle']:
            return Azimuth(str(setDecimal(self.decimal+otherAngle.decimal)))
        elif type(otherAngle) in [type(1), type(3.14)]:
            return Azimuth(str(setDecimal(self.decimal+otherAngle)))
    
    def __radd__(self, other):
        if type(other) in [type(1), type(3.14)]:
            return Azimuth(str(setDecimal(self.decimal+other)))
        elif other.type in ['Azimuth', 'Angle']:
            return Azimuth(str(setDecimal(self.decimal+other.decimal)))

    def setAzimuth(self):
        if self.degree > 360 :
            return self.degree_standard
        else:
            return self.degree

def setDecimal(decimal):
    if decimal < 0 :
        return 360*(abs(decimal)//360+1) + decimal
    else:
        return decimal
    
    