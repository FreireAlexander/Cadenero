import os
from person import Person
from car import Car
from account import Account
from uberx import UberX
from model import *

def main():
    print("Creando nueva cuenta")
    cuenta = Account("Freire", "1140858993")
    print(f"Vars Cuenta 1 {vars(cuenta)}")
    print(f"Cuenta creada con éxito de {cuenta.name} con cedula {cuenta.document}")
    carro = Car(cuenta, "ENK489")
    print(f"Vars Carro de la cuenta 1 {vars(carro)}")
    print(f"El carro con placas {carro.license} con conductor {carro.name} y documento de identidad {carro.document}")
    uberx = UberX(carro, "Onix", "2018")
    print(f"Vars UberX {vars(uberx)}")
    print(f"El UberX con conductor {uberx.name} con documento de identidad {uberx.document}\n")

    print("Objetos de cadenero \n")

    punto = point.Point(23.45677, 100.90023223)
    print(f"Coordenada 1 {punto.x} E y {punto.y} N")

if __name__ == "__main__":
    main()