class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def __str__(self):
        line = ''
        cur = self.head
        while cur is not None:
            line += f'{cur.item} -->'
            cur = cur.item
        line += 'None'
        return line

    def travel(self, start: bool = True):
        if start:
            cur = self.head
            while cur is not None:
                print(f'{cur.item} --> ', end=' ')
                cur = cur.next
        else:
            cur = self.tail
            while cur is not None:
                print(f'{cur.item} --> ')
                cur = cur.previous

    def add_to_front(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def add_to_back(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def insert(self, target, item):
        node = Node(item)
        cur = self.head
        prev_node = None

        while cur.item != target:
            prev_node = cur
            cur = cur.next

        node.next = prev_node.next
        prev_node.next.previous = node

        prev_node.next = node
        node.previous = prev_node


    def delete_first(self):
        if self.is_empty():
            print('list empty')
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def delete_last(self):
        if self.is_empty():
            print('list empty')
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            prev = self.tail.previous
            prev.next = None
            self.tail = prev

    def delete_key(self, key):
        if self.is_empty():
            print('list empty')
            return
        cur = self.head
        while cur is not None and cur.item != key:
            cur = cur.next

        if cur is None:
            print(f'{key} not in the list')
            return

        prev = cur.previous
        if cur.next is None:
            self.tail = prev

        if prev is None:
            self.head = cur.next
            if self.head is not None:
                self.head.previous = None
        else:
            prev.next = cur.next
            cur.previous = None
            if prev.next is not None:
                prev.next.previous = prev






dll = DoublyLinkedList()
dll.add_to_front(5)
dll.add_to_front(10)
dll.add_to_front(15)
#dll.add_to_back(20)
#dll.insert(5, 4)
#dll.delete_first()
#dll.delete_last()
#dll.delete_key(5)
#dll.delete_key(4)
#dll.delete_key(10)
dll.travel()






n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

n1.next = n2
n2.next = n3

n3.previous = n2
n2.previous = n1

cur = n3
while cur is not None:
    print(cur.item, ' --> ', end=' ')
    cur = cur.previous
print('None')

cur = n1
while cur is not None:
    print(cur.item, ' --> ', end=' ')
    cur = cur.next
print('None')











class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        node = Node(x)
        if node is None:
            print('Heap Overflow')
            return

        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print('Heap Overflow')
            return
        top = self.top.item
        self.top = self.top.next
        self.size -= 1
        return top


    def is_empty(self):
        return self.top is None

    def get_top(self):
        if not self.is_empty():
            return self.top.item
        else:
            print('stack empty')

    def size(self):
        return self.size


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(f'Top: {stack.get_top()}')
stack.pop()
stack.pop()
print(f'Top: {stack.get_top()}')
stack.pop()
print(f'Stack empty?  {stack.is_empty()}')











































