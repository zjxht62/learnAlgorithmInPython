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
def convert(num, base):
    strs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num < base:
        return strs[num]
    return convert(num//base, base) + strs[num%base]
def re2oct(num, base):
    strs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    oct_result = 0
    # 每一位对应要乘的进制数
    cal = len(num) -1
    for n in num:
        count = strs.index(n)
        oct_result += count * base**cal
        cal-=1
    return oct_result

mn:str = input()
m = int(mn.split()[0])
n = int(mn.split()[1])

number = input()


print(convert(re2oct(number, m),n))
