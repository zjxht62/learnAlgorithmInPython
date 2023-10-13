def mergeSort(alist):
    # 基本结束条件
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        # 拉链式交错把左右半部分从小到大归并到结果列表中
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        # 归并左半部分剩余项
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        # 归并右半部分剩余项
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


if __name__ == '__main__':
    alist = [1, 2, 7, 45, 3234, 75, 23, 42, 56, 2, 9, 43, 22, 64]
    mergeSort(alist)
    print(alist)
