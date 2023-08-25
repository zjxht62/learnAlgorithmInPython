# 斐波那契数列
# 消除重复子问题
# 使用记忆化搜索，在计算过程中将重复子问题的结果保存起来
class Fibonacci2:
    def __init__(self):
        self.temp_dict = {}

    def fib(self, n):
        return self.dfs(n)

    # 时间复杂度：O(n)
    def dfs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # 先从字典中检索子问题的解
        # 如果已经计算，则直接返回即可
        if n in self.temp_dict.keys():
            return self.temp_dict[n]


        left_fib = self.dfs(n - 1)
        right_fib = self.dfs(n - 2)
        # 将计算好的结果放入到字典中，
        self.temp_dict[n] = left_fib + right_fib
        return left_fib + right_fib


if __name__ == '__main__':
    fib = Fibonacci2()
    print(fib.fib(6))
