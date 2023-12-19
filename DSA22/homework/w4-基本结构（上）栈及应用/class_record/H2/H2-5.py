# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList():
    # 请在此编写你的代码（可删除pass语句）
    def __init__(self, it=None):
        self.head = None
        self.tail = None
        self.length = 0
        if it is not None:
            for i in it:
                self.append(i)

    def get_tail(self):
        return self.tail

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node_add = Node(item)
        # 第一个加入列表
        if self.head is None:
            self.head = self.tail = node_add
        else:
            # 原来head的前一个设置为node_add，node_add的下一个设置为之前的head
            node_add.set_next(self.head)
            self.head.set_prev(node_add)
            # 将head指向新添加的node_add
            self.head = node_add
        self.length += 1

    def append(self, item):
        node_append = Node(item)
        # 第一个追加到列表
        if self.head is None:
            self.head = self.tail = node_append
        else:
            node_append.set_prev(self.tail)
            self.tail.set_next(node_append)
            self.tail = node_append
        self.length += 1

    def search(self, item):
        return self.index(item) is not None

    def size(self):
        return self.length

    __len__ = size

    def delete(self, current):
        if self.head == current:
            self.head = current.get_next()
        if self.tail == current:
            self.tail = current.get_prev()
        if current.get_prev() is not None:
            current.get_prev().set_next(current.get_next())
        if current.get_next() is not None:
            current.get_next().set_prev(current.get_prev())
        self.length -= 1

    def remove(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                self.delete(current)
                break
            current = current.get_next()

    def index(self, item):
        current, index = self.head, 0
        while current is not None:
            if current.get_data() == item:
                return index
            else:
                current = current.get_next()
                index += 1
        return None

    def pop(self, n: int = None):
        if n is None:
            n = self.length - 1
        current, i = self.head, 0
        while i < n:
            current = current.get_next()
            i += 1
        dat = current.get_data()
        self.delete(current)
        return dat

    def insert(self, idx, item):  # 加为idx个
        current, n = self.head, 0
        while n < idx:
            current = current.get_next()
            n += 1
        if current is None:
            if self.head is None:
                # 这是第一个插入列表的
                self.add(item)
            else:
                self.append(item)
        else:
            node_insert = Node(item)
            node_insert.set_next(current)
            node_insert.set_prev(current.get_prev())
            if node_insert.get_prev() is not None:
                node_insert.get_prev().set_next(node_insert)
            current.set_prev(node_insert)
        self.length += 1

    def __str__(self):
        tlist = []
        current = self.head
        while current is not None:
            tlist.append(current.get_data())
            current = current.get_next()
        return str(tlist)

    __repr__ = __str__

    def __getitem__(self, key):
        if isinstance(key, int):
            current, index = self.head, 0
            # 使用while循环和for都行，感觉for更好理解
            while index < key:
                current: Node = current.get_next()
                index += 1
            # for _ in range(key):
            #     current = current.get_next()
            #     index += 1
            if current is not None:
                return current.get_data()
            else:
                raise StopIteration
        elif isinstance(key, slice):
            start = 0 if key.start is None else key.start
            stop = self.length if key.stop is None else key.stop
            step = 1 if key.step is None else key.step
            current, i = self.head, 0
            # 定位到start
            while i < start:
                current = current.get_next()
                i += 1
            dcopy = DoublyLinkedList()
            while i < stop:
                dcopy.append(current.get_data())
                s = step
                while current is not None and s > 0:
                    current = current.get_next()
                    s -= 1
                i += step
            return dcopy

    def __eq__(self, other):
        if other is None or not isinstance(other, DoublyLinkedList):
            return False
        if len(self) != len(other):
            return False
        for s,o in zip(self, other):
            if s!=o:
                return False
        else:
            return True
    # 代码结束


# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
print(mylist)
print(mylist[4])
mylist.add(3)
mylist.remove(6)
print(mylist.get_tail().get_prev().get_data())  # 16
print(mylist.is_empty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[3:8:2])  # ['10', 10, 14]
