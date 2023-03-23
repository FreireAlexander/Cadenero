import menu
import calculus as calc
import validation as val
import input

## CONSTANTS FOR MENUS
SUBTITLE1 = "What information do you have?"

## SUB app used in principal apps of Land Survey Calculator

## Menus

### Input Angle format menu
def angle_format_menu():
    subtitle = "How do you prefer to insert angles?"
    suboptions = ["1. Decimal angle ", "2. in DD°MM'SS'' "]
    choice = menu.print_menu(subtitle, suboptions)
    return suboptions.index(choice)

### Input Type of Angle menu
def angle_type_menu():
    subtitle = "Which type of angle do you know?"
    suboptions = [
            "1. Whole Circle Bearing",
            "2. Reduced Bearing",
            "3. Back Bearing"
            ]
    choice = menu.print_menu(subtitle, suboptions)
    return suboptions.index(choice)
## Principal Apps and Functions for Main App

def coordinates():
    # Asking about What type angle is known
    choice_angle = angle_type_menu()
    # Asking about the format of that angle
    choice_format = angle_format_menu()

    subtitle = "Which coordinates do you know?"
    suboptions = [
        "1. Initial Point coordinates",
        "2. Final Point coordinates"
    ]
    coordinate_choice = menu.print_menu(subtitle, suboptions)
    coordinates = []
    coordinates = input.Coordinates()


    
    if choice_format != 1:
        
        if choice_angle == 0 or choice_angle == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.input_angle()
            wcb = angle

        if choice_angle == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.rbdecimal()
            rb = angle
            rb = val.bearingdata_decimal(rb)
            rb = calc.rbdecimaltowcb(rb)
            wcb = rb

        if choice_angle == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.input_angle()
            backbearing = calc.backbearing(angle)
            wcb = backbearing

    elif choice_format == 1:
        
        if choice_angle == 0 or choice_angle == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.dms()
            wcb = angle
            wcb = val.bearingdata(wcb)
            wcb = calc.dmstodecimals(wcb)

        elif choice_angle == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.reducedbearing()
            rb = angle
            rb = val.bearingdata(rb)
            rb = calc.rbdmstowcb(rb)
            wcb = rb

        elif choice_angle == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            backbearing = calc.backbearing(backbearing)
            wcb = backbearing

        
    print("------Input distance-----------------")
    distance = 0
    distance = input.input_distance()

    point_order = "initial point to final point"
    if coordinate_choice == suboptions[0]:
        point_order = "final point to initial point"

    # Type of angle used
    anglestr = ""
    if choice_angle == 0:
        anglestr = "Whole Circle Bearing"
    elif choice_angle == 1:
        anglestr = "Reduced Bearing"
    elif choice_angle == 2:
        anglestr = "Back Bearing"
    
    coord_result = calc.coordinatesfrompoint(coordinates, distance, wcb)
    menu.clear()
    print("\t the coordinates are {} ".format(coord_result))
    print("\t from {} with a distance of {} m".format(point_order,distance))
    print("\t using {} an angle of {}".format(anglestr,angle))
    print("\t this mean an WCB of {}°\n".format(round(wcb,3)))

    print("\t CoordX = {} + {}*SIN({}°) = {}".format(coordinates[0],distance,round(wcb,3),coord_result[0]))
    print("\t CoordY = {} + {}*COS({}°) = {}".format(coordinates[0],distance,round(wcb,3),coord_result[1]))
    print("\nPress Enter to continue...")
    input()
    menu.clear()

    return

