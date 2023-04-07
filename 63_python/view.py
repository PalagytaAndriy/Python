def print_menu(func):

    def inner():
        print('Menu shop\n'
              'Mode: administrator\n'
              'Function:\n'
              '1.Add shoes in stock\n'
              '2.Show shoes in stock\n'
              '3.Exit')
        return func()

    return inner

# def index():
#     print('Menu shop\n'
#           'Mode: administrator\n'
#           'Function:\n'
#           '1.Add shoes in stock\n'
#           '2.Show shoes in stock\n'
#           '3.Exit')


def stock_contains(ls):
    print(f'Stock contains {len(ls)} Shoes\n')
    for item in ls:
        print(item)
        print()


def ending():
    print('you exit on shop, buy!')