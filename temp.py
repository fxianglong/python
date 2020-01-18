class Celsius:
    def __init__(self,value=26.0):
        self.value = float(value)

    def __get__(self,instance,value):
        return self.value

    def __set__(self,instrance,value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self,instrance,value):
        return instrance.cel*1.8+32

    def __set__(self,instrance,value):
        instrance = (float(instance.cel*1.8+32))

class Tempature:
    cel = Celsius()
    fah = Fahrenheit()

        
