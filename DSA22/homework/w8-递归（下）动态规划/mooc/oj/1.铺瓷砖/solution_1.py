# W06-1，铺瓷砖递归版本
n = int(input())
vlist = [1, 1, 2, 4, 8]

# 第1块是1,total(n-1)
# 第1块是2,total(n-2)
# 第1块是3,total(n-3)
# 第1块是4,total(n-4)

def total(N):
    if N <= 4:
        return vlist[N]
    else:
        return total(N - 1) + total(N - 2) + total(N - 3) + total(N - 4)


print(total(n))
