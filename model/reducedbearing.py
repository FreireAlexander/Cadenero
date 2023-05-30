import math

class ReducedBearing:
    """
    Estos objetos son Rumbos en toda su definición, 
    Es decir, que es necesario escribir su cuadrante en la notación.
    Norte o Sur + ángulo en grados, minutos y segundos + Este u Oeste.
    De manera similar a los acimutes se tendrían las siguientes maneras de escribirlos, 
    recordando claro que al inicio y al final se debe especificar el cuadrante vertical al inicio y 
    el cuadrante horizontal al final:
    1. [Norte o Sur]numero entero  [Este u Oeste]
    2. [Norte o Sur]numero decimal [Este u Oeste]
    3. [Norte o Sur]numero decimal + ' o ° cualquiera de los dos [Este u Oeste]
    4. [Norte o Sur]numero entero + ' o ° + numero decimal o entero + ° o '  [Este u Oeste]
    5. [Norte o Sur]numero entero + ' o ° + numero entero [entre 0 a 59] + ° o ' + numero decimal o entero entre 0 y 59 + ' o ° o " [Este u Oeste]
    """
    value = None

    def __init__(self, value):
        if type(value)==type([]):
            if len(value)==3:
                self.degree_decimals = float(value[2])
                self.degree = int(math.floor(self.degree_decimals))
                self.minutes_decimals = round((self.degree_decimals - self.degree)*60,3)
                self.minutes = int(math.floor(self.minutes_decimals))
                self.seconds = round(float((self.minutes_decimals - self.minutes)*60),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
                self.vertical = value[0]
                self.horizontal = value[1]
            if len(value)==4:
                print("longitud 2")
                self.degree_decimals = float(value[2])
                self.degree = int(math.floor(self.degree_decimals))
                self.minutes_decimals = round(float(value[3]),3)
                self.minutes = int(math.floor(self.minutes_decimals))
                self.seconds = round(float((self.minutes_decimals - self.minutes)*60),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
                self.vertical = value[0]
                self.horizontal = value[1]
            if len(value)==5:
                self.degree_decimals = float(value[2])
                self.degree = int(self.degree_decimals)
                self.minutes_decimals = float(value[3])
                self.minutes = int(self.minutes_decimals)
                self.seconds = round(float(value[4]),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
                self.vertical = value[0]
                self.horizontal = value[1]               
    

    def print_angle(self):
        """
        Esta función imprime de manera organizada el Azimut en el formato de 
        grados, minutos y segundos. 
        """
        print(f'''{self.vertical} {self.degree}°{self.minutes}'{self.seconds}" {self.horizontal}''')