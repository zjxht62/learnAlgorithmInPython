# =========== 1 博物馆大盗问题 ===========
# 给定一个宝物列表treasureList = [{'w': 2,'v': 3}, {'w': 3,'v': 4}, ...]
# 注意：每样宝物只有1个。
# 这样treasureList[0]['w']就是第一件宝物的重量，等等
# 给定包裹最多承重maxWeight > 0
# 实现一个函数，根据以上条件得到最高总价值以及对应的宝物
# 参数：宝物列表treasureList，背包最大承重maxWeight
# 返回值：最大总价值maxValue，选取的宝物列表choosenList(格式同treasureList)
def dpMuseumThief(treasureList, maxWeight):
    maxValue = 0
    choosenList = []

    # 请在此编写你的代码（可删除pass语句）
    tr = [None] + treasureList  # 让宝物编码从1开始
    # 初始化二维表格m[(i,w)]，均为0，None
    # 表示前i个宝物中，最大重量w的组合，所得到的最大价值
    # 以及加了哪个宝物得到的这个最大价值
    # 当i什么都不取，或w上限为0，价值均为0
    m = {(i, w): [0, None] for i in range(len(tr)) for w in range(maxWeight + 1)}
    for i in range(1, len(tr)):
        for w in range(1, maxWeight + 1):
            if tr[i]['w'] > w:
                m[i, w][0] = m[i - 1, w][0]
            else:
                # 放入当前宝物后的价值
                v_put = tr[i]['v'] + m[i - 1, w - tr[i]['w']][0]
                # 不放入当前宝物时的价值
                v_not_put = m[i - 1, w][0]
                # table[i][w] = max(v_put, v_not_put)
                if v_put >= v_not_put:
                    m[i, w][0] = v_put
                    m[i, w][1] = tr[i]
                else:
                    m[i, w][0] = v_not_put

    maxValue = m[i, w][0]
    while w > 0:
        if m[i, w][1] is not None:  # 如果装了宝物就输出
            choosenList.insert(0, m[i, w][1])
            # 重量减去当前宝物的重量
            w = w - m[i, w][1]['w']
        # 考虑上一个宝贝
        i = i - 1

    # current_max_value = maxValue
    # current_max_weight = maxWeight
    # for i in range(len(treasureList) - 1, -1, -1):
    #     # print(table[i])
    #     if i > 0:
    #         if current_max_value != table[i - 1][current_max_weight]:
    #             choosenList.append(treasureList[i])
    #             current_max_value = current_max_value - treasureList[i]['v']
    #             current_max_weight = current_max_weight - treasureList[i]['w']
    #     elif i == 0:
    #         if treasureList[i]['w'] <= current_max_weight:
    #             choosenList.append(treasureList[i])

    # 代码结束

    return maxValue, choosenList


# 检验
print("=========== 1 博物馆大盗问题 ============")
treasureList = [[{'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]]
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7},
     {'w': 5, 'v': 7},
     {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12},
     {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 16}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6},
     {'w': 4, 'v': 7},
     {'w': 5, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 11}, {'w': 7, 'v': 12},
     {'w': 8, 'v': 13},
     {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18},
     {'w': 11, 'v': 18}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5},
     {'w': 4, 'v': 6},
     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {'w': 7, 'v': 10}, {'w': 7, 'v': 11},
     {'w': 8, 'v': 12},
     {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17},
     {'w': 11, 'v': 18},
     {'w': 12, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21},
     {'w': 14, 'v': 22}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5},
     {'w': 4, 'v': 6},
     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {'w': 7, 'v': 9}, {'w': 7, 'v': 10},
     {'w': 8, 'v': 11},
     {'w': 8, 'v': 12}, {'w': 9, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17},
     {'w': 11, 'v': 18},
     {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21},
     {'w': 14, 'v': 22},
     {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27},
     {'w': 18, 'v': 28}])

maxWeightList = [20, 50, 80, 100, 150]
for i in range(len(treasureList)):
    maxValue, choosenList = dpMuseumThief(treasureList[i], maxWeightList[i])
    print(maxValue)
    print(choosenList)

# 可有多种取法，以下只给出一种符合条件的宝物列表
# 29
# [{'w':2, 'v':3}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]
# 83
# [{'w': 1, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12}, {'w': 8, 'v': 13}, {'w': 9, 'v': 16}]
# 139
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18}]
# 164
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 8, 'v': 13}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 21}, {'w': 14, 'v': 22}]
# 246
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 9, 'v': 15}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27}]
