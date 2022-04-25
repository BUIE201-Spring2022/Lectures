class TreeItem:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def insert(self, new_data):        
        if new_data < self._data:
            if self._left is None:
                self._left = TreeItem(new_data)
            else:
                self._left.insert(new_data)
        else:
            if self._right is None:
                self._right = TreeItem(new_data)
            else:
                self._right.insert(new_data)

    def print(self, level):
        if self._right is not None:
            self._right.print(level + 1)
        print (level * "  ", self._data)
        if self._left is not None:
            self._left.print(level + 1)

class Tree201:
    def __init__(self):
        self._root = None

    def insert(self, new_data):
        if self._root is None:
            self._root = TreeItem(new_data)
        else:
            self._root.insert(new_data)

    def print(self):      
        if self._root is not None:
            self._root.print(1)


t = Tree201()
t.insert(6)
t.insert(3)
t.insert(4)
t.insert(8)
t.insert(7)

t.print()