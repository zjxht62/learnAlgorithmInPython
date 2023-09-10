# W06-1，铺瓷砖递归版本+函数值缓存
n = int(input())
cache = {0: 1, 1: 1, 2: 2, 3: 4, 4: 8}


# 第1块是1,total(n-1)
# 第1块是2,total(n-2)
# 第1块是3,total(n-3)
# 第1块是4,total(n-4)
def total(N):
    if N <= 4:
        return cache[N]
    elif N in cache:
        return cache[N]
    else:
        cache[N] = total(N - 1) + total(N - 2) + total(N - 3) + total(N - 4)
        return cache[N]


print(total(5))
