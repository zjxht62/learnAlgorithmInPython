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


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.get_next()
        return count

    def my_search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def my_remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                if current == self.head:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current
                current = current.get_next()

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        # 先查找是否存在匹配的数据项
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        # 再根据是否是表头分别进行处理
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



if __name__ == '__main__':
    ll = UnorderedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.my_remove(5)
    print(ll.my_search(8))
    print(ll.my_search(1))
    print(ll.my_search(2))
    print(ll.my_search(3))
    print(ll.my_search(4))
