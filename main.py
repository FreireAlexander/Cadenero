from model import Angle, Azimuth, Bearing
import math

def test_1():
    for i in range(6):
        angle = input(f"Ingresa el Azimuth 1 intento {i+1}: ")
        rumbo = input(f"Ingresa el Azimuth 2 intento {i+1}: ")

        try:
            azimuth1 = Azimuth(angle)
            azimuth2 = Azimuth(rumbo)
            resta = azimuth1 - azimuth2
            resta1 = azimuth1-100
            resta2 = azimuth2-1000.25
            print(f"{azimuth1} - {azimuth2} = {resta} con refencia en {resta.meridian} y valor absoluto de {resta.Standard} y azimuth de {resta.Azimuth}")
            print(f"{azimuth1} - 100 = {resta1} con refencia en {resta1.meridian} y valor absoluto de {resta1.Standard} y azimuth de {resta1.Azimuth}")
            print(f"{azimuth2} - 1000.25 = {resta2} con refencia en {resta2.meridian} y valor absoluto de {resta2.Standard} y azimuth de {resta2.Azimuth}")
            print(f"o un Contra reloj de {resta2.Counter}")

        except ValueError:
            azimuth = 0
            print(f"No pudo convertirse en un Azimuth porque el valor está equivocado")
        """
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