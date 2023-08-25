# 斐波那契数列
# 消除重复子问题
# 使用记忆化搜索，在计算过程中将重复子问题的结果保存起来
# 使用列表保存结果
class Fibonacci3:
    def __init__(self):
        self.memo = []

    def fib(self, n):
        # 将列表元素初始化为-1，长度为n+1
        self.memo = [-1] * (n+1)
        return self.dfs(n)
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def dfs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # 先从字典中检索子问题的解
        # 如果已经计算，则直接返回即可
        if self.memo[n] != -1:
            return self.memo[n]


        left_fib = self.dfs(n - 1)
        right_fib = self.dfs(n - 2)
        # 将计算好的结果放入到字典中，
        self.memo[n] = left_fib + right_fib
        return left_fib + right_fib


if __name__ == '__main__':
    fib = Fibonacci3()
    print(fib.fib(6))
