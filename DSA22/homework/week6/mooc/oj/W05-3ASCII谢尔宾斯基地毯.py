# 谢尔宾斯基地毯一种正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。
#
# 现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。
#
# 注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应
#
# 输入
# 输入为两行，分别为地毯大小正整数N与组成元素字符串c
#
# 输入数据保证N为3的正整数幂
# 输出
# 由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯
# 样例输入
# 9
# []
# 样例输出
# [][][][][][][][][]
# []  [][]  [][]  []
# [][][][][][][][][]
# [][][]      [][][]
# []  []      []  []
# [][][]      [][][]
# [][][][][][][][][]
# []  [][]  [][]  []
# [][][][][][][][][]

n = int(input())  # 阶数
ch = input()  # 构成字符
blank = " " * len(ch)  # 构成空白
pic = [[ch for col in range(n)] for row in range(n)]  # 先初始化画板，也就是完整的由符号组成的n阶图形


def spski(n, top, left):  # n阶， 左上角的行列数
    if n == 1:
        return
    # 分为三行三列，挖掉中心，其余递归n//3
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:  # 挖空
                for r1 in range(n // 3):
                    for c1 in range(n // 3):
                        pic[top + n // 3 + r1][left + n // 3 + c1] = blank
            else:  # 递归n//3
                spski(n // 3, top + row * n // 3, left + col * n // 3)


spski(n, 0, 0)
for r in range(n):
    print("".join(pic[r]))
