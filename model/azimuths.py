import math

class Azimuth:
    """
    Estos objetos son ángulos en el sentido de las manecillas del reloj a partir del Norte, 
    Es decir, son exclusivamentes azimutes por el momento, pueden ser escritos de la sgte manera.
    Siguiendo la notación de los ángulos en grados, minutos y segundos o de forma numeríca, para
    la separación entre grados minutos o segundos se puede utilizar lso caracteres de ° o ' para 
    los grados o los minutos y el caracter de " para los segundos, es obligatorio ponerlo si o sí 
    para que el programa identifique si se trata de un ángulo con grados, grados y minutos o grados, 
    minutos y segundos.
    1. numero entero 
    2. numero decimal
    3. numero decimal + ' o ° cualquiera de los dos
    4. numero entero + ' o ° + numero decimal o entero + ° o ' 
    5. numero entero + ' o ° + numero entero [entre 0 a 59] + ° o ' + numero decimal o entero entre 0 y 59 + ' o ° o "
    """
    value = None

    def __init__(self, value):
        if type(value)==type([]):
            value[0]=float(value[0])
            self.spin_number = int(value[0] // 360)
            self.spin_number_decimal = round(value[0] / 360, 3)
            value[0] = value[0] - 360*self.spin_number
            
            if len(value)==1:
                self.degree_decimals = value[0]
                self.degree = int(math.floor(self.degree_decimals))
                self.minutes_decimals = round((self.degree_decimals - self.degree)*60,3)
                self.minutes = int(math.floor(self.minutes_decimals))
                self.seconds = round(float((self.minutes_decimals - self.minutes)*60),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
            if len(value)==2:
                self.degree_decimals = value[0]
                self.degree = int(math.floor(self.degree_decimals))
                self.minutes_decimals = round(float(value[1]),3)
                self.minutes = int(math.floor(self.minutes_decimals))
                self.seconds = round(float((self.minutes_decimals - self.minutes)*60),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
            if len(value)==3:
                self.degree_decimals = value[0]
                self.degree = int(self.degree_decimals)
                self.minutes_decimals = float(value[1])
                self.minutes = int(self.minutes_decimals)
                self.seconds = round(float(value[2]),3)
                self.decimal = (self.degree+self.minutes/60+self.seconds/3600)
    
    def print_angle(self):
        """
        Esta función imprime de manera organizada el Azimut en el formato de 
        grados, minutos y segundos. 
        """
        print(f'''{self.degree}°{self.minutes}'{self.seconds}"''')
    