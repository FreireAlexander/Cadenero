

def setSexagesimal(angle):
    try:
        res = {
                    'sign': '',
                    'degree': 0,
                    'degree_decimal': 0,
                    'minutes': 0,
                    'minutes_decimal': 0,
                    'seconds': 0,
                    'seconds_decimals': 0
            }
        if angle < 0:
            res['sign']='-'
            angle *= -1
        res['degree'] = int(angle)
        res['degree_decimal'] = float(angle)
        res['minutes'] = int((res['degree_decimal'] - res['degree'])*60)
        res['minutes_decimal'] = (res['degree_decimal'] - res['degree'])*60
        res['seconds']= round(float(((angle - res['degree'])*60 - res['minutes'])*60),6)
        res['seconds_decimal']= round(float(((angle - res['degree'])*60 - res['minutes'])*60),6)
        return res
    except:
        raise ValueError(f" {angle} must be a int or float")

def toSexagesimal(angle):
    try:
        res = setSexagesimal(angle)
        return f'''{res['sign']}{res['degree']}°{res['minutes']}'{res['seconds']}"'''
    except:
        raise ValueError(f" {angle} must be a int or float")

