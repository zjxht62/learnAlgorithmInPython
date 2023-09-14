# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可
def dpWordEdit(original, target, oplist):
    score = 0
    operations = []

    # 请在此编写你的代码（可删除pass语句）
    original_len = len(original)
    target_len = len(target)
    # 初始化dp表格
    dp = [[0] * (target_len + 1) for i in range(original_len + 1)]
    # 子问题，dp[i][0]
    for i in range(1, original_len + 1):
        dp[i][0] = i * oplist['delete']
    # 子问题,dp[0][j]
    for j in range(1, target_len + 1):
        dp[0][j] = j * oplist['insert']
    for i in range(1, original_len + 1):
        for j in range(1, target_len + 1):
            # 如果original第i-1（因为i从1开始，i-1才能代表对应字符的下标）等于original第i-1，则不用编辑
            if original[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + oplist['copy']
            else:
                dp[i][j] = min(dp[i - 1][j] + oplist['delete'], dp[i][j - 1] + oplist['insert'])

    for l in dp:
        print(l)

    i = original_len
    j = target_len
    while i > 0 or j > 0:
        if original[i - 1] == target[j - 1]:
            operations.insert(0, f'copy {target[j - 1]}')
            i -= 1
            j -= 1
        else:
            if dp[i][j] - dp[i - 1][j] == oplist['delete']:
                operations.insert(0, f'delete {original[i - 1]}')
                i -= 1

            elif dp[i][j] - dp[i][j - 1] == oplist['insert']:
                operations.insert(0, f'insert {target[j - 1]}')
                j -= 1

    score = dp[original_len][target_len]
    # 代码结束
    # for l in dp:
    #     print(l)

    return score, operations


# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = [
    "cane", "sheep", "algorithm", "debug", "difficult", "directory",
    "wonderful"
]
targetWords = [
    "new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"
]
for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)

# 操作所对应的分数可调整
# oplist = {'copy':5, 'delete':20, 'insert':20}
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':5, 'delete':10, 'insert':15}
# 45
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 45
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 125
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 135
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 130
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 145
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 150
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':10, 'delete':25, 'insert':20}
# 90
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 85
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 230
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 230
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 245
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 265
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 280
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
