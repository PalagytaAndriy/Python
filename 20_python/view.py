def print_menu(func):

    def inner():
        print('\nМеню магазина\n\n'
              '1.Добавити взуття на склад магазина\n'
              '2.Показати яке взуття є на складі в магазині\n'
              '3.Вихід\n')
        return func()

    return inner


def stock(ls):
    print(f'-------------------- В магазині є {len(ls)} пар взуття -------------------------\n')
    for item in ls:
        print(item)
        print()


def end():
    print('-------------------------- До зустрічі ----------------------------')