def simplecalculatewcb():

    suboptions = [
        "1. WCB between two coordinates",
        "2. A Reduced Bearing",
        "3. A Back Whole circle Bearing"
    ]

    info_choice = menu.print_menu(SUBTITLE1, suboptions)

    if info_choice == suboptions[0]:
        initialcoordinates, finalcoordinates = input.twoCoordinates()
        wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
        menu.clear()
        print("\n\tWCB from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,calc.decimaltodms(wcb)))
    
    elif info_choice == suboptions[1]:
        choice_format = choice_format()
        if choice_format != 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.rbdecimal()
            rb = angle
            rb = val.bearingdata_decimal(rb)
            rb = calc.rbdecimaltowcb(rb)
            wcb = rb
            menu.clear()
            print("\t The WCB is equal to {} from Reduced Bearing {}".format(wcb,angle))
        elif choice_format == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.reducedbearing()
            rb = angle
            rb = val.bearingdata(rb)
            rb = calc.rbdmstowcb(rb)
            wcb = rb
            wcb = calc.decimaltodms(wcb)
            menu.clear()
            print("\t The WCB is equal to {} from Reduced Bearing {}".format(wcb,angle))
        
        
    elif info_choice == suboptions[2]:
        
        choice_format = angle_format_menu()
        if choice_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.input_angle()
            backbearing = angle
            backbearing = calc.backbearing(backbearing)
            wcb = backbearing
            menu.clear()
            print("\t The WCB is equal to {} from Back Bearing {}".format(wcb,angle))
        elif choice_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            backbearing = calc.backbearing(backbearing)
            wcb = calc.decimaltodms(backbearing)
            menu.clear()
            print("\t The WCB is equal to {} from Back Bearing {}".format(wcb,angle))

    print("\nPress Enter to continue...")
    input()
    menu.clear()

    return


def simplecalculaterb():
    
    suboptions = [
        "1. Reduced Bearing between two coordinates",
        "2. A Whole Circle Bearing",
        "3. A Back Whole circle Bearing"
    ]

    info_choice = menu.print_menu(SUBTITLE1, suboptions)

    if info_choice == suboptions[0]:
        initialcoordinates, finalcoordinates = input.twoCoordinates()
        wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
        rb = calc.wcbdecimaltorbdms(wcb)
        menu.clear()
        print("\n\t Reduced Bearing from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,rb))
    elif info_choice == suboptions[1]:
        choice_format = angle_format_menu()
        if choice_format != 1:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.input_angle()
            wcb = angle
            rb = calc.wcb_to_rb_decimal(wcb)
            print("\t The Reduced Bearing is equal to {} from WCB {}° ".format(rb,angle))
        elif choice_format == 1:
            print("------Input Wcb------")
            print("** Angles must be introduces as positive")
            angle = input.dms()
            wcb = angle
            wcb = val.bearingdata(wcb)
            wcb = calc.dmstodecimals(wcb)
            rb = calc.wcbdecimaltorbdms(wcb)
            print("\t The Reduced Bearing is equal to {} from WCB {} ".format(rb,angle))
    
    elif info_choice == suboptions[2]:
        choice_format = angle_format_menu()
        if choice_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.input_angle()
            backbearing = angle
            backbearing = calc.backbearing(backbearing)
            rb = calc.wcb_to_rb_decimal(backbearing)
            menu.clear()
            print("\t The Reduced Bearing is equal to {} from Back Bearing {} ".format(rb,angle))
        elif choice_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            angle = input.dms()
            backbearing = angle 
            backbearing = val.bearingdata(backbearing)
            backbearing = calc.dmstodecimals(backbearing)
            wcb = calc.backbearing(backbearing)
            rb = calc.wcbdecimaltorbdms(wcb)
            menu.clear()
            print("\t The Reduced Bearing is equal to {} from Back Bearing {} ".format(rb,angle))
    
    print("\nPress Enter to continue...")
    input()
    menu.clear()

    return

def simpleangleconvertion():
    subtitle = "What do you want to do?"
    suboptions = [
        "1. Convert Degree Minutes Seconds to Decimals",
        "2. Convert Decimals to Degree Minutes Seconds"
    ]
    choice = menu.print_menu(subtitle, suboptions)
    if choice == suboptions[0]:
        print("------Input Angle------")
        angle = input.input_angledms()
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
    elif choice == suboptions[1]:
        print("------Input Angle------")
        print("** Angles must be introduces as positive")
        angle = input.input_angle()
        angle = round(angle, 3)
        angledms = calc.decimaltodms(angle)
        print("the angle {}° in range [0 to 360°] is equal to {}".format(angle,angledms))

    print("\nPress Enter to continue...")
    input()
    menu.clear()

    return