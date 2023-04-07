import view
from model import Shoes
from view import end, stock


def show_all():
    shoes = Shoes.get_json()
    return stock(shoes)

@view.print_menu
def menu():
    return input(' --> ')

def start():

    answer = menu()

    while answer != '3':

        if answer == '1':
            Shoes.load_json(Shoes(input('Модель: '), input('Колір: '), input('Ціна: '), input('Виробник: '), input('Розмір: ')))
            answer = menu()
        elif answer == '2':
            show_all()
            answer = menu()
        else:
            print('------------------ Не вірний ввід -------------------')
            answer = menu()
    end()




if __name__ == '__main__':
    start()