# 描述
# 一开始给出了一个由小写字母组成的字符串
# S。我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次
#
# 返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）。
#
# 代码模板(建议复制粘贴使用)：
#
# def func(S):
#     # your code here
#     return output
#
#
# S = eval(input())
# print(func(S))
#
# 输入
# S。S为仅含有小写字母的字符串，长度不超过100000。
# 输出
# 一个与S等长的字符串。
# 样例输入
# "cba"
# 样例输出
# "acb

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        str_result = ""
        for i in range(-1, -self.size() - 1, -1):
            str_result += str(self.items[i])
        return str_result

# 解法1，先将所有字母入队
# 为Queue编写__str__方法
# 循环len-1次，每次将队列头部元素出队，再入队到队尾
# 直到找到最小字符串
def func1(S):
    # your code here
    letter_queue = Queue()
    for c in S:
        letter_queue.enqueue(c)
    min_str = str(letter_queue)
    for i in range(letter_queue.size()):
        letter_queue.enqueue(letter_queue.dequeue())
        if str(letter_queue) < min_str:
            min_str = str(letter_queue)
    return min_str

#解法2
# 也是循环len-1次
# 通过切片操作实现字符串的移动
def func2(s):
    min_str = s
    for i in range(len(s) - 1):
        s = s[1:] + s[0]
        if s < min_str:
            min_str = s
    return min_str


S = eval(input())
print(func1(S))
print(func2(S))
