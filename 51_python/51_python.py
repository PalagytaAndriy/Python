class Circle():

    def __init__(self,r):
        self.r = r

    def __add__(self, other):
        return self.r + other

    def __iadd__(self, other):
        self.r += other
        return  self.r

    def __sub__(self, other):
        self.r -= other
        return self.r

    def __isub__(self, other):
        return self.r - other

    def __eq__(self, other):
        return self.r == other
    def __lt__(self, other):
        return  self.r < other
    def __gt__(self, other):
        return  self.r > other
    def __le__(self, other):
        return  self.r <= other
    def __ge__(self, other):
        return  self.r >= other

o1 = Circle(5)
o2 = Circle(3)
print(o1+3)
print(o1-3)
o1 +=1
o2 -=2
print(o1)
print(o2)
print(o1==o2)
print(o1<o2)
print(o1>o2)
print(o1<=o2)
print(o1>=o2)

class Complex(object):

    def __init__(self, arg, static):
        self.arg = arg
        self.static = static
        # Formats our results
        print(self.arg + self.static)

    def __add__(self, other):
        return Complex(self.arg + other.arg, self.static + other.static)

    def __sub__(self, other):
        return Complex(self.arg - other.arg, self.static - other.static)

    def __mul__(self, other):
        return Complex((self.arg * other.arg) - (self.static * other.static),(self.static * other.arg) + (self.arg * other.static))

    def __truediv__(self, other):
        r = (other.arg ** 2 + other.static ** 2)
        return Complex((self.arg * other.arg - self.static * other.static) / r,(self.static * other.arg + self.arg * other.static) / r)

a1 = Complex(1, 5j)
a2 = Complex(6, 2j)

# Add
a1 + a2
# Subtract
a1 - a2
# Multiply
a1 * a2
# Divide
a1 / a2