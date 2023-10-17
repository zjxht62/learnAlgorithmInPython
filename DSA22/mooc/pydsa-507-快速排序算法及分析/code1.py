def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    # 基本结束条件
    if first < last:
        # 分裂
        splitpoint = partition(alist, first, last)
        # 递归调用
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    # 选定“中值”
    privotvalue = alist[first]
    # 初始化左右标
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # 向右移动左标，直到第一个比“中值”大的
        while leftmark <= rightmark and alist[leftmark] <= privotvalue:
            leftmark += 1
        # 向左移动右标，直到第一个比“中值”小的
        while rightmark >= leftmark and alist[rightmark] >= privotvalue:
            rightmark -= 1
        # 两标相错就结束移动
        if leftmark > rightmark:
            done = True
        else:
            # 交换左右标的值
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    # 最后就位“中值”
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    # 返回中值点，也就是分裂点
    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
