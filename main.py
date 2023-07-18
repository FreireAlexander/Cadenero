from model import *
import math

def test_1():
    for i in range(6):
        print(setAttributes(-1)['Azimuth'])
        angle = input(f"Ingresa el angulo {i+1}: ")
        
        
        ans = getValues(angle)
        res = setAttributes(angle)
        print(f"El valor del angulo es {ans}")
        print(f"El numero de rotaciones {res['rotations']}")
        print(f"El angulo crudo en decimales es {res['value']}")
        print(f"El angulo en sentido de las manecillas del reloj es  {res['Standard']}")
        print(f"El angulo en contra de las manecillas del reloj es  {res['Counter']}")
        print(f"El azimuth es {res['Azimuth']}")
        print(f"El Valor del Azimuth es {res['Azimuth_value']}")
        print(f"El Azimuth como decimal es {res['Azimuth_decimal']}")
        print(f"El Rumbo es {res['Bearing']}")
        print(f"El valor decimal del rumbo es {res['Bearing_value']}")
        print(f"El Rumbo en formato decimal es {res['Bearing_decimal']}")
        print(f"El angulo es igual a {res['Angle']}")
        print(f"El angulo en formato decimal es {res['Angle_decimal']}")
        print(f"El angulo en radianes es {res['Radians']}")

def main():
    test_1()

if __name__ == "__main__":
    main()