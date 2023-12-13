# 递归实现任意进制转换
def any_convert(num: int, base: int):
    conv_string = "0123456789ABCDE"
    if num < base:
        return conv_string[num]
    return any_convert(num//base, base) + conv_string[num%base]

print(any_convert(9, 2))