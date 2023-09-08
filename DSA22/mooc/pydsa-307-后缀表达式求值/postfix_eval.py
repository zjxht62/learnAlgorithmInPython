from DSA22.pythonds.basic.stack import Stack
def postfix_eval(postfix_str):
    op_num_stack = Stack()
    postfix_list = postfix_str.split(" ")
    for token in postfix_list:
        if token in "0123456789":
            op_num_stack.push(int(token))
        else:
            op2 = op_num_stack.pop()
            op1 = op_num_stack.pop()
            op_num_stack.push(do_math(token, op1, op2))
    return op_num_stack.pop()

def do_math(op, op1, op2):
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2




if __name__ == '__main__':
    result = postfix_eval("5 5 + 7 2 - *")
    print(result)