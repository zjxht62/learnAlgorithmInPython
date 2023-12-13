class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return self.items.__str__()


if __name__ == '__main__':
    q = Queue()
    print(q)
    print(q.isEmpty())
    q.enqueue(4)
    print(q)
    q.enqueue('dog')
    print(q)
    q.enqueue(True)
    print(q)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(8.4)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    print(q.size())



