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
#        dato3 = input(f"Ingrese Angulo : ")
        numero = float(input(f"Ingrese un numero "))
        try:
            angulo1 = Angle(dato1)
            angulo2 = Bearing(dato2)
#            angulo3 = Angle(dato3)
        except:
            print("Alguno de los datos no esta bien")
        
        try:
            print(f"angulo 1 {repr(angulo1)}\n", f"angulo 2 {repr(angulo2)}\n")
#                ,f"angulo 3 {repr(angulo3)}\n")
            print(angulo1, angulo2)
        except:
            print("Alguno de los datos no esta bien")
        
        try:
            print("Angulo mas rumbo")
            res = angulo1 + angulo2
            print(f"{angulo1} + {angulo2} = {res}")
        except:
            print("Suma de Angle y Azimuth no dio...")

        try:
            res = angulo2 + angulo1
            print(f"{angulo2} + {angulo1} = {res}")
        except:
            print("Suma de Azimuth y Angle no dio...")

        try:
            resta = angulo1 + numero
            print(f"Sumas con el numero {numero} despues")
            print(f"{angulo1} + {numero} = {resta}")
        except:
            print("Suma de Angle + numero no dio...")
        
        try:
            resta = numero + angulo2
            print(f"Sumas con el numero {numero} por delante")
            print(f"{numero} + {angulo2} = {resta}")
        except:
            print("Suma de Angle + Numero no dio...")

        try:
            resta = angulo2 - angulo1
            print(f"{angulo2} - {angulo1} = {resta}")
        except:
            print("Resta de Angle y Angle no dio...")
        
        try:
            resta = angulo1 - angulo2
            print(f"{angulo1} - {angulo2} = {resta}")
        except:
            print("Resta de Angle y Angulo no dio...")


        input(f"Enter para continuar..")

def main():
    test_1()

if __name__ == "__main__":
    main()