from os import system, name
import math
import readchar

'''
UP = "\x1b\x5b\x41"
DOWN = "\x1b\x5b\x42"
LEFT = "\x1b\x5b\x44"
RIGHT = "\x1b\x5b\x43"
'''

COORD_SPACE = 11  # 8 (max number of digits) + 3 (decimals)
NUMBER_SPACE = 5  # 5 (max number of digits) + 3 (arrow)
ID_SPACE = 10 # 7 (station) + 3 (blank spaces)
ARROW_CHAR = "-->"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def cursor_UP_DOWN(option):
    key_arrow = readchar.readkey()
    if key_arrow == "\x1b\x5b\x41":
        option -= 1
    elif key_arrow == "\x1b\x5b\x42":
        option += 1
    return option, key_arrow


def validatingoption(option, dataset):
    if option <= -1:
            option = len(dataset)-1
    elif option > len(dataset)-1:
            option = 0

    return option


def heading_survey(title):
    print("="*(ID_SPACE + COORD_SPACE)*4 + "="*(len(title)))
    print(" "*(ID_SPACE + COORD_SPACE)*2 +
             title + " "*(ID_SPACE + COORD_SPACE)*2)
    print("="*(ID_SPACE + COORD_SPACE)*4 + "="*(len(title)))
    print("\tStation\t" + "\tline\t" + "\tWCB\t" +
             "\tDistance\t" + "Description")
    print("-"*(ID_SPACE + COORD_SPACE)*4 + "-"*(len(title))) 


def justshowdatasurvey(dataset):
    for data in dataset:
            for item in data:
                index = data.index(item)
                if index in [0, 1]:
                    item = str(item)
                    print("\t{}".format(item)+" "*
                    (ID_SPACE-len(item)), end="")
                elif index in [2, 3]:
                    print("\t{}".format(round(item, 3))+" "*
                          (COORD_SPACE-len(str(item))), end="")
                else:
                    print("\t{}".format(item), end="")
            print("\n")


def justshowsurveyinginfo(title, dataset):

    heading_survey(title)
    justshowdatasurvey(dataset)
    print("\nEsc to exit or press Enter to select option\n")
    input()


def heading_point(title):
    print("="*(NUMBER_SPACE + COORD_SPACE)*4 + "="*(len(title)))
    print(" "*(NUMBER_SPACE + COORD_SPACE)*2 +
             title + " "*(NUMBER_SPACE + COORD_SPACE)*2)
    print("="*(NUMBER_SPACE + COORD_SPACE)*4 + "="*(len(title)))
    print(" "*3 + "\tID \t" + "X coordinate\t" + "Y coordinate\t" +
             "Elevation\t" + "Description")
    print("-"*(NUMBER_SPACE + COORD_SPACE)*4 + "-"*(len(title)))    


def justshowdatapoints(dataset):
    for data in dataset:
            for item in data:
                index = data.index(item)
                if index == 0:
                    print("\t{}".format(item)+" " *
                          (NUMBER_SPACE-len(str(item))), end="")
                elif index in [1, 2, 3]:
                    print("\t{}".format(round(item, 3))+" " *
                          (COORD_SPACE-len(str(item))), end="")
                else:
                    print("\t{}".format(item), end="")
            print("\n")


def showdatapoints(dataset, option):
    for data in dataset:

            if dataset.index(data) == option:
                print("{}".format(ARROW_CHAR), end="")
            else:
                print(" "*len(ARROW_CHAR), end="")

            for item in data:
                index = data.index(item)
                if index == 0:
                    print("\t{}".format(item)+" " *
                          (NUMBER_SPACE-len(str(item))), end="")
                elif index in [1, 2, 3]:
                    print("\t{}".format(round(item, 3))+" " *
                          (COORD_SPACE-len(str(item))), end="")
                else:
                    print("\t{}".format(item), end="")
            print("\n")


def justshowsurveyingdata(title, dataset):

    heading_point(title)
    justshowdatapoints(dataset)
    print("\nEsc to exit or press Enter to select option\n")
    input()


def showsurveyingdata(title,dataset):

    isValid = True
    option = 0

    while isValid:
        
        heading_point(title)
        showdatapoints(dataset, option)
        print("\nEsc to exit or press Enter to select option\n")
        # Catching cursor
        option,key_arrow = cursor_UP_DOWN(option)
        clear()      
        # Validating option
        option = validatingoption(option, dataset)
        # Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option
        # Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None


def main():
    title = "Surveying Data"
    dataset = [[0, 100, 100.234, 10, "initial"], [1, 200.345, 100.13456, 1240.45678, "final"], 
               [2, 300, 100, 0, "other point"], [3, 200, 300, 0, "other point"],
               [4, 800, 100, 0, "other point"], [5, 800, 700, 0, "other point around the park"]
               ]
    #showsurveyingdata(title, dataset)
    justshowsurveyingdata(title, dataset)
    title = "Radial Traversing"
    dataset2 = [
        ["A", "1", 200.234, 0.0000, "North"],
        ["A", "2", 100.234, 10.3456, "Corner"],
        ]
    justshowsurveyinginfo(title, dataset2)


if __name__ == "__main__":
    main()

