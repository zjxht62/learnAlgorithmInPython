# 冒泡排序改进：通过判断某一趟比对是否有交换，提前确定排序是否完成
def bubble_sort(alist):
    # 首先将交换设置为True
    switch = True
    i = len(alist) - 1
    # 每趟循环判断是否交换过，若没交换过，后续趟就不比较了
    while i > 0 and switch:
        # 设置当前趟交换为False
        switch = False
        for j in range(i):
            if alist[j] > alist[j + 1]:
                # 发生交换
                switch = True
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
        i -= 1
    return alist


if __name__ == '__main__':
    print(bubble_sort([6, 1, 2, 3, 4, 5, ]))
