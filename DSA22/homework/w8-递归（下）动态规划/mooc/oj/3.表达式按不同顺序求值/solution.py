def doMath(op, op1, op2):
    if op == '+':
        return op1+op2
    elif op == '-':
        return op1-op2
    elif op == '*':
        return op1*op2
    else:
        raise RuntimeError("非法操作符")



def findWays(expr):
    def calc(nums: list, ops: list, numstk: list, opstk: list):
        if len(nums) == 0:  # 递归结束，计算值返回
            while len(opstk) > 0:
                op = opstk.pop()
                op2 = numstk.pop()
                op1 = numstk.pop()
                numstk.append(doMath(op, op1, op2))
            results.add(numstk.pop())
            return
        else:
            # 不计算栈中的子表达式，入栈，递归调用
            calc(nums[1:], ops[1:], numstk + [nums[0]], opstk + [ops[0]])
            while len(opstk) > 0:
                # 计算一到多次子表达式，入栈，递归调用
                op = opstk.pop()
                op2 = numstk.pop()
                op1 = numstk.pop()
                numstk.append(doMath(op, op1, op2))
                calc(nums[1:], ops[1:], numstk + [nums[0]], opstk + [ops[0]])
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

    results = set()

    # 头两个数入栈，头一个操作符入栈，递归调用
    calc(nums[2:], ops[1:],[nums[0],nums[1]],[ops[0]])
    # 结果排序、输出
    ret = sorted(list(results))
    return ",".join(map(str, ret))

expr=input()
print(findWays(expr))

