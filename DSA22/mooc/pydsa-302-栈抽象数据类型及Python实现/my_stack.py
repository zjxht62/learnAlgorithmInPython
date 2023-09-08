class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # return len(self.items) == 0  # 此处是我自己的实现，相比于老师的来说显得更加复杂
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.isEmpty())
    my_stack.push(4)
    my_stack.push('dog')
    print(my_stack.peek())
    my_stack.push(True)
    print(my_stack.size())
    print(my_stack.isEmpty())
    my_stack.push(8.4)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.size())
