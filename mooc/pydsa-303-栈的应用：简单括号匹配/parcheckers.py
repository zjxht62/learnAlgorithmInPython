from pythonds.basic.stack import Stack


def myParChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        # 可以定义一个变量来存储当前字符，节省代码
        if symbolString[i] == "(":
            s.push(symbolString[i])
            # 可以提取到外面
            i += 1
            continue
        # 此处老师直接用的else，因为假设输入只有左右括号
        if symbolString[i] == ")":
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                i += 1
    if not s.isEmpty():
        balanced = False

    return balanced


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# 通用括号匹配算法
def parCheckerPlus(symbolString):
    s = Stack()
    balanced =  True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        # 碰到各种左括号依旧入栈
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                # 碰到各种右括号的时候需要判断栈顶的左括号是否跟右括号是同一种类
                par = s.pop()
                if not isParMatch(par, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def isParMatch(par1, par2):
    left_pars ="([{"
    right_pars = ")]}"
    return left_pars.index(par1) == right_pars.index(par2)

if __name__ == '__main__':
    print(myParChecker("(()()(())())"))
    print(parCheckerPlus("{()()([])()}}"))
