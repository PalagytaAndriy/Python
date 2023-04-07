class Node:
    def __init__(self,d):
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

    def enqueue(self,data):
        if self.t is None:
            self.h = Node(data)
            self.t = self.h
        else:
            if self.l == self.s:
                print('Heap Overflow')
                return
            else:
                self.t.n = Node(data)
                self.t.n.p = self.t
                self.t = self.t.n
        self.s += 1


    def dequeque(self):
        if self.h is None:
            return  None
        else:
            temp = self.h.d
            self.h = self.h.n
            if self.h != None:
                self.h.p = None
            self.s -= 1
            return temp


    def travel(self):
        print('Elem')
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
        print('\nWork with the stack\n')
        print('1.Add in stack\n'
              '2.Push from stack\n'
              '3.Show stack\n'
              '4.Check for emptiness\n'
              '5.Check for fulless\n'
              '6.Exit\n')
        return func()

    return inner

@print_menu
def menu():
    return int(input('Choose: '))


choose = menu()

s = Stack()

while choose != 6:
    if choose == 1:
        s.enqueue(input('Enter your value: '))
        print(s)
        choose = menu()
    elif choose == 2:
        print(f'Element removed from the queue: {s.dequeque()}')
        print(s)
        choose = menu()
    elif choose == 3:
        s.travel()
        choose = menu()
    elif choose == 4:
        print(f'Empty: {s.is_empty()}')
        choose = menu()
    elif choose == 5:
        print(f'Full: {s.is_full()}')
        choose = menu()
    else:
        print('Incorrect value')