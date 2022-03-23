import menus
import calculus as calc
import validation as val
import typeindata as load

## CONSTANTS FOR MENUS
SUBTITLE1 = "What information do you have?"

## SUB app used in principal apps of Land Survey Calculator

## Menus

### Input Angle format menu
def inputangleformatmenu():
    subtitle = "How do you prefer to insert angles?"
    suboptions = ["1. Decimal angle ", "2. in DD°MM'SS'' "]
    angle_format = menus.list_menu(subtitle, suboptions)
    return angle_format

### Input Type of Angle menu
def inputtypeofanglemenu():
    subtitle = "Which angle do you know?"
    suboptions = [
            "1. Whole Circle Bearing",
            "2. Reduced Bearing",
            "3. Back Bearing"
            ]
    angle_choice = menus.list_menu(subtitle, suboptions)
    return angle_choice
## Principal Apps and Functions for Main App

def simplecalculatecoordinates():
    
    subtitle = "Which coordinates do you know?"
    suboptions = [
        "1. Initial Point coordinates",
        "2. Final Point coordinates"
    ]
    coordinate_choice = menus.list_menu(subtitle, suboptions)
    coordinates = []
    coordinates = load.Coordinates()

    # Asking about What type angle is known
    angle_choice = inputtypeofanglemenu()
    # Asking about the format of that angle
    angle_format = inputangleformatmenu()
    
    if angle_format != 1:
        
        if angle_choice == 0 or angle_choice == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.angle()
            wcb = angle

        elif angle_choice == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.rbdecimal()
            rb = angle
            rb = val.bearingdata_decimal(rb)
            rb = calc.rbdecimaltowcb(rb)
            wcb = rb

        elif angle_choice == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.angle()
            backbearing = calc.backbearing(angle)
            wcb = backbearing

    elif angle_format == 1:
        
        if angle_choice == 0 or angle_choice == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.dms()
            wcb = angle
            wcb = val.bearingdata(wcb)
            wcb = calc.dmstodecimals(wcb)

        elif angle_choice == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.reducedbearing()
            rb = angle
            rb = val.bearingdata(rb)
            rb = calc.rbdmstowcb(rb)
            wcb = rb

        elif angle_choice == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            backbearing = calc.backbearing(backbearing)
            wcb = backbearing

        
    print("------Input distance-----------------")
    distance = 0
    distance = load.distance()

    point_order = "initial point to final point"
    if coordinate_choice == 1:
        point_order = "final point to initial point"

    # Type of angle used
    anglestr = ""
    if angle_choice == 0:
        anglestr = "Whole Circle Bearing"
    elif angle_choice == 1:
        anglestr = "Reduced Bearing"
    elif angle_choice == 2:
        anglestr = "Back Bearing"
    
    coord_result = calc.coordinatesfrompoint(coordinates, distance, wcb)
    menus.clear()
    print("\t the coordinates are {} ".format(coord_result))
    print("\t from {} with a distance of {} m".format(point_order,distance))
    print("\t using {} an angle of {}".format(anglestr,angle))
    print("\t this mean an WCB of {}°\n".format(round(wcb,3)))

    print("\t CoordX = {} + {}*SIN({}°) = {}".format(coordinates[0],distance,round(wcb,3),coord_result[0]))
    print("\t CoordY = {} + {}*COS({}°) = {}".format(coordinates[0],distance,round(wcb,3),coord_result[1]))
    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return

