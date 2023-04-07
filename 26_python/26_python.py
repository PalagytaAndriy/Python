num = int(input('Enter size: '))
for x in range(0, num):
        for j in range(1, 5):
                print('* '*num + '_ '*num, end='')
        print('\n')
for x in range(0, num):
        for j in range(1, 5):
                print('_ ' * num + '* ' * num, end='')
        print('\n')