class Node:
    def __init__(self,item):
        self.i = item
        self.n = None
        self.p = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.limit = 3

    def push(self,x):
        node = Node(x)
        if node is None or self.limit == self.size:
            print('Heap Overflow')
            return

        node.n = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print('Heap Overflow')
            return

        self.top = self.top.n
        self.size -= 1

    def size_stack(self):
        return self.size

    def empty(self):
        return  self.top is None

    def full(self):
        return True if self.limit == self.size else False

    def clear(self):
        self.top = None
        self.size = 0
        # self.top.n = None

    def get_item(self):
        if not self.empty():
            return self.top.i
        else:
            print('Stack empty')

    def travel(self):
        cur = self.top
        while cur is not None:
            print(f'{cur.i} -> ', end='')
            cur = cur.n
        print('None')



s = Stack()

def print_menu(func):

    def inner():
        print('\nWork with the stack\n')
        print('1.Add in stack\n'
              '2.Push from stack\n'
              '3.Size the stack\n'
              '4.Check for emptiness\n'
              '5.Check for fulless\n'
              '6.Clear  stack\n'
              '7.Get item\n'
              '8.Show stack\n'
              '9.Exit\n')
        return func()

    return inner

@print_menu
def menu():
    return int(input('Choose: '))


choose = menu()

while choose != 9:

    if choose == 1:
        s.push(input('Enter your value: '))
        s.travel()
        choose = menu()
    elif choose == 2:
        print('The last element was a delete from stack')
        s.pop()
        s.travel()
        choose = menu()
    elif choose == 3:
        s.size_stack()
        choose = menu()
    elif choose == 4:
        print(f'Empty: {s.empty()}')
        choose = menu()
    elif choose == 5:
        print(f'Full: {s.full()}')
        choose = menu()
    elif choose == 6:
        s.clear()
        choose = menu()
    elif choose == 7:
        print(s.get_item())
        choose = menu()
    elif choose == 8:
        s.travel()
        choose = menu()
    else:
        print('Inccorect value')

#Если еще надо третье задание то я доделаю оно не сложное