def simplecalculatewcb():

    suboptions = [
        "1. WCB between two coordinates",
        "2. A Reduced Bearing",
        "3. A Back Whole circle Bearing"
    ]

    info_choice = menus.list_menu(SUBTITLE1, suboptions)

    if info_choice == 0:
        initialcoordinates, finalcoordinates = load.twoCoordinates()
        wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
        menus.clear()
        print("\n\tWCB from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,calc.decimaltodms(wcb)))
    
    elif info_choice == 1:
        angle_format = inputangleformatmenu()
        if angle_format != 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.rbdecimal()
            rb = angle
            rb = val.bearingdata_decimal(rb)
            rb = calc.rbdecimaltowcb(rb)
            wcb = rb
            menus.clear()
            print("\t The WCB is equal to {} from Reduced Bearing {}".format(wcb,angle))
        elif angle_format == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.reducedbearing()
            rb = angle
            rb = val.bearingdata(rb)
            rb = calc.rbdmstowcb(rb)
            wcb = rb
            wcb = calc.decimaltodms(wcb)
            menus.clear()
            print("\t The WCB is equal to {} from Reduced Bearing {}".format(wcb,angle))
        
        
    elif info_choice == 2:
        
        angle_format = inputangleformatmenu()
        if angle_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.angle()
            backbearing = angle
            backbearing = calc.backbearing(backbearing)
            wcb = backbearing
            menus.clear()
            print("\t The WCB is equal to {} from Back Bearing {}".format(wcb,angle))
        elif angle_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            backbearing = calc.backbearing(backbearing)
            wcb = calc.decimaltodms(backbearing)
            menus.clear()
            print("\t The WCB is equal to {} from Back Bearing {}".format(wcb,angle))

    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return


def simplecalculaterb():
    
    suboptions = [
        "1. Reduced Bearing between two coordinates",
        "2. A Whole Circle Bearing",
        "3. A Back Whole circle Bearing"
    ]

    info_choice = menus.list_menu(SUBTITLE1, suboptions)

    if info_choice == 0:
        initialcoordinates, finalcoordinates = load.twoCoordinates()
        wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
        rb = calc.wcbdecimaltorbdms(wcb)
        menus.clear()
        print("\n\t Reduced Bearing from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,rb))
    elif info_choice == 1:
        angle_format = inputangleformatmenu()
        if angle_format != 1:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.angle()
            wcb = angle
            rb = calc.wcbdecimaltorbdecimal(wcb)
            print("\t The Reduced Bearing is equal to {} from WCB {}° ".format(rb,angle))
        elif angle_format == 1:
            print("------Input Wcb------")
            print("** Angles must be introduces as positive")
            angle = load.dms()
            wcb = angle
            wcb = val.bearingdata(wcb)
            wcb = calc.dmstodecimals(wcb)
            rb = calc.wcbdecimaltorbdms(wcb)
            print("\t The Reduced Bearing is equal to {} from WCB {} ".format(rb,angle))
    
    elif info_choice == 2:
        angle_format = inputangleformatmenu()
        if angle_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.angle()
            backbearing = angle
            backbearing = calc.backbearing(backbearing)
            rb = calc.wcbdecimaltorbdecimal(backbearing)
            menus.clear()
            print("\t The Reduced Bearing is equal to {} from Back Bearing {} ".format(rb,angle))
        elif angle_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = load.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            wcb = calc.backbearing(backbearing)
            rb = calc.wcbdecimaltorbdms(wcb)
            menus.clear()
            print("\t The Reduced Bearing is equal to {} from Back Bearing {} ".format(rb,angle))
    
    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return

def simpleangleconvertion():
    subtitle = "What do you want to do?"
    suboptions = [
        "1. Convert Degree Minutes Seconds to Decimals",
        "2. Convert Decimals to Degree Minutes Seconds"
    ]
    choice = menus.list_menu(subtitle, suboptions)
    if choice == 0:
        print("------Input Angle------")
        angle = load.angledms()
        angle_input = angle
        angle = val.bearingdata(angle)
        degree = 0
        if angle[3] == '':
            degree = round(calc.dmstodecimals(angle),3)
            degree = str(degree) +"°"
        else:
            degree = round(calc.dmstodecimals(angle),3)
            degree = str(degree) +"° in quadrant "+ angle[3]
        print("The angle {} is equal to {}".format(angle_input,degree))
    elif choice == 1:
        print("------Input Angle------")
        print("** Angles must be introduces as positive")
        angle = load.angle()
        angle = round(angle, 3)
        angledms = calc.decimaltodms(angle)
        print("the angle {}° in range [0 to 360°] is equal to {}".format(angle,angledms))

    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return