import re

# Patrones para identificar el ingreso de un ángulo e identificarlo
# Por el momento solo se aceptan ángulos positivos.
p_integer     = r"^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)$"
p_integer_n   = r"^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)$"
p_decimal     = r"^(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)$"
p_decimal_n   = r"^-(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)$"
p_angle_d     = re.compile(r"""  
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    | # o inicia por numero decimal
    ^(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE)
p_angle_d_n     = re.compile(r"""  
    ^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    | # o inicia por numero decimal
    ^-(\d+\.\d+|\s+\d+\.\d+|\d+\.\d+\s+|\s+\d+\.\d+\s+)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE)

p_angle_dm    = re.compile(r"""  
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))   
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    |
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    $
    """, re.VERBOSE)

p_angle_dm_n    = re.compile(r"""  
    ^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))   
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    |
    ^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
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
    |
    ^(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    $
    """, re.VERBOSE)

p_angle_dms_n   = re.compile(r"""  
    ^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    $
    |
    ^-(\d+|\s+\d+|\d+\s+|\s+\d+\s+)    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    $
    """, re.VERBOSE)

p_bearing_vertical    = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_d     = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9]\.\d+)|([0-9])|([1-8][0-9]\.\d+)|([1-8][0-9])|(90))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9]\.\d+)|([0-9])|([1-8][0-9]\.\d+)|([1-8][0-9])|(90))\s*
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dm_vertical   = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)\s*
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dm    = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(89))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(89))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (90)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (90)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)\s*
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dms   = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(89))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (90)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (90)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)\s*
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (([0-9])|([1-8][0-9])|(89))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9])|([1-5][0-9]))
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    ([eEwWoO]{1}|(este|oeste|east|west))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_bearing_dms_vertical  = re.compile(r"""  
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)\s*
    $
    |
    ^([nNsS]{1}|(sur|norte|south|north))\s*
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (0)\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_azimuth_integer = re.compile(r"""
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    $
    |
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE | re.IGNORECASE)

p_azimuth_decimal = re.compile(r"""
    ^(
    (?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360))|
    ((?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)
    )
    $
    |
    ^(
    (?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360))|
    ((?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE | re.IGNORECASE)


p_azimuth_d = re.compile(r"""
    ^(
    (?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360))|
    ((?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)|
    (\s+(?:0|0\.\d+|[1-9][0-9]|[1-9][0-9]\.\d+?|1[0-9]{2}|1[0-9]{2}\.\d+|2[0-9]{2}||2[0-9]{2}\.\d+|3[0-5][0-9]|3[0-5][0-9]\.\d+|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    """, re.VERBOSE | re.IGNORECASE)

p_azimuth_dm = re.compile(r"""
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))   
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    $
    |
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)

p_azimuth_dms = re.compile(r"""
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))   
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))    
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+|"|"\s+|\s+"|\s+"\s+)
    $
    |
    ^(
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360))|
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)|
    (\s+(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-9]{2}|3[0-5][0-9]|360)\s+)
    )
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))   
    (°|°\s+|\s+°|\s+°\s+|'|'\s+|\s+'|\s+'\s+)
    (([0-9]\.\d+)|([0-9])|([1-5][0-9]\.\d+)|([1-5][0-9]))\s*
    $
    """, re.VERBOSE | re.IGNORECASE)