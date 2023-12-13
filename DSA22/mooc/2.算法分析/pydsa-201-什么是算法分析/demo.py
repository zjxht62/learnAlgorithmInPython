import time
def sumofN(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum += i
    return the_sum

def sumOfN2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum += i
    end = time.time()
    return the_sum, end-start

def sumOfN3(n):
    start = time.time()
    the_sum = (n*(n+1))/2
    end = time.time()
    return the_sum, end-start

for i in range(5):
    # print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))
    print("Sum is %d required %10.7f seconds" % sumOfN3(1000000))