from objects import Coord, Line

def main() -> int:

    coordinate = Coord(1,3.434567)
    coordinate_1 = Coord(1, 5.778923)

    print(f"Coordinate 0: {coordinate} \nCoordinate 1: {coordinate_1}")

    line = Line(coordinate, coordinate_1)
    line2 = Line(coordinate_1, coordinate)
    
    print(line)
    print(line2)
    print(f"get precision Line 1 -> {line.precision}")
    print(f"get precision Line 2 -> {line2.precision}")

    print(f"Lenght of Line 1: {line.len}\nLenght of line 2: {line2.len}")

    line2.precision = 10
    
    print("Changing precision for lenght")

    print(f"get precision Line 1 -> {line.precision}")
    print(f"get precision Line 2 -> {line2.precision}")

    print(f"Lenght of Line 1: {line.len}\nLenght of line 2: {line2.len}")

    try: 
        line2.len = 200
    except:
        print("Len can not be modified by user")

    print(f"New Lenght line 2: {line2.len}")

    print(f"Vector for Line 1: {line.vector}\nVector for line 2: {line2.vector}")

    return 0

if __name__ == "__main__":
    main()