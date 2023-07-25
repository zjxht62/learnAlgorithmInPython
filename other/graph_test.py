class Node:
    # 图顶点的定义
    def __init__(self, val):
        self.value = val
        self.neighbors = []


class GraphTest:
    def __init__(self):
        # 维护一个已经访问过的节点的列表
        self.visited_node = []

    # 图的深度优先遍历
    def dfs(self, node: Node):
        # 已经访问过的节点不再访问
        if node is None or node in self.visited_node:
            return
        print(node.value)
        self.visited_node.append(node)
        for n in node.neighbors:
            self.dfs(n)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_5, node_6]
    node_3.neighbors = [node_1]
    node_6.neighbors = [node_3]

    gt = GraphTest()

    gt.dfs(node_1)
