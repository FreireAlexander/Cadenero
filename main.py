from model import Angle, Azimuth, Bearing
from pyemenu import clear_screen
import math

def test_1():
    """
    Dunder Methods para el Angle
    """
    for i in range(6):
        clear_screen()
        print(f"Intento {i+1}")
        dato1 = input(f"Ingrese Angle 1: ")
        dato2 = input(f"Ingrese Angle 2: ")
        dato3 = input(f"Ingrese Angulo : ")
        numero = float(input(f"Ingrese un numero "))
        try:
            angulo1 = Angle(dato1)
            angulo2 = Bearing(dato2)
            angulo3 = Azimuth(dato3)
        except:
            print("Alguno de los datos no esta bien")
        
        try:
            print(f"angulo 1 {repr(angulo1)}\n", f"angulo 2 {repr(angulo2)}\n"
                    ,f"angulo 3 {repr(angulo3)}\n")
            print(angulo1, angulo2)
        except:
            print("Alguno de los datos no esta bien")
        
        try:
            print("Angulo menos rumbo")
            res = angulo2 - angulo1
            print(f"{angulo1} - {angulo2} = {res}")
        except:
            print(f"La resta de {angulo2}  - {angulo1}  .... Error Rumbo")

        try:
            print("Angulo menos Azimuth")
            res = angulo3 - angulo1
            print(f"{angulo1} - {angulo3} = {res}")
        except:
            print(f"La resta de {angulo3}  - {angulo1}  .... Error Azimuth")

        try:
            print("Angulo menos numero")
            res = numero - angulo1
            print(f"{angulo1} - {numero} = {res}")
        except:
            print(f"La resta de {numero}  - {angulo1}  ... Error  Numero ")

        input(f"Enter para continuar..")

def main():
    test_1()

if __name__ == "__main__":
    main()