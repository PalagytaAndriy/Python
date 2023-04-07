import view
from model import Shoes
from view import  ending, stock_contains


def show_all():
    shoes = Shoes.get_json_request()
    return stock_contains(shoes)

@view.print_menu
def menu():
    return  int(input('Choose: '))

def start():

    answer = menu()

    while answer != 3:

        if answer == 1:
            ''' Shoes('male', 'snickers', 'green', '50$', 'Puma', 39) '''
            Shoes.load_json_request(Shoes(input('Male or Female: '), input('Type shoes: '), input('Color: '),
                                                 input('Prise: '), input('Manufacturer: '), int(input('Size: '))))
            answer = menu()
        elif answer == 2:
            show_all()
            answer = menu()
        else:
            print('Incorrect value')
            answer = menu()
    ending()




if __name__ == '__main__':
    start()