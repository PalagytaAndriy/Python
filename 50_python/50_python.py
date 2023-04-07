class Fraction:
    c = 0
    count = 0
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1
        self.__class__.c += 1

    @classmethod
    def get_created_instances_count1(cls):
        return cls.c

    @staticmethod
    def get_created_instances_count2():
        return  Fraction.count


class TemperatureConversion:
    i = 0

    def __init__(self):
        self.__class__.i += 1

    @staticmethod
    def convert_celsius_to_fahrenheit(value):
        TemperatureConversion.i += 1
        return f'Fahrenheit = {round((value*1.8)+32)}'

    @staticmethod
    def convert_fahrenheit_to_celsius(value):
        TemperatureConversion.i += 1
        return f'Celsius = {round((value-32)*0.5556)}'

    @staticmethod
    def count():
        return TemperatureConversion.i

f1 = Fraction(1,2)
f2 = Fraction(3,5)

print(f'clasmethod: {Fraction.get_created_instances_count1()}')
print(f'staticmethod: {Fraction.get_created_instances_count2()}')

print(TemperatureConversion.convert_fahrenheit_to_celsius(50))
print(TemperatureConversion.convert_celsius_to_fahrenheit(30))
print(f'count: {TemperatureConversion.count()}')