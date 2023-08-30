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

def sierpinski(degree, s):
    if degree >= 3:
        empty = degree//3
        for i in range(degree):
            if i in range(empty, empty+empty-1):
                print('haha')
                # print(s*empty + ' '*empty + s*empty)
                print(s*empty + ' '*empty + s*empty)
            else:
                print(s*degree)
        # sierpinski(degree//3, s)



if __name__ == '__main__':
    # sierpinski(3,'a')
    print(1 in range(1,2))