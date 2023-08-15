class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# 用来存储所有路径的list
path_list = []
# 用来再递归过程中计算路径的list
path = []
def dfs(tree_node: Node):
    if tree_node is None:
        return
    # 在”递“的过程中，将访问的节点放到path中
    path.append(tree_node.value)
    # 如果碰到叶子节点，那么当前的path就是一条路径，就将当前path拷贝到path_list
    if tree_node.left is None and tree_node.right is None:
        path_list.append(list(path))

    # 递归访问左右子树
    dfs(tree_node.left)
    dfs(tree_node.right)
    # 在“归“的过程中，删除访问过的节点
    path.pop()

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(4)
    n3 = Node(8)
    n4 = Node(11)
    n5 = Node(13)
    n6 = Node(4)
    n7 = Node(7)
    n8 = Node(2)
    n9 = Node(5)
    n10 = Node(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n4.left = n7
    n4.right = n8
    n3.left = n5
    n3.right = n6
    n6.left = n9
    n6.right = n10

    dfs(n1)
    print(path_list)
