# 斐波那契数列
# 自底向上推导
class Fibonacci5:
    # 动态规划的四个步骤
    def __init__(self):
        # 1.定义状态数组，定义每个状态值表示什么：这里表示的是第i个斐波那契数
        # 2. 状态初始化
        self.dp = [0, 1]

    def fib(self, n):
        # 3.状态转移
        for i in range(2, n+1):
            # 从第三个元素开始计算斐波那契数的结果
            self.dp.append(self.dp[i - 1] + self.dp[i - 2])
        # 4.返回最终需要的状态值
        return self.dp[n]



if __name__ == '__main__':
    fib = Fibonacci5()
    print(fib.fib(20))
