def merge_sort(alist):
    # 最小子问题，长度为0或只有一个元素，直接返回
    if len(alist)<=1:
        return alist
    else:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        # 缩小问题规模
        # 递归调用自身
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        # 合并过程
        while i < len(left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:
                alist[k] = left_half[i]
                i+=1
            else:
                alist[k] = right_half[j]
                j+=1
            k+=1
        # 处理剩余项
        while i < len(left_half):
            alist[k] = left_half[i]
            i+=1
            k+=1

        while j < len(right_half):
            alist[k] = right_half[j]
            j+=1
            k+=1


if __name__ == '__main__':
    alist = [1, 2, 7, 45, 3234, 75, 23, 42, 56, 2, 9, 43, 22, 64]
    merge_sort(alist)
    print(alist)
