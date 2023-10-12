def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        # n-1趟
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                # 错序，交换
                # temp = alist[i]
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp

                # Python支持直接交换
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
