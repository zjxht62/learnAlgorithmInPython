# 如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过1.8*10^19步才能解开。
#
# 透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下，找出完成迁移的最小步骤数。
#
# 输入
# 一个非负整数M，M代表盘数，M<=1000。
# 输出
# 一个非负整数，表示完成迁移的最小步骤数。
# 样例输入
# 3
# 样例输出
# 5
# 在计算过程中使用缓存，将中间结果保存起来
n = int(input())
# n = 4
h4cache = [None for x in range(n + 1)]


def hanoi4(n: int):
    if h4cache[n]:
        return h4cache[n]
    if n == 0:
        h4cache[n] = 0
    elif n == 1:
        h4cache[n] = 1
    elif n == 2:
        h4cache[n] = 3
    else:
        H = []
        for x in range(1, n):
            # 缩小规模
            # 对于取定的x的值（小于n）
            # 第一步的步数就是hanoi4(x)
            # 第二步的步数就是hanoi3(n-x)=2**(n-x)-1
            # 第三步还是hanoi4(x)
            H.append(2 * hanoi4(x) + 2 ** (n - x) - 1)
        h4cache[n] = min(H)
    return h4cache[n]


print(hanoi4(n))
