num = int(input("Enter number: "))

th = ['', "M", "MM", "MMM"]
h = ['', "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
t = ['', "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
o = ['', "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

result = th[(num // 1000)] + h[((num % 1000) // 100)] + t[((num % 100) // 10)] + o[num % 10]

print(result)