#Exercise 1
from datetime import datetime
nl = '\n'

def loading_file(file,mode):
    try:
        f = open(file, mode)
        return f.read()
    except Exception as exc:
        print('ERROR', datetime.now().strftime("%d.%m.%y %H:%M:%S"), exc)
    finally:
        f.close()


def first():
    ls1 = loading_file('file2.txt','r')
    ls2 = loading_file('file2.txt','r')

    if ls1 == ls2:
        print(f'Are the same:\n{ls1} - {ls2}')
    else:
        print('their difference:')
        print(
            f'file1: {" ".join(list(set(ls1.replace(nl, " ").split(" ")).difference(set(ls2.replace(nl, " ").split(" ")))))}')
        print(
            f'file1: {" ".join(list(set(ls2.replace(nl, " ").split(" ")).difference(set(ls1.replace(nl, " ").split(" ")))))}')
#Exercise 2
def second():
    line = 1
    digit = 0
    ls3 = loading_file('Exercise2.txt','r')
    vow = ['a', 'e', 'i', 'o', 'u', 'y']
    con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    print(ls3)

    for i in ls3.split(' '):
        if '\n' in i:
            line += 1

    for i in ls3:
        if i.isdigit():
            digit += 1
    count_vow = [each for each in ls3.lower() if each in vow]
    count_con = [each for each in ls3.lower() if each in con]
    print(f'symbol: {len(ls3)}')
    print(f'line: {line}')
    print(f'vowels: {len(count_vow)}')
    print(f'Consonants: {len(count_con)}')
    print(f'digit: {digit}')
#Exercise 3
def third():
    ls4 = loading_file('Exercise3.txt', 'r')
    new_line = ls4.split('\n')
    new_line.pop()

    try:
        with open('Exercise31.txt', 'w') as file:
            file.write(' '.join(new_line))
    except Exception as exc:
        print('ERROR', datetime.now().strftime("%d.%m.%y %H:%M:%S"), exc)
    finally:
        file.close()
#Exercise 4
def fourth():
    ls5 = loading_file('Exercise3.txt', 'r')
    print(f'max line: {max(ls5.split(nl), key=len)}')

# first()
# second()
# third()
fourth()