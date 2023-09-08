# 题目内容：
#
# 给定一个M进制的数，请将其转换为N进制并输出
#
# 输入
# 两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
#
# 第二行为待转换的M进制数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证数据的每一位不超过M
# 输出
# 一行字符串，表示转换后的N进制数
# 样例输入
# 8 16
# 471
# 样例输出
# 139

m, n = [int(x) for x in input().split()]
k = input()
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def nbase2int(k, n):  # n进制转换为整数，k是字符串
    if len(k) == 1:
        return chars.index(k)
    else:
        return nbase2int(k[:-1], n) * n + chars.index(k[-1])


def int2base(k, n): # 整数转为n进制，k是整数
    if k < n:
        return chars[k]
    else:
        return int2base(k // n, n) + chars[k % n]


print(int2base(nbase2int(k, m), n))
