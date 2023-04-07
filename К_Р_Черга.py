class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Q:
    def __init__(self):
        self.head = None
        self.tail = None

    def first(self):
        return self.head if self.head else None

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def is_empty(self):
        return self.head is None


    def travel(self):
        print('Element: ')
        temp = self.head
        while temp is not None:
            print(temp.data, end=' --> ')
            temp = temp.next
        print('None')

    def enqueue(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

q = Q()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

q.travel()
q.dequeue()
q.travel()

