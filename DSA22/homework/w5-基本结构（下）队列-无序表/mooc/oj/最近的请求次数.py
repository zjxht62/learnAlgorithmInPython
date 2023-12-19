# 描述
# 计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k - 10000
# 和k（两端均含）之间。
#
# 代码模板(建议复制粘贴使用)：
#
# def func(mylist):
#     # your code here
#     return output
#
#
# mylist = eval(input())
# print(func(mylist))
#
# 输入
# 一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。
# 输出
# 一个与mylist等长的列表。
# 样例输入
# [0, 10, 100, 1000, 10000, 20000, 100000]
# 样例输出
# [1, 2, 3, 4, 5, 2, 1]

# 解法1：
# 从一个元素开始逐渐截取列表，之后用列表推导式将符合的元素添加到新列表中，再计算长度
def func1(mylist):
    result = []
    for i in range(len(mylist)):
        happened_list = [j for j in mylist[:i] if mylist[i]-j <= 10000]
        result.append(len(happened_list)+1)
    return result
    # your code here
    # return output

# 解法1的变种
def func2(mylist):
    result = []
    for i in range(len(mylist)):
        count = 1
        for j in range(i):
            if mylist[j] <= mylist[i] and mylist[i]-mylist[j] <= 10000:
                count +=1
        result.append(count)
    return result


# 解法三 暂时没懂
def func3(mylist):
    output = []
    new_list = [] # 用列表来模拟队列
    for i in range(len(mylist)):
        new_list.append(mylist[i])
        while new_list[-1] - new_list[0] > 10000:
            new_list.pop(0)
        count = 0
        for j in range(i+1, len(mylist)):
            if mylist[j] == mylist[i]:
                count += 1
            else:
                break
        output.append(len(new_list)+count)
    return output
#
# mylist = eval(input())
# print(type(mylist))


mylist = [0, 10, 100, 1000, 10000, 20000, 100000]
print(func1(mylist))
print(func2(mylist))
print(func3(mylist))

mylist = [0, 10, 100, 1000, 10000, 20000, 100000, 100050, 300050]
print(func1(mylist))
print(func2(mylist))
print(func3(mylist))
