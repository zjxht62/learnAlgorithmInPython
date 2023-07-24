class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class FindMaxDepth:
    # 递归计算二叉树深度
    def __init__(self):
        self.res = 0

    def find_max_depth_with_pre_order(self, node: Node, depth: int):
        # 使用前序遍历计算二叉树深度，传入当前节点的depth，存到栈帧
        if node is None:
            # 如果节点是空，直接return
            return
        # 将当前节点的深度和res比较取较大者
        self.res = max(self.res, depth)
        # 遍历左右子树
        self.find_max_depth_with_pre_order(node.left, depth + 1)
        self.find_max_depth_with_pre_order(node.right, depth + 1)

    def find_max_depth_with_post_order(self, node: Node):
        # 使用后序遍历计算二叉树深度
        if node is None:
            # 如果节点为空，则其深度为0
            return 0
        # 获取左右叶子节点的深度
        left_max_depth = self.find_max_depth_with_post_order(node.left)
        right_max_depth = self.find_max_depth_with_post_order(node.right)
        # 根节点深度为左右子节点较大者再+1
        return max(left_max_depth, right_max_depth)+1


def pre_order(root: Node):
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: Node):
    if root is None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root: Node):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)


if __name__ == '__main__':
    node_0 = Node(10)
    node_1 = Node(8)
    node_2 = Node(9)
    node_3 = Node(23)
    node_4 = Node(11)
    node_5 = Node(7)

    node_0.left = node_1
    node_0.right = node_2

    node_1.left = node_3
    node_1.right = node_4

    node_2.right = node_5

    # pre_order(node_0)
    # in_order(node_0)
    # post_order(node_0)

    find_max_depth = FindMaxDepth()
    # find_max_depth.find_max_depth_with_pre_order(node_0, 1)
    # print(find_max_depth.res)

    print(find_max_depth.find_max_depth_with_post_order(node_0))