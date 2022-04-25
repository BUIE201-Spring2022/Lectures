class ListItem:
    def __init__(self, data, next = None):
        self._data = data
        self._next = next

    def next(self):
        return self._next

    def update(self, data = None, next = None):
        if data is not None:
            self._data = data
        if next is not None:
            self._next = next

    def print(self):
        print (self._data)

class List201:
    def __init__(self):
        self._head = None

    def insert_at_head(self, new_data):
        new_list_item = ListItem(new_data, self._head)
        self._head = new_list_item

    def insert_at_tail(self, new_data):
        new_list_item = ListItem(new_data)

        if self._head is None:
            self._head = new_list_item
        else:    
            list_item = self._head
            while list_item.next() is not None:
                list_item = list_item.next()

            list_item.update(next = new_list_item)

    def print(self):
        print ("")
        list_item = self._head
        while list_item is not None:
            list_item.print()
            list_item = list_item.next()

lst = List201()
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(12)

lst.print()

lst.insert_at_tail(15)

lst.print()
