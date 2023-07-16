# uuid_share#  4e746bfe-8d2d-42ca-af59-cb654a86adee  #
# PKUDSA课程上机作业
# 【H2】栈与队列编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的*函数体内*编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
#

# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def get_op_priority(op):
    prority_dict = {}
    prority_dict['^'] = 4
    prority_dict['*'] = 3
    prority_dict['/'] = 3
    prority_dict['+'] = 2
    prority_dict['-'] = 2
    prority_dict['('] = 1
    return prority_dict[op]


def do_math(op: str, op1: float, op2: float) -> float:
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '^':
        return op1 ** op2


def calculate(s) -> float:
    # 请在此编写你的代码（可删除pass语句）
    # 创建两个栈，分别存储操作符和操作数
    op_stack = Stack()
    op_num_stack = Stack()

    infix_list = s.split(" ")
    for token in infix_list:
        # 如果字符串是数字，就push到操作数栈中
        if token.isdigit():
            op_num_stack.push(float(token))
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            op_top = op_stack.pop()
            while op_top != '(':
                # 将操作符弹出栈的时候，从操作数栈中也弹出两个操作数，计算后再压栈
                op2 = op_num_stack.pop()
                op1 = op_num_stack.pop()
                op_num_stack.push(do_math(op_top, op1, op2))
                op_top = op_stack.pop()
        else:
            while not op_stack.isEmpty() and get_op_priority(op_stack.peek()) >= get_op_priority(token):
                # 若栈顶元素优先级高， 则需要先弹栈，同时弹出两个操作数来计算
                op2 = op_num_stack.pop()
                op1 = op_num_stack.pop()
                op_num_stack.push(do_math(op_stack.pop(), op1, op2))
            op_stack.push(token)
    while not op_stack.isEmpty():
        # 弹出剩余操作符，弹出一个，计算一下
        op2 = op_num_stack.pop()
        op1 = op_num_stack.pop()
        op_num_stack.push(do_math(op_stack.pop(), op1, op2))
    return op_num_stack.pop()
    # 代码结束


# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))
