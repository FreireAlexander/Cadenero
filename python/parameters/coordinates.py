"""
Coordinates

    x: float
    y: float
    z: float

"""

class Coordinate():

    __slot__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __str__(self) -> str:
        return f"({self.x},{self.y},{self.z})"
    

    def translateX(self, x: float):
        self.x = x
        return self


    def translateY(self, y: float):
        self.y = y
        return self


    def translateZ(self, z: float):
        self.z = z
        return self
    

    def translate(self, x: float = None, y: float = None, z: float = None):
        
        def isNotNone(newValue, oldValue):
            if newValue:
                return newValue
            else: 
                return oldValue

        self.x = isNotNone(x, self.x)
        self.y = isNotNone(y, self.y)
        self.z = isNotNone(z, self.z)


        return self


           

    
    


