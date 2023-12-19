def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    # 用于在结束循环后将最后一个num加入到nums中
    else:
        nums.append(num)

    # code here

# expr=input()
# print(findWays(expr))

if __name__ == '__main__':
    findWays("2*3-4*5")