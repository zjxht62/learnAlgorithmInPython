from pythonds.basic.stack import Stack

OP_LATTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def get_op_priority(op):
    prority_dict = {}
    prority_dict['*'] = 3
    prority_dict['/'] = 3
    prority_dict['+'] = 2
    prority_dict['-'] = 2
    prority_dict['('] = 1

    return prority_dict[op]

def infix2postfix(input_str):
    opstack = Stack()

    infix_list = input_str.split(" ")
    result_list = []
    for token in infix_list:
        if token in OP_LATTERS:
            result_list.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            op_top = opstack.pop()
            while op_top != "(":
                result_list.append(op_top)
                op_top = opstack.pop()
        else:
            while not opstack.isEmpty() and get_op_priority(opstack.peek()) >= get_op_priority(token):
                result_list.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        result_list.append(opstack.pop())

    return " ".join(result_list)





    pass

if __name__ == '__main__':
    print(infix2postfix("A + B * C"))
    print(infix2postfix("( A + B ) * C"))
    print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infix2postfix("( 2 + 3 ) * 6 + 4 / 2"))
