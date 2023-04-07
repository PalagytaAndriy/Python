class FirstSimpleClass:

    def __init__(self, arr: set):
        self._arr = arr

    def sum_set(self):
        return  sum({i for i in self._arr})

    def avg_set(self):
        return  sum({i for i in self._arr})/len(self._arr)

    def max_set(self):
        return max(self._arr)

    def min_set(self):
        return min(self._arr)


class SecondSimpleClass:

    def __init__(self,value = None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise TypeError('error')

    def  convert_value_to_octal_system(self):
        return  oct(self._value)

    def  convert_value_to_hexadecimal_system(self):
        return hex(self._value)

    def  convert_value_to_binary_system(self):
        return bin(self._value)


# ssc = SecondSimpleClass(10)
# ssc.value = '10'
# print(ssc.convert_value_to_binary_system())
# print(ssc.convert_value_to_octal_system())
# print(ssc.convert_value_to_hexadecimal_system())