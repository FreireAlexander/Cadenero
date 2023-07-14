from model import *

def test_1():
    Sum = 0
    print(float('-0'))
    print(float(-12.34))
    
    for i in range(5):
        angle = input(f"Ingrese el ángulo {i}: ")
        try:
            angulo = Angle(angle)
            print(f"El angulo ingresado es {angulo} y es del tipo {angulo.type}")
            print(f"El norte esta rotado {angulo.rotation}")
        except:
            print(f'No se pudo convertir a angulo')
        if isBearing(angle):
            print("Ingresaste un Rumbo")
            angle = Bearing(angle)
            print(angle)
            print(f"El angulo es {angle}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El numero de vuelta en decimales es {angle.spin_number_decimal}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            
        elif isAzimuth(angle):
            print("Es un Azimuth")
            angle = Azimuth(angle)
            print(angle)
            print(f"El angulo es {angle}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El numero de vuelta en decimales es {angle.spin_number_decimal}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            Sum += angle
            print(f"Tipo de la suma {Sum.type}")
            print(f"Total de Azimuths acumulados es igual {Sum}")
        elif isAngle(angle):
            print("Es un Angle a toda regla")
            angle = Angle(angle)
            print(angle)
            print(f"El angulo es {angle}")
            print(f"El numero de vuelta es {angle.spin_number}")
            print(f"El numero de vuelta en decimales es {angle.spin_number_decimal}")
            print(f"El angulo en decimales es {angle.decimal}")
            print(f"Los grados estandar es igual a {angle.degree_standard}")
            print(f"El angulo en formato estandar es {angle.standard}")
            print(f"el tipo del angulo es {angle.type}")
            Sum += angle
            print(f"Tipo de la suma {Sum.type}")
            print(f"Total de Azimuths acumulados es igual {Sum}")


def test_2():
    print(float(-12.34))
    print(toSexagesimal(-200.2342))
    try:
        print(toSexagesimal('holisisisis'))
    except:
        print('lo anterior no se pudo')
    for i in range(6):
        angle = input(f"Ingresa el angulo {i+1}: ")
        if isAzimuth(angle): 
            print("Es Azimuth")
        angulo = None
        try:
            angulo = Meridian(angle)
        except:
            print(f"El valor {angle} no es valido...")
        if angulo != None:
            print(f"El angulo es {angulo} y es de tipo {angulo.type}")
            print(f"EL numero de vueltas es {angulo.spin_number}")
            print(f"El numero de vueltas decimales es {angulo.spin_number_decimal}")
            print(f"El angulo en decimales es {angulo.decimal}")
            print(f"El angulo standard es {angulo.standard}")
            print(f"Imprimiento angulo estandard {toSexagesimal(angulo.standard)}")


def test_3():
    for i in range(6):
        angle = input(f"Ingresa el angulo {i+1}: ")
        try:
            value, horizontal, vertical = getQuadrant(angle)
            print(f"el valor es {value}, la hor: {horizontal} y la vert {vertical}")
        except:
            print("Te equivocaste")

def main():
    test_3()

if __name__ == "__main__":
    main()