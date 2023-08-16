# 全排列问题
class Permutation:
    def __init__(self):
        # 用于存储所有的路径结果
        self.all_path: list = []
        # 用于在遍历过程中存储路径
        self.path: list = []


    def permute(self, nums: list) -> list:
        # 将根节点index设置为-1，后续不做处理
        self.dfs(nums, -1)
        return self.all_path

    def dfs(self, nums: list, index:int):
        # 当path长度等于nums时 结束
        if len(self.path) == len(nums):
            return
        # 不处理根节点
        if index != -1:
            self.path.append(nums[index])
        # path长度等于nums时，将其加入到all_path
        if len(self.path) == len(nums):
            self.all_path.append(list(self.path))
        # 遍历其他索引
        for i in range(len(nums)):
            self.dfs(nums, i)

        # 在回溯过程中，将当前节点从path中删除
        if index != -1:
            self.path.pop()


if __name__ == '__main__':
    p = Permutation()
    print(p.permute([1, 2, 3, 4]))