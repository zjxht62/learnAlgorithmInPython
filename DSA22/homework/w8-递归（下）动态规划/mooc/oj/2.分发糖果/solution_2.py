# 分发糖果，两趟循环算法

def candy(ratings):
    n = len(ratings)
    left = [0] * n
    for i in range(n):
        if i > 0 and ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1

    # right = ret = 0
    right = 1
    ret = 0
    for i in range(n - 1, -1, -1):
        # i从n-1开始，也就是最后一个元素，所以第一次不进if，right直接是1
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1
        ret += max(left[i], right)

    return ret


lst = eval(input())
print(candy(lst))
