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
            self.all_path.append(list(self.path))
            return


        # 遍历其他索引
        for i in range(len(nums)):
            self.path.append(nums[i])
            self.dfs(nums, i)
            self.path.pop()



if __name__ == '__main__':
    p = Permutation()
    print(p.permute([1, 2, 3, 4]))