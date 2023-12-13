def shellSort(alist):
    sublistcount = len(alist) // 2  # 设定间隔
    while sublistcount > 0:
        # 子列表排序
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is ", alist)

        # 减小间隔
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and currentvalue < alist[position - gap]:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [1, 2, 7, 45, 3234, 75, 23, 42, 56, 2, 9, 43, 22, 64]
    shellSort(alist)
    print(alist)
