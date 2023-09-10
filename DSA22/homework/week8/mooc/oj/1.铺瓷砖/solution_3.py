# W06-1-2，铺瓷砖动态规划版本
n = int(input())
cache = {0: 1, 1: 1, 2: 2, 3: 4, 4: 8}


def total(N):
    if N <= 4:
        return cache[N]
    else:
        for i in range(5, N+1):
            cache[i] = cache[i-1]+cache[i-2]+cache[i-3]+cache[i-4]
        return cache[N]


print(total(n))
