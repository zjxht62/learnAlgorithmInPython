import timeit
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

# x = list(range(2000000))
# print(popzero.timeit(number=1000))
# print(popend.timeit(number=1000))

# 通过改变列表长度来测试两个操作的增长趋势
print("pop(0)  pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pe = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print(f'{pz:15.5f}, {pe:15.5f}')
