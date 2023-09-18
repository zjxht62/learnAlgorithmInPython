
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
    table = [[0] * (maxWeight + 1) for i in range(len(treasureList))]
    for i in range(len(treasureList)):
        for w in range(maxWeight + 1):
            if treasureList[i]['w'] > w:
                table[i][w] = table[i - 1][w]
            else:
                # 放入当前宝物后的价值
                v_put = treasureList[i]['v'] + table[i - 1][w - treasureList[i]['w']]
                # 不放入当前宝物时的价值
                v_not_put = table[i - 1][w]
                table[i][w] = max(v_put, v_not_put)
                # if v_put >= v_not_put:
                #     choosenList.append(treasureList[i])
                #     table[i][w] = v_put
                # else:
                #     table[i][w] = v_not_put
    # for line in table:
    #     print(line)
    maxValue = table[len(treasureList) - 1][maxWeight]

    current_max_value = maxValue
    current_max_weight = maxWeight
    for i in range(len(treasureList) - 1, -1, -1):
        # print(table[i])
        if i > 0:
            if current_max_value != table[i - 1][current_max_weight]:
                choosenList.append(treasureList[i])
                current_max_value = current_max_value - treasureList[i]['v']
                current_max_weight = current_max_weight - treasureList[i]['w']
        elif i == 0:
            if treasureList[i]['w'] <= current_max_weight:
                choosenList.append(treasureList[i])

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

