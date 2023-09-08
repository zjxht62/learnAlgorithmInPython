# 动态规划背包问题
# 初始化物品信息
treasures = [None, {'n': 1, 'w': 2, 'v': 3}, {'n': 2, 'w': 3, 'v': 4}, {'n': 3, 'w': 4, 'v': 8},
             {'n': 4, 'w': 5, 'v': 8}, {'n': 5, 'w': 9, 'v': 10}]
# 最大背包容量
max_size = 20

# 初始化表
m = [[0] * (max_size + 1) for n in range(len(treasures))]

for i in range(1, len(treasures)):
    for w in range(1, max_size + 1):
        # 如果装不下第i个物品
        if treasures[i]['w'] > w:
            # 不装了
            m[i][w] = m[i - 1][w]
        else:
            # 装和不装第i个宝物，两种情况的最大价值
            m[i][w] = max(m[i - 1][w], treasures[i]['v'] + m[i - 1][w - treasures[i]['w']])

# 输出结果
print(m[len(treasures) - 1][max_size])