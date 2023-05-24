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


if __name__ == '__main__':
    print(myParChecker("(()()(())()"))
