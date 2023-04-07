# exercise_1
def first():
    num = input("Enter a six-digit number: ")
    if not num or len(num) != 6:
        print('error')
    elif (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
        print('Enter a six-digit number')
    else:
        print('you have an unlucky number')
# exercise_2
def second():
    num = input("Enter a six-digit number: ")
    if not num or len(num) != 6:
        print('error')
    else: print(f'{num[5]}{num[4]}{num[2]}{num[3]}{num[1]}{num[0]}')
# exercise_3
def third():
    month = int(input('Enter value a month: '))
    if 1 <= month <= 2 or month == 12: print('Winter')
    elif 3 <= month <= 5: print('Spring')
    elif 6 <= month <= 8: print('Summer')
    elif 9 <= month <= 11:print('Autumn')
    else: print('error')