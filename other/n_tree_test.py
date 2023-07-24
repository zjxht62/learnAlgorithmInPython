class Node:
    # 多叉树的定义
    def __init__(self, val):
        self.value = val
        self.children = []


def pre_order(node:Node):
    if node is None:
        return
    print(node.value)
    for n in node.children:
        pre_order(n)

def post_order(node:Node):
    if node is None:
        return
    for n in node.children:
        post_order(n)
    print(node.value)


if __name__ == '__main__':
    node_1 = Node(4)
    node_2 = Node(2)
    node_3 = Node(7)
    node_4 = Node(7)
    node_5 = Node(1)
    node_6 = Node(9)
    node_7 = Node(3)
    node_8 = Node(6)
    node_9 = Node(9)
    node_10 = Node(6)
    node_11 = Node(9)
    node_12 = Node(9)

    node_1.children = [node_2, node_3, node_4]
    node_2.children = [node_5, node_6,node_7]
    node_3.children = [node_8, node_9]
    node_4.children = [node_10, node_11, node_12]

    # pre_order(node_1)
    post_order(node_1)

