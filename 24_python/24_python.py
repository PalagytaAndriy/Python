# exercise_1
def first():
    print(input('Enter value first: ') +
          input('Enter value second: ') +
          input('Enter value third: '))
# exercise_2

def second():
    num = int(input('Enter your number:'))
    num1 = num // 1000
    num2 = (num // 100) % 10
    num3 = (num // 10) % 10
    num4 = num % 10

    return num1,num2,num3,num4
    # print(num1 * num2 * num3 * num4)

# exercise_3

def third():
    metr = int(input('Enter value metters:'))
    cm = metr * 100
    dm = metr * 10
    mm = metr * 100
    ml = metr * 1609
    print(f'centimeters to meters: {cm}cm\n'
          f'decimeters to meters: {dm}dm\n'
          f'millimeters to meters: {mm}mm\n'
          f'miles per meter: {ml}ml\n')

# exercise_4
def fourth():
    main = int(input('Enter main triangle: '))
    hight = int(input('Enter hight triangle: '))
    print(f'S = {1 / 2 * main * hight} (m\u00B2)')

# exercise_1
first()
# exercise_2
sec = second()
print(sec[0] * sec[1] * sec[2] * sec[3])
# exercise_3
third()
# exercise_4
fourth()
# exercise_5
fif = second()
print(f'{sec[3]}{sec[2]}{sec[1]}{sec[0]}')