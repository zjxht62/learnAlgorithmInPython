class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.head is None

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        is_over = False
        while current is not None and not found and not is_over:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    is_over = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        current: Node = self.head
        previous: Node = None
        found_larger: bool = False
        while current is not None and not found_larger:
            if current.get_data() > item:
                found_larger = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous is None:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)

if __name__ == '__main__':
    ol = OrderedList()
    ol.add(17)
    ol.add(26)
    ol.add(54)
    ol.add(77)
    ol.add(93)
