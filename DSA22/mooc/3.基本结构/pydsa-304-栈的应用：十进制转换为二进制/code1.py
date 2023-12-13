from DSA22.pythonds.basic.stack import Stack


def divideBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())

    return binString

if __name__ == '__main__':
    print(divideBy2(35))