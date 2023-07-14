from typing import Optional
# ======== 4 链表实现栈和队列 ========
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


# 用链表实现ADT Stack与ADT Queue的所有接口
class LinkStack:
    def __init__(self):
        self.head: Optional[Node] = None
        self.length: int = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.length

    def peek(self):
        return self.head.get_data()

    def push(self, item):
        top = Node(item)
        top.set_next(self.head)
        self.head = top
        self.length += 1

    def pop(self):
        top_item = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1
        return top_item

    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


class LinkQueue():
    # 请在此编写你的代码（可删除pass语句）
    pass
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.length

    def enqueue(self, item):
        tail = Node(item)
        # 第一个入队
        if self.head is None:
            self.head = tail
            self.tail = tail
        else:
            self.tail.set_next(tail)
            self.tail = self.tail.get_next()
        self.length += 1

    def dequeue(self):
        top_item = self.head.get_data()
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.get_next()
        self.length -= 1
        return top_item
    # 代码结束


# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False
