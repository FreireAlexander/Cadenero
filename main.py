from extras import *
from model import *
import pyemenu

def main():

    for i in range(2):
        text = input("Ingrese el ángulo: ")
        angulo = setangle(text)
        if angulo != None:
            angulo.print_angle()
            print(f"Numero de vueltas {angulo.spin_number}")
            print(f"Numero de vueltas aproximadas {angulo.spin_number_decimal}")
        else:
            print("Entrada incorrecta")

if __name__ == "__main__":
    main()