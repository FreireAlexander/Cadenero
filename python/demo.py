"""
Cadenero
version: 0.0.0-dev


author: Freire Alexander Palomino Palma
email: freirealexander0214@gmail.com
"""
from parameters import Coordinate
from parameters import Line

def main():
    startPoint = Coordinate(0,0)
    print(f"Start point: {startPoint}")
    endPoint = Coordinate(5,5)
    print(f"End Point: {endPoint}")
    line = Line((1,3.45), (2.34, -100))
    print(f"Line: {line}")
    line = Line(startPoint.translate(x=24, z=100), endPoint)
    print(f"Line: {line}")


if __name__ == "__main__":
    main()