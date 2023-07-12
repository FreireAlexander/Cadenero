from model import *

def main():
    Sum = 0
    print(float('-0'))
    for i in range(5):
        angle = input(f"Ingrese el ángulo {i}: ")
        
        if isBearing(angle):
            print("Ingresaste un Rumbo")
            angle = Bearing(angle)
            print(angle)
            print(f"El angulo es {angle.print}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            
        elif isAzimuth(angle):
            print("Es un Azimuth")
            angle = Angle(angle)
            print(angle)
            print(f"El angulo es {angle.print}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            Sum += angle
            print(f"Tipo de la suma {Sum.type}")
            print(f"Total de Azimuths acumulados es igual {Sum.print}")
        elif isAngle(angle):
            print("Es un Angle a toda regla")
            angle = Angle(angle)
            print(angle)
            print(f"El angulo es {angle.print}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            Sum += angle
            print(f"Tipo de la suma {Sum.type}")
            print(f"Total de Azimuths acumulados es igual {Sum.print}")

if __name__ == "__main__":
    main()