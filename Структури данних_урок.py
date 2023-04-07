
import llist


class Node:
    def __init__(self, item):
        self.item = item
        self.next = Node


n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

n1.next = n2
n2.next = n3
#print(f'n1 - {n1}, n2 - {n2}, n3 - {n3}')

cur = n1

while cur:
    print(cur.item)
    cur = cur.next



class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node



    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node



    def insert(self, position, item):
        if position == 0:
            self.add(item)
        elif 0 < position < self.__len__():
            node = Node(item)
            count = 0
            cur = self.head
            while cur:
                if position == count + 1:
                    node.next = cur.next
                    cur.next = node
                cur = cur.next
                count += 1


        else:
            raise 'index out of range'







    def travel(self):
        cur = self.head
        while cur:
            print(cur.next, end= '--> ')
            cur = cur.next
        print('None')


    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count




    def is_empty(self):
        return self.head is None

ls = LinkedList()

ls.add(5)
ls.add(10)
ls.append(8)
ls.travel()

