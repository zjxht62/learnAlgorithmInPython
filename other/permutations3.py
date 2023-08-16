# 全排列问题
# 排除非全排列的组合
class Permutation:
    # O(n! * n^2)
    def __init__(self):
        # 用于存储所有的路径结果
        self.all_path: list = []
        # 用于在遍历过程中存储路径
        self.path: list = []


    def permute(self, nums: list) -> list:
        # 将根节点index设置为-1，后续不做处理
        self.dfs(nums)
        return self.all_path

    def dfs(self, nums: list):
        # 当path长度等于nums时 结束
        if len(self.path) == len(nums):
            self.all_path.append(list(self.path))
            return


        # 遍历其他索引
        for i in range(len(nums)):
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.dfs(nums)
            self.path.pop()



if __name__ == '__main__':
    p = Permutation()
    print(p.permute([1, 2, 3, 4, 5, 6, 7, 8, 9]))