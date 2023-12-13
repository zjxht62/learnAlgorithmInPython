from timeit import Timer
# 4种生成前n个整数列表的方法
# 循环连接列表
def test1():
    l = []
    for i in range(10000):
        l = l + [i]


# append
def test2():
    l = []
    for i in range(10000):
        l.append(i)


# 列表推导式
def test3():
    l = [i for i in range(10000)]

# range函数转成列表
def test4():
    l = list(range(10000))

if __name__ == '__main__':
    t1 = Timer("test1()", "from __main__ import test1")
    print(f"concat {t1.timeit(number=100)} seconds\n")

    t2 = Timer("test2()", "from __main__ import test2")
    print(f"concat {t2.timeit(number=100)} seconds\n")

    t3 = Timer("test3()", "from __main__ import test3")
    print(f"concat {t3.timeit(number=100)} seconds\n")

    t4 = Timer("test4()", "from __main__ import test4")
    print(f"concat {t4.timeit(number=100)} seconds\n")