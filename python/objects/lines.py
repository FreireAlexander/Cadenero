'''

    A Line is define by two coordinates.
        * Coordinates are the same as points in its core

    author: Freire Alexander Palomino Palma
    email: freirealexander0214@gmail.com
    website: freirealexander.top
'''
from math import sqrt
from .coords import Coord

PRECISION = 6

class Line():
    '''
        A coordinate in the cartesian plane
        it must an x coordinate, y coordinate and z coordinate.
    '''
    def __init__(self, start: Coord, end: Coord):
        
        self.start = start
        self.end = end
        self._deltaX = end.x - start.x
        self._deltaY = end.y - start.y
        self._deltaZ = end.z - start.z
        self._precision = PRECISION
        self._len = Line.lenght(self, self._precision)
        self._lenAuxiliar = Line.lenght(self, PRECISION)
        self._vector = Line.getVector(self)
    
    
    def __str__(self):
        return f"{self.start} -> {self.end}"
    

    def lenght(self, precision: int = 6) -> float:
        return round(sqrt(self._deltaX**2 + self._deltaY**2 + self._deltaZ**2), precision)


    def getVector(self) -> list:
        return [self.deltaX/self._lenAuxiliar, self.deltaY/self._lenAuxiliar, self.deltaZ/self._lenAuxiliar]
    

    @property
    def deltaX(self):
        return self._deltaX


    @property
    def deltaY(self):
        return self._deltaY
    
    @property
    def deltaZ(self):
        return self._deltaZ
    

    @property
    def precision(self):
        return self._precision
    

    @property
    def len(self):
        self._len = Line.lenght(self, self._precision)
        return self._len
    

    @property
    def vector(self):
        self._vector = Line.getVector(self)
        return self._vector
    

    @precision.setter
    def precision(self, precision: int):
        self._precision = precision


