from pythonds.basic.stack import Stack

class VisiableStack(Stack):
    def __repr__(self):
        l = self.size() * 7
        s = "|" + "-"*l + ")\n|"
        for i in self.items:
            s += "| %-5s" % i
        s+= "\n|"+"-"*l +")"
        return s

    __str__ = __repr__



def visiable_postfix_eval(expression: str) -> int:
    # 创建空栈
    s = VisiableStack()
    char_list = expression.split()
    for char in char_list:
        if char in '0123456789':
            print("压入操作数")
            s.push(int(char))
        else:
            print(f"遇到操作符{char}")
            op2 = s.pop()
            op1 = s.pop()
            print(f"弹出第一操作数：{op1}，第二操作数：{op2}")
            temp_sum = do_math(op1, op2, char)
            print(f"将结果{temp_sum}入栈")
            s.push(temp_sum)
        print(s)
    return s.pop()


def do_math(op1: int, op2: int, do_op: str) -> int:
    if do_op == '+':
        print(f'执行运算:{op1} {do_op} {op2}')
        return op1 + op2
    elif do_op == '-':
        print(f'执行运算:{op1} {do_op} {op2}')
        return op1 - op2
    elif do_op == '*':
        print(f'执行运算:{op1} {do_op} {op2}')
        return op1 * op2
    else:
        print(f'执行运算:{op1} {do_op} {op2}')
        return op1 / op2


if __name__ == '__main__':
    # print(visiable_postfix_eval('5 5 + 7 2 - *'))
    # print(visiable_postfix_eval('2 3 * 4 +'))
    # print(visiable_postfix_eval('1 2 + 3 + 4 + 5 +'))
    print(visiable_postfix_eval('1 2 3 4 5 * + * +'))
