
class Circle:
    def __init__(self, r1):
        self.__r1 = r1


    def info(self):
        return f"{self.__r1}"

    def __eq__(self, other):
        return self.__r1 == other

    def __lt__(self, other):
        return self.__r1 < other

    def __gt__(self, other):
        return self.__r1 > other

    def __le__(self, other):
        return self.__r1 <= other

    def __ge__(self, other):
        return self.__r1 >= other

    def __mul__(self, other):(self):
        return Circle(2 * 3.14 * self.__r1)

n1 = Circle(10)
n2 = Circle(5)
print('Перевірка на рівність')
if n1 == n2:
    print('Радіуси рівні')
else:
    print('Радіуси різні')
print()



print(n1.info())
print(n2.info())


#print(n2 < 2)
#print(n2 > 2)
#print(n2 <= 2)
#print(n2 >= 2)