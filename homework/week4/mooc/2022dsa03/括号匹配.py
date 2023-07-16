# 有效的括号
from pythonds.basic.stack import Stack
brackets_str = input()
# brackets_str = '(([]{}))]'

def is_brackets_pair(left,right):
    if left == '(' and right == ")":
        return True
    elif left == '[' and right == "]":
        return True
    elif left == '{' and right == "}":
        return True
    else:
        return False

def valid_brackets(brackets_str):

    brackets_stack = Stack()
    brackets_str_list = list(brackets_str)
    for b in brackets_str_list:
        if b in "([{":
            brackets_stack.push(b)
        elif b in ")]}":
            if not brackets_stack.isEmpty():
                last_bracket = brackets_stack.pop()
                if is_brackets_pair(last_bracket, b):
                    continue
                else:
                    return False
            else:
                return False
    if not brackets_stack.isEmpty():
        return False
    else:
        return True


result = valid_brackets(brackets_str)
print(result)