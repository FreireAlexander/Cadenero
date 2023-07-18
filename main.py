from model import *
import math

def test_1():
    for i in range(6):
        print(setAngle(math.pi)['Raw'])
        angle = input(f"Ingresa el angulo {i+1}: ")
        
        try:
            ans = getValues(angle)
            res = setAngle(angle)
            print(f"El valor del angulo es {ans}")
            print(f"El numero de rotaciones {res['rotations']}")
            print(f"El angulo en crudo es igual {res['Raw']}")
            print(f"El angulo crudo en decimales es {res['decimal']}")
            print(f"El angulo en sentido de las manecillas del reloj es  {res['Standard']}")
            print(f"El angulo en contra de las manecillas del reloj es  {res['Counter']}")
            print(f"El azimuth es {res['Azimuth']}")
            print(f"El Rumbo es {res['Bearing']}")
            print(f"El angulo es igual a {res['Angle']}")
        except:
            print("Te equivocaste")

def main():
    test_1()

if __name__ == "__main__":
    main()