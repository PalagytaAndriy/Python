class Node:

    def __init__(self, d):
        self.d = d
        self.n = None
        self.p = None


class Stack:

    def __init__(self):
        self.h = None
        self.t = None
        self.s = 0
        self.l = 5

    def is_empty(self):
        return True if self.h is None else False

    def is_full(self):
        return True if self.l == self.s else False

    def enqueue(self, data):
        if self.t is None:
            self.h = Node(data)
            self.t = self.h
        else:
            if self.l == self.s:
                print('Переповнений')
                return
            else:
                self.t.n = Node(data)
                self.t.n.p = self.t
                self.t = self.t.n
        self.s += 1

    def dequeque(self):
        if self.h is None:
            return None
        else:
            temp = self.h.d
            self.h = self.h.n
            if self.h != None:
                self.h.p = None
            self.s -= 1
            return temp

    def travel(self):
        print('Елементи :')
        temp = self.h
        while temp is not None:
            print(temp.d, end='--> ')
            temp = temp.n
        print('None')

    def __str__(self):
        ls = ''
        cur = self.h
        while cur is not None:
            ls += f'{cur.d} --> '
            cur = cur.n
        ls += 'None'
        return ls


def print_menu(func):
    def inner():
        print('1. Добавити до стеку\n'
              '2. Виштовхнути зі стеку\n'
              '3. Показати стек\n'
              '4. Перевірка на пустоту\n'
              '5. Перевірка чи повний\n'
              '6. Вихід\n')
        return func()

    return inner


@print_menu
def menu():
    return int(input('--> '))


ch = menu()

s = Stack()

while ch != 6:
    if ch == 1:
        s.enqueue(input('Введіть значення : '))
        print(s)
        ch = menu()
    elif ch == 2:
        print(f'Елемент видалений з очереді : {s.dequeque()}')
        print(s)
        ch = menu()
    elif ch == 3:
        s.travel()
        ch = menu()
    elif ch == 4:
        print(f'чи пустий ? : {s.is_empty()}')
        ch = menu()
    elif ch == 5:
        print(f'Чи повний ? : {s.is_full()}')
        ch = menu()
    else:
        print('Error')
