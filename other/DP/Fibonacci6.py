# 斐波那契数列
# 优化空间复杂度,只存储前两个元素
class Fibonacci6:
    def __init__(self):
        self.prev = 0
        self.current = 1

    def fib(self, n):
        if n == 0: return self.prev
        if n == 1: return self.current

        for i in range(2, n + 1):
            # 从第三个元素开始计算斐波那契数的结果
            sum = self.current + self.prev
            self.prev = self.current
            self.current = sum
        return self.current


if __name__ == '__main__':
    fib = Fibonacci6()
    print(fib.fib(6))
