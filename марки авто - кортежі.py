q = input(str(" введіть назву яку шукаємо - "))
w = input(str(" введіть слово для заміни - "))
avto = ('Lancia', 'Mazda', 'Lexus' , 'BMW', 'Renault', 'Renault','Mazda', 'BMW', 'BMW')
avto_1 = list(avto)
print(avto)
i = 0
for i in range(len(avto_1)):
    if avto_1[i] == q:
        avto_1[i] = w
print()
avto_3 =tuple(avto_1)
print(avto_3)
