tup = ('Ford','Ferrari','Dodge','Suzuki','Mazda','For','BMW','Citroen','Lexus','Ford','Mazda','Mercedes-Benz')

print(f'Old tuple: {tup}')

old_word = str(input('enter the old manufacturer: '))
new_word = str(input('enter the new manufacturer: '))
y = list(tup)

for i in range(0,len(y)):
    if old_word in y[i]:
        y[i] = new_word

tup = tuple(y)
print(f'New tuple: {tup}')