l = [1, 2, 3, 4, 5]

def print_item(list):
    if len(list) == 1:
        print(list[0])
    else:
        print(list[0])
        print_item(list[1:])

def list_sum(list):
    if len(list) ==1:
        return list[0]
    else:
        return list[0] + list_sum(list[1:])

print_item(l)
print(list_sum(l))


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


def print_linked_list(head:Node):
    if head.get_next() is None:
        print(head.get_data())
    else:
        print(head.get_data())
        print_linked_list(head.get_next())

def remove_node(head:Node, val:int):
    # 最小子问题
    if head is None:
        return None
    # 除了头结点外，剩下的子链表删除指定元素后返回的头节点
    ret = remove_node(head.get_next(), val)

    # 如果头节点不需要删除，那么将其next设置为ret，返回head
    if head.get_data() != val:
        head.set_next(ret)
        return head
    # 否则，head的next设置为空，返回ret
    else:
        head.set_next(None)
        return ret

def remove_node2(head:Node, val:int):
    # 最小子问题
    if head is None:
        return None
    # 如果头节点不用删除，那就设next为子问题返回的头结点，返回head
    if head.get_data() != val:
        head.set_next(remove_node2(head.get_next(), val))
        return head
    # 否则，直接返回子问题的头结点
    else:
        return remove_node2(head.get_next(), val)

def reverse_linked_list(head:Node):
    if head.get_next() is None or head is None:
        return head
    ret = reverse_linked_list(head.get_next())
    head.get_next().set_next(head)
    head.set_next(None)
    return ret








node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node6)
node6.set_next(node7)


# print_linked_list(node1)
# remove_node2(node1, 6)
# print_linked_list(node1)
result = reverse_linked_list(node1)
print_linked_list(result)
# print(node1)

