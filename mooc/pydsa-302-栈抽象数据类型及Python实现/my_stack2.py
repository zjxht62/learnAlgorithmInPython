# 使用List的左端作为栈顶
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

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
