from model import Angle, Azimuth, Bearing, Declination
from pyemenu import clear_screen
import math

def test_1():
    """
    Dunder Methods para el Azimuth
    """
    for i in range(6):
        clear_screen()
        print(f"Intento {i+1}")
        dato1 = input(f"Ingrese Azimuth 1: ")
        dato2 = input(f"Ingrese Bearing 2: ")
        dato3 = input(f"Ingrese ANgulo : ")
        numero = float(input(f"Ingrese un numero "))
        try:
            angulo1 = Azimuth(dato1)
            angulo2 = Bearing(dato2)
            angulo3 = Angle(dato3)
        except:
            print("Alguno de los datos no esta bien")
        
        try:
            resta = angulo1 - angulo2
            print(f"{angulo1} - {angulo2} = {resta}")
            print(f"Desde el polo en {resta.orientation}")
        except:
            print("Resta de Azimuth y Azimuth no dio...")
        
        try:
            resta = angulo1 - angulo3
            print(f"{angulo1} - {angulo3} = {resta}")
            print(f"Desde el polo en {resta.orientation}")
            print(f"El value de {angulo3} es {angulo3.value}\n")
        except:
            print("Resta de Azimuth y Angulo no dio...")

        try:
            angulo3 = Angle(dato3, numero)
            resta = angulo1 - angulo3
            print(f"{angulo1} - {angulo3} = {resta}")
            print(f"Resta es igual a desde el polo en {resta.orientation} azimuth {resta.Azimuth}")
            print(f"El angulo 3 es {angulo3} con Value {angulo3.value}\n")
            print(f"El angulo 3 es {angulo3} con azimuth {angulo3.Azimuth}\n")
        except:
            print("Resta de Azimuth y Angulo con Orientacion no dio...")

        try:
            resta = angulo2 - angulo1
            print(f"{angulo2} - {angulo1} = {resta}")
            print(f"Desde el polo en {resta.orientation}")
        except:
            print("Resta de Rumbo y Azimuth no dio...")

        try:
            resta = angulo1 - numero
            print(f"{angulo1} - {numero} = {resta}")
            print(f"Desde el polo en {resta.orientation}")
        except:
            print("Resta de Azimuth y numero no dio...")
        
        try:
            resta = numero - angulo2
            print(f"{numero} - {angulo2} = {resta}")
            print(f"Desde el polo en {resta.orientation}")
        except:
            print("Resta de numero - azimuth no dio...")

        input(f"Enter para continuar..")

def main():
    test_1()

if __name__ == "__main__":
    main()