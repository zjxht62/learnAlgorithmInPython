# 洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
# 小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
# 老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。

from pythonds.basic.stack import Stack

# input_str = '1043257689'
input_str = input()

def dishChecker(orderString):
    s = Stack()
    index = 0
    pop_str = ''
    for order in range(10):
        s.push(str(order))
        # 根据顾客输入的取到的盘子的序号顺序看看能不能从小明洗完的盘子中取到
        while not s.isEmpty() and orderString[index] == s.peek():
            # 如果能拿到，那就拼接出栈字符串
            pop_str = pop_str + s.pop()
            # 看看下面的能不能取到
            index += 1

    if pop_str == orderString:
        return "Yes"
    else:
        return "No"

result = dishChecker(input_str)
print(result)