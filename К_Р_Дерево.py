class Node:
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    def clear(self):
        self._root = None

    def add(self, item):
        if self._root is None:
            self._root = Node(item)
        else:
            self.__add(item, self._root)

    def __add(self, item, node):
        if item < node.item:
            if node.left is not None:
                self.__add(item, node.left)
            else:
                node.left = Node(item)
        else:
            if node.right is not None:
                self.__add(item, node.right)
            else:
                node.right = Node(item)

    def find(self, item):
        if self._root == item:
            return self._root
        elif self._root is not None:
            return self.__find(item, self._root)
        else:
            return None

    def __find(self, item, node):
        if item == node.item:
            return node.item
        elif item < node.item and node.left is not None:
            return self.__find(item, node.left)
        elif item > node.item and node.ridht is not None:
            return self.__find(item, node.ridht)

    def delete(self, item):
        if self.root is not None:
            return self.__delete(item, self.root)
        else:
            return None

    def __delete(self, item, node):
        if node is None:
            return node

        if item < node.item:
            node.left = self.__delete(item, node.left)
        elif item > node.item:
            node.right = self.__delete(item, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.__find_min(node.right)
            node.item = temp.item
            node.right = self.__delete(temp.item, node.right)

        return node


    @staticmethod
    def __find_min(node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur




COUNT = [10]

def print2DUtil(root, space):
    if (root == None):
            return
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(' -->', root.item)
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)



t = Tree()
t.add(5)
t.add(7)
t.add(6)
t.add(4)
t.add(9)
t.add(10)
t.add(9)
t.add(8)
t.add(7.12)
t.delete(7)
t.delete(7.12)

print2D(t.root)

