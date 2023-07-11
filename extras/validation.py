import re
import model

# Patrones para identificar el ingreso de un ángulo e identificarlo
# Por el momento solo se aceptan ángulos positivos.
p_integer     = r"^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)$"
p_decimal     = r"^(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)$"

p_angle_d     = re.compile(r"""  
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    | # o inicia por numero decimal
    ^(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE)

p_angle_dm    = re.compile(r"""  
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE)

p_angle_dms   = re.compile(r"""  
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    $
    """, re.VERBOSE)

p_bearing_d     = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9]\.\d+)|([0-9])|([1-8][0-9]\.\d+)|([1-8][0-9])|(90))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dm    = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(90))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dms   = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(90))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

def formatangle(text: str):
    numbers = text.replace(" ", "").replace("'", "°").replace('"', '°').split('°')[:-1]
    return model.WholeCircleBearing(numbers)



def isAngle(text: str):
    flag = False
    if re.match(p_integer, text):
        flag = True
    if re.match(p_decimal, text):
        flag = True
    if isWholecirclebearing(text):
        flag = True   
    if isBearing(text):
        flag = True

    return flag    
    
def isWholecirclebearing(angle):
    flag = False
    if re.match(p_angle_d, angle):
        flag = True
    if re.match(p_angle_dm, angle):
        flag = True
    if re.match(p_angle_dms, angle):
        flag = True

    return flag   


def isBearing(angle):
    flag = False
    if re.match(p_bearing_d, angle):    
        flag = True
    if re.match(p_bearing_dm, angle):    
        flag = True
    if re.match(p_bearing_dms, angle):    
        flag = True
    
    return flag 

def setangle(text: str):
    if re.match(p_integer, text):
        return model.WholeCircleBearing([text])
    if re.match(p_decimal, text):
        return model.WholeCircleBearing([text])
    if re.match(p_angle_d, text):
        return formatangle(text)
    if re.match(p_angle_dm, text):
        return formatangle(text)
    if re.match(p_angle_dms, text):
        return formatangle(text)
    if re.match(p_bearing_d, text):    
        return formatbearing(text)
    if re.match(p_bearing_dm, text):    
        return formatbearing(text)
    if re.match(p_bearing_dms, text):    
        return formatbearing(text)

def formatbearing(text: str):
    text = text.lower().replace(" ", "")
    if re.match(r"([sS]{1}|(sur|south))", text):
        vertical = 'S'
        text = text.replace("sur", "").replace("south", "")
    if re.match(r"([nN]{1}|(norte|north))", text):
        vertical = 'N'
        text = text.replace("norte", "").replace("north", "")
    if re.search(r"([wWoO]{1}|(oeste|west))", text):
        horizontal = 'W'
        text = text.replace("oeste", "").replace("west", "")
    elif re.search(r"([eE]{1}|(este|east))", text):
        horizontal = 'E'
        text = text.replace("este", "").replace("east", "")

    text = text.replace("s", "").replace("n", "").replace("e", "").replace("w", "").replace("o", "")
    numbers = text.replace("'", "°").replace('"', '°').split('°')[:-1]
    numbers.insert(0, horizontal)
    numbers.insert(0, vertical)
    
    return model.ReducedBearing(numbers)  