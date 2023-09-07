# 宝物的重量和价值
tr = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
# 大盗最大承重
max_w = 20

# 初始化记忆化表格m
# key是(宝物组合， 最大重量）,value是最大价值
m = {}


def thief(tr, w):
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0  # tuple是key的要求
        return 0
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                # 逐个从集合中去掉某个宝物，递归调用
                # 选出所有价值中的最大值
                v = thief(tr - {t}, w - t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        return vmax

# 输出结果
print(thief(tr, max_w))
