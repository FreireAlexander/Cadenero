from model import Angle, Azimuth, Bearing, Declination
import math

def test_1():
    for i in range(6):
        dato1 = input(f"Ingresa el Azimuth 1 intento {i+1}: ")
        dato2 = input(f"Ingresa el Azimuth 2 intento {i+1}: ")

        try:
            azimuth1 = Azimuth(dato1)
            azimuth2 = Azimuth(dato2)
            angulo1 = Angle(dato1, dato2)
            print(f"El angulo1 tiene una magnitud de {angulo1.value}")
            print(f"El angulo1 tiene un azimuth de {angulo1.Azimuth_value}")
            print(f"el azimuth es {angulo1.Azimuth}")
            resta = azimuth1 - azimuth2
            resta1 = azimuth1-100
            resta2 = azimuth2-1000
            print(f"Resta entre declinations")
            print(f"{azimuth1} + {azimuth2} = {resta}")
            print(f"Resta expresada en Values")
            print(f"{resta.value}")
            print(f"value: {resta.value} Azimuth: {resta.Azimuth} Bearing: {resta.Bearing}")
            print(f"con orientacion desde {resta.orientation}")
            print(f"Restarle 100")
            print(f"{azimuth1} - 100 = {resta1}")
            print(f"Resta expresada en Values")
            print(f"{resta1.value}")
            print(f"value: {resta1.value} Azimuth: {resta1.Azimuth} Bearing: {resta1.Bearing}")
            print(f"con orientacion desde {resta1.orientation}")
            print(f"Restarle 1000")
            print(f"{azimuth2} - 1000 = {resta2}")
            print(f"Resta expresada en Values")
            print(f"{resta2.value}")
            print(f"value: {resta2.value} Azimuth: {resta2.Azimuth} Bearing: {resta2.Bearing}")
            print(f"con orientacion desde {resta2.orientation}")
        except ValueError:
            print(f"No pudo convertirse en un Azimuth porque el valor está equivocado")
        """
        try:
            azimuth1 = Declination(dato1)
            azimuth2 = Declination(dato2)
            resta = azimuth1 - azimuth2
            resta1 = azimuth1-100
            resta2 = azimuth2-1000.25
            print(f"{azimuth1} - {azimuth2} = {resta} con refencia en {resta.orientation} y valor absoluto de {resta.Standard} y azimuth de {resta.Azimuth}")
            print(f"el azimuth es {resta.Azimuth_value}")
            print(f"{azimuth1} - 100 = {resta1} con refencia en {resta1.orientation} y valor absoluto de {resta1.Standard} y azimuth de {resta1.Azimuth}")
            print(f"el azimuth es {resta1.Azimuth_value}")
            print(f"{azimuth2} - 1000.25 = {resta2} con refencia en {resta2.orientation} y valor absoluto de {resta2.Standard} y azimuth de {resta2.Azimuth}")
            print(f"el azimuth es {resta2.Azimuth_value}")
            print(f"o un Contra reloj de {resta2.Counter}")

        except ValueError:
            azimuth = 0
            print(f"No pudo convertirse en un Azimuth porque el valor está equivocado")
        try:
            angulo = Angle(angle)
            print(angulo)
        except ValueError:
            angulo = 0
            print(f"No pudo convertirse en un angulo porque el valor está equivocado")
        
        try:
            azimuth = Azimuth(angle)
            print(azimuth)
            print(azimuth.Azimuth)
            print(f"el standard value es {azimuth.Azimuth_value}")
        except ValueError:
            azimuth = 0
            print(f"No pudo convertirse en un Azimuth porque el valor está equivocado")
        
        try:
            bearing = Bearing(rumbo)
            print(bearing)
            print(bearing.Azimuth)
            print(f"el standard value es {bearing.Azimuth_value}")
        except ValueError:
            bearing = Bearing('N0')
            print(f"No pudo convertirse en un Rumbo porque el valor está equivocado")

        print(f"Congruentes {bearing == 0 & bearing > -1}")
        print(f"Mayor igual que {bearing >= 225}")
        print(f"Mayor que {bearing > azimuth}")
        print(f"Distintos {bearing != 225}")
        print(f"Menor igual que {bearing <= 225}")
        print(f"Menor que {bearing < azimuth}")
        print(dir(angulo))
        """


def main():
    test_1()

if __name__ == "__main__":
    main()