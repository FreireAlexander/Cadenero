from model import *

def main():
    for i in range(5):
        angle = input(f"Ingrese el ángulo {i}: ")
        if isBearing(angle):
            print("Ingresaste un Rumbo")
            angle = Angle(angle)
            print(f"El angulo es {angle.print_angle()}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El angulo en decimales es {angle.decimal}")
        elif isAzimuth(angle):
            print("Es un Azimuth")
            angle = Angle(angle)
            print(f"El angulo es {angle.print_angle()}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El angulo en decimales es {angle.decimal}")

if __name__ == "__main__":
    main()