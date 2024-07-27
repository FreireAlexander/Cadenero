'''

    This are the basic atom element for geometry.

    author: Freire Alexander Palomino Palma
    email: freirealexander0214@gmail.com
    website: freirealexander.top
'''

class Coord:
    '''
        A coordinate in the cartesian plane
        it must an x coordinate, y coordinate and z coordinate.
    '''
    def __init__(self, x, y, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x} ; {self.y} ; {self.z})"
    
