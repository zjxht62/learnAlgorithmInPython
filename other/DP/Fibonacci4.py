# 斐波那契数列
# 自底向上推导
class Fibonacci4:
    def __init__(self):
        # 初始化前两个元素
        self.fibs = [0, 1]

    def fib(self, n):
        for i in range(2, n+1):
            # 从第三个元素开始计算斐波那契数的结果
            self.fibs.append(self.fibs[i-1]+self.fibs[i-2])
        # 返回最终结果
        return self.fibs[n]



if __name__ == '__main__':
    fib = Fibonacci4()
    print(fib.fib(20))
