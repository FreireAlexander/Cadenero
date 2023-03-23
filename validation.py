# Libraries
import re
import calculus as calc


def is_positive_number(number):
	num_format = r'^\d+(\.\d+)?$'
	return bool(re.match(num_format, number))

def is_number(number):
	patron = r'^-?\d+(\.\d+)?$'
	return bool(re.match(patron,number))

def is_dms(angle):
     patron = r''
     return bool(re.match(patron, angle, re.IGNORECASE))

def isbearing(bearing):
    bearingformat = re.compile(r"^[nNsS][ ]?([0-9]|[1-8][0-9])[°']([0-9]|[1-5][0-9])[°'](0|0?\.[1-9]*|[1-9](?:\.[0-9]*)?|[1-5][0-8](?:\.[0-9]*)?|[5][9])[°']?[°'][ ]?[EeWwOo]$")
    return re.match(bearingformat,bearing)


def isbearing2(bearing):
    bearingformat1 = re.compile(r"^[nNsS][ ]?([9][0])[°']([0])[°'](0)[°']?[°'][ ]?[EeWwOo]$")
    return re.match(bearingformat1,bearing)


def isbearingdecimal(bearing):
    bearingformat = re.compile(r"^[nNsS][ ]?((?:\.[0-9]*)?|[1-8][0-9](?:\.[0-9]*)?|[9][0])[°']?[ ]?[EeWwOo]")
    return re.match(bearingformat,bearing)

def isdms(bearing):
    bearingformat = re.compile(r"^[ ]?([0-9]*)[°']([0-9]|[1-5][0-9])[°'](0|0?\.[1-9]*|[1-9](?:\.[0-9]*)?|[1-5][0-8](?:\.[0-9]*)?|[5][9])[°']?[°'][ ]?$")
    return re.match(bearingformat,bearing)


def bearingdata(bearing):
    bearingdata = ''
    quadrant = ''
    for char in bearing:

        if char not in [' ','N','n','S','s','W','w','E','e','O','o']:
            bearingdata += char
        elif char in ['N','n','S','s','W','w','E','e','O','o']:
            quadrant += char.upper()

    bearingdata = bearingdata.replace("''","°")
    bearingdata = bearingdata.replace("'°","°")
    bearingdata = bearingdata.replace("°'","°")
    bearingdata = bearingdata.replace("°°","°")
    bearingdata = bearingdata.replace("'","°")
    bearingdata = bearingdata.split("°")
    bearingdata.pop()
    bearingdata.append(quadrant)

    return bearingdata

def bearingdata_decimal(bearing):
    bearingdata = ''
    quadrant = ''
    for char in bearing:

        if char not in [' ','N','n','S','s','W','w','E','e','O','o','°',"'"]:
            bearingdata += char
        elif char in ['N','n','S','s','W','w','E','e','O','o']:
            quadrant += char.upper()

    bearinginfo = [bearingdata]
    bearinginfo.append(quadrant)

    return bearinginfo

# Function for testing
def run():
    number = input("Input number: ")
    print(f"es angulo en d:m:s {isbearing(number)}")
    print(f"es numero {is_dms(number)}")


if __name__ == "__main__":
	run()

