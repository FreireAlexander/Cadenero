import validation as val
import calculus as calc
import menus

def distance():

    distance = input("\tInput distance [meters]: ")
    while not val.positive_number_validation(distance):
        print("\tDsitances must be a number")
        distance = input("\tInput distance [meters]: ")
        
    distance = val.ToNumber(distance)

    return distance


def angle():

    wcb = input("\tInput angle: ")
    while not val.positive_number_validation(wcb):
        print("\tAngles must be a number")
        print("!!! Remenber angles must be introduces as positive !!!")
        wcb = input("\tInput angle: ")
        
    wcb = val.ToNumber(calc.is_wcb_360(float(wcb)))

    return wcb


def angledms():
    print("\tInput angle as DD°MM°SS° or N DD°MM°SS° E")
    print("\tif minutes or seconds are 0's introduce them as well")
    angle = input("\tInput angle: ")
    flag1 = 0
    flag2 = 0
    if val.isbearing(angle):
        flag1 = 1
    if val.isdms(angle):
        flag2 = 1

    while (flag1 + flag2) == 0:
        flag1 = 0
        flag2 = 0
        print("\tInput angle as DD°MM°SS° or N DD°MM°SS° E")
        print("\tif minutes or seconds are 0's introduce them as well")
        print("\tplease follow the format")
        angle = input("\tInput angle: ")
        if val.isbearing(angle):
            flag1 = 1
        if val.isdms(angle):
            flag2 = 1

    return angle

def dms():
    print("\tInput angle as DD°MM°SS°")
    print("\tif minutes or seconds are 0's introduce them as well")
    angle = input("\tInput angle: ")
    flag2 = 0
    if val.isdms(angle):
        flag2 = 1

    while flag2 == 0:
        flag2 = 0
        print("\tInput angle as DD°MM'SS'' ")
        print("\tif minutes or seconds are 0's introduce them as well")
        print("\tplease follow the format")
        angle = input("\tInput angle: ")
        if val.isdms(angle):
            flag2 = 1

    return angle


def reducedbearing():
    print("\tInput angle as  N DD°MM'SS'' E ")
    print("\tif minutes or seconds are 0's introduce them as well")
    angle = input("\tInput angle: ")
    flag1 = 0
    if val.isbearing(angle):
        flag1 = 1
    flag2 = 0
    if val.isbearing2(angle):
        flag2 = 1
    while (flag1 + flag2) == 0:
        flag1 = 0
        flag2 = 0
        print("\tInput angle as N DD°MM'SS'' E")
        print("\tif minutes or seconds are 0's introduce them as well")
        print("\tplease follow the format ")
        angle = input("\tInput angle: ")
        if val.isbearing(angle):
            flag1 = 1
        
        if val.isbearing2(angle):
            flag2 = 1

    return angle


def rbdecimal():
    print("\tInput angle as  N decimals°[is optional] E ")
    angle = input("\tInput angle: ")
    flag1 = 0
    if val.isbearingdecimal(angle):
        flag1 = 1

    while flag1 == 0:
        flag1 = 0
        print("\tInput angle as N decimals°[is optional] E")
        print("\tplease follow the format ")
        angle = input("\tInput angle: ")
        if val.isbearingdecimal(angle):
            flag1 = 1

    return angle

def Coordinates():

    coordinates = [0,0]   
    coordinates[0] = input("\tInput horizontal coordinates: ")
    while not val.number_validation(coordinates[0]):
        print("\tRemenber coordinates must be a number")
        coordinates[0] = input("\tInput horizontal coordinates: ")
           
    coordinates[0] = val.ToNumber(coordinates[0])

    coordinates[1] = input("\tInput vertical coordinates: ")
    while not val.number_validation(coordinates[1]):
        print("\tRemenber coordinates must be a number")
        coordinates[1] = input("\tInput vertical coordinates: ")
           
    coordinates[1] = val.ToNumber(coordinates[1])
    
    return coordinates

def twoCoordinates():
    print("\t Input initial point Coordinates")
    initialcoordinates = []
    initialcoordinates = Coordinates()
    menus.clear()
    print("\t Input final point Coordinates")
    finalcoordinates = []
    finalcoordinates = Coordinates()

    return initialcoordinates, finalcoordinates
