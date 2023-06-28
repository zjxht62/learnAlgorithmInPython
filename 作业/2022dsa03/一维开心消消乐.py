

# 开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。
# 如果字符全部被消完，则输出不带引号的“None”

#输入样例1：beepooxxxyz
#输出样例1：bpxyz

#输入样例3：（这里bb被消了以后，第二个a挨上来了，所以两个a也相邻，同样消去）
#abbacddccc00

#输出样例3：None
from pythonds.basic.stack import Stack

test_str = input()
# test_str = 'beepooxxxyz'
def xiaoxiaole(str):
    # 创建栈保存字符
    str_stack = Stack()
    str_list = list(str)
    for s in str_list:
        # 如果栈不为空，比对栈顶元素与当前元素
        if not str_stack.isEmpty():
            top_str = str_stack.peek()
            # 如果相等，则可以抵消，将栈顶元素弹栈，当前元素也不处理（不入栈）
            if top_str == s:
                str_stack.pop()
            else:
                # 不相等则将当前元素入栈
                str_stack.push(s)
        # 栈为空，直接将当前元素入栈
        else:
            str_stack.push(s)

    # 使用另一个栈反转元素顺序
    stack_2 = Stack()
    while not str_stack.isEmpty():
        stack_2.push(str_stack.pop())

    result_list = []

    while not stack_2.isEmpty():
        result_list.append(stack_2.pop())

    if not len(result_list) == 0:
        return "".join(result_list)
    else:
        return "None"


result =xiaoxiaole(test_str)
print(result)
