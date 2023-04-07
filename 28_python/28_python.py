def first():
    checks = 0
    order_index = []
    orders = []

    menu = ['', 'Americano', 'Americano with milk', 'Latte', 'Cappuccino', 'Espresso']
    customers = int(input('How many are you?\n'))
    print(f'{customers} Person')

    for i in range(1, customers + 1):

        print(f'Num 1: Americano - 10$\n'
              f'Num 2: Americano with milk - 12$\n'
              f'Num 3: Latte - 15$\n'
              f'Num 4: Cappuccino -20$\n'
              f'Num 5: Espresso- 6$\n')

        choice = int(input("Choice: "))
        if not choice or choice < 1 or choice > 5:
            print('You don\'t make a choice')
        else:
            order_index.append(choice)

        kek = input("Add something else y/n\n")

        while kek.lower() == 'y' or kek.lower() == 'yes':
            choice = int(input("Choice: "))
            if not choice or choice < 1 or choice > 5:
                print('You don\'t make a choice')
            else:
                order_index.append(choice)
            kek = input("Add something else y/n\n")

        if i != customers:
            print('Next person')

    for j in order_index:
        orders.append(menu[j])

    for i in range(1, len(order_index) + 1):
        if i == 1:
            checks += 10
        elif i == 2:
            checks += 12
        elif i == 3:
            checks += 15
        elif i == 4:
            checks += 20
        elif i == 5:
            checks += 6

    print('Your order: {} '.format(', '.join(orders)))
    print(f'Your chang: {checks}$')

def second():
    start = int(input('Enter start range: '))
    end = int(input('Enter end range: '))
    array = []
    for i in range(start, end+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:array.append(i)
    print('Simple value in range:')
    print(array)

def thord():

    st = str(input('Enter your word: '))
    if st == st[::-1]:
        print(f'This word {st} - polinom')
    else: print(f'it\'s not polinom')