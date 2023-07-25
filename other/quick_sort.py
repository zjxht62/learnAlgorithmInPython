my_arr = [1, 2, 43, 21, 9, 66, 14, 78, 24, 33]


def quick_sort(arr, low, high):
    if low < high:
        j = partion(arr, low, high)
        quick_sort(arr, low, j - 1)
        quick_sort(arr, j + 1, high)


# 将列表分区，取最后一个元素为支点，小于它的放在左边，大于它的放在右边，返回排序后支点的下标
def partion(arr, low, high):
    less = low
    p = arr[high]
    for great in range(low, high):
        # 如果great所指向的元素大于p，则直接进入下一次循环
        if arr[great] < p:
            arr[less], arr[great] = arr[great], arr[less]
            less += 1
    arr[less], arr[high] = arr[high], arr[less]
    return less


quick_sort(my_arr, 1, 9)
print(my_arr)
