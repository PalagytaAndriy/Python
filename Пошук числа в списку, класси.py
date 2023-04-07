class Node:
    def __init__(self, i):
        self.i = i
        self.n = None
        self.p = None

class DoubleList:
    def __init__(self):
        self.h = None
        self.t = None

    def is_empty(self):
        return not self.h

    def add(self, x):
        node = Node(x)
        if self.is_empty():
            self.h = self.t = node
        else:
            cur = self.h
            while cur:
                if cur.i == node.i:
                    return print('це значення доступне з списка')
                cur = cur.n

            node.n = self.h
            self.h.p = node
            self.h = node

    def remove(self, x):

        if self.is_empty():
            print('Список пустий')
            return

        cur = self.h
        while cur is not None and cur.i != x:
            cur = cur.n

        if cur is None:
            print(f'{x} -- error')
            return

        prev = cur.p

        if cur.n is None:
            self.t = prev

        if prev is None:
            self.h = cur.n
            if self.h is not None:
                self.h = None

        prev.n = cur.n
        prev.n.p = prev

    def __str__(self):
        ls = ''
        cur = self.h
        while cur is not None:
            ls += f'{cur.i} --> '
            cur = cur.n
        ls += 'None'
        return ls

    def travel(self, start: bool = True):
        ls = ''
        if start:
            cur = self.h
            while cur is not None:
                ls += f'{cur.i} --> '
                cur = cur.n
        else:
            cur = self.t
            while cur is not None:
                ls += f'{cur.i} --> '
                cur = cur.p
        print(f'{ls}None')

    def search(self, x):
        cur = self.h
        while cur:
            if cur.i == x:
                return print(f'Знайдено: {cur.i}')
            cur = cur.n
        return print('Таке число незнайдено')

    def replase(self, target, item):
        node = Node(item)
        cur = self.h

        while cur:
            if cur.i == target:
                while cur.i != target:
                    cur = cur.n

                node.n = cur.n
                node.p = cur.p

                if cur.n == None:
                    self.t = node
                    cur.n = None
                else:
                    cur.n.p = node

                if cur.p == None:
                    self.h = node
                    cur.p = None
                else:
                    cur.p.n = node

            cur = cur.n
        return print('Таке число незнайдено')



def print_menu(func):

    def inner():
        print('1.Додати до списку\n'
              '2.Видалити з списка\n'
              '3.Показати список\n'
              '4.Перевірити чи є число в списку\n'
              '5.Змінити значення в списку\n'
              '6.Вихід')
        return func()

    return inner

@print_menu
def menu():
    return int(input('--> '))


choose = menu()

ddl = DoubleList()

while choose != 6:

    if choose == 1:
        ddl.add(input('Введіть ваше значення -> '))
        print(ddl)
        choose = menu()
    elif choose == 2:
        ddl.remove(input('Введіть значення для видалення -> '))
        print(ddl)
        choose = menu()
    elif choose == 3:
        print('Показати список з початку чи кінця ?')
        choose_show = str(input('Початок - 1 '
                                'Кінець - 0\n'
                                '--> '))
        if choose_show.upper() == '1':
            ddl.travel(start=True)
        elif choose_show.upper() == '0':
            ddl.travel(start=False)
        else:
            print('error')
        choose = menu()
    elif choose == 4:
        ddl.search(input('Введіть ваше значення -> '))
        choose = menu()
    elif choose == 5:
        ddl.replase(input('Введіть яке значення змінити -> '),
                    input('Введіть НА ЯКЕ значення змінити -> '))
        print(ddl)
        choose = menu()
    else:
        print('error')