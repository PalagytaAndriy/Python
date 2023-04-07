import os
import time

name_file = []
str = ''
i = ''

while 'quit' not in name_file:

    i = input('Enter name file: ')
    if i == 'quit':
        break
    else:
        if os.path.exists(i) and i not in name_file:
            name_file.append(i)
        else:
            if i in name_file:
                print(f'Error, this file - {i},already been added ')
            else:
                print('Error, file not found')


print(f'files name: {" ".join(name_file)}')

for i in list(set(name_file)):
     with open(i,'r') as f:
         str += f.read()

print(f'value from files: {str}')

with open('result.txt','w') as f:
    print('Loading results', end=' ')
    for i in range(0,4):
        time.sleep(1)
        print(' . ', end='')
    f.write(str)
