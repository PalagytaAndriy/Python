class Node:
    def __init__(self,i):
        self.i = i
        self.n = None
        self.p = None

# add ->(if this value are available from list, call mesegge about it, and don't addintion value ),
# remove all added value from list
# show list from the end or the start
# check value in list
# value  replace in list (user decide, which replace only first value or all )
class DoubleList:
    def __init__(self):
        self.h = None
        self.t = None

    def is_empty(self):
        return  not self.h

    def add(self,x):
        node = Node(x)
        if self.is_empty():
            self.h = self.t =  node
        else:
            cur = self.h
            while cur:
                if cur.i == node.i:
                    return print('this value are available from list')
                cur = cur.n

            node.n = self.h
            self.h.p = node
            self.h = node

    def remove(self,x):

        if self.is_empty():
            print('List empty')
            return

        cur = self.h
        while cur is not None and cur.i != x:
            cur = cur.n

        if cur is None:
            print(f'{x} dose not exist in the list')
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
        return  ls

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

    def search(self,x):
        cur = self.h
        while cur:
            if cur.i == x:
                return print(f'find: {cur.i}')
            cur = cur.n
        return print('This variable not found')

    def replase(self,target,item):
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
        return print('This variable not found')



def print_menu(func):

    def inner():
        print('\nWork with the list\n')
        print('1.Add in list\n'
              '2.Remove from list\n'
              '3.Show list\n'
              '4.Check value in list\n'
              '5.Value replace in list\n'
              '6.Exit\n')
        return func()

    return inner

@print_menu
def menu():
    return int(input('Choose: '))


choose = menu()

ddl = DoubleList()

while choose != 6:

    if choose == 1:
        ddl.add(input('Enter your value: '))
        print(ddl)
        choose = menu()
    elif choose == 2:
        ddl.remove(input('Enter your value: '))
        print(ddl)
        choose = menu()
    elif choose == 3:
        print('Show you from the end or the start?')
        choose_show = str(input('S/E\nChoose: '))
        if choose_show.upper() == 'S':
            ddl.travel(start=True)
        elif choose_show.upper() == 'E':
            ddl.travel(start=False)
        else:
            print('Inccorect value')
        choose = menu()
    elif choose == 4:
        ddl.search(input('Enter your value: '))
        choose = menu()
    elif choose == 5:
        ddl.replase(input('enter value to find from list: '),input('Enter new value: '))
        print(ddl)
        choose = menu()
    else:
        print('Inccorect value')