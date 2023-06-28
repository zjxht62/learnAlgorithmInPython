# 计算阶乘
n = int(input())

def calculate_factorial(num):
    result = 1
    # for i in range(2,num+1):
    # 使用-1步长，实现从num到1的迭代
    for i in range(num, 0, -1):
        result = result*i
    return result

print(calculate_factorial(n))