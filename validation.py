import re
import calculus as calc

def ToNumber(number):
	try:
		number = float(number)
	except ValueError:
		number = 0

	return number

def positive_number_validation(number):
	num_format = re.compile(r'^([.][0-9]*|0[.0-9]*|[1-9][0-9]*[.0-9]*)$')
	return re.match(num_format, number)

def number_validation(number):
	num_format = re.compile(r'^[^!\v$][^!\D$]\-?[0-9]*[.0-9]*$|^[\d][.0-9]*|^[ -][.0-9]*')
	return re.match(num_format,number)


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

