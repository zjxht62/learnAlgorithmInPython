# 斐波那契数列
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))
#

class Fibonacci1:
    def fib(self, n):
        return self.dfs(n)

    # 时间复杂度：O(2^n)
    def dfs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.dfs(n - 1) + self.dfs(n - 2)

if __name__ == '__main__':
    fib = Fibonacci1()
    print(fib.fib(6))