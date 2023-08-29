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
