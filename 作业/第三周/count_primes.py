# 求素数个数
a = int(input())
b = int(input())

def cout_primes(start, end):
    count = 0
    for i in range(start, end+1):
        for j in range(2, i):
            if i%j == 0:
                # print(f'{i}不是素数')
                break
        else:
            # print(f'{i}是素数')
            count += 1
    return count


count = cout_primes(a,b)
print(count)