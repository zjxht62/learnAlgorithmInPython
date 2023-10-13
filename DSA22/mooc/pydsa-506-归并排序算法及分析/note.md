# 归并排序算法及分析
## 归并排序Merge Sort
+ 下面我们来看看**分治策略**在排序中的应用
+ 归并排序是递归算法，思路是将数据表持续分裂为两半，对两半分别进行归并排序
  + 递归的**基本结束条件**是：数据表仅有1个数据项，自然是排好序的
  + **缩小规模**：将数据表分为相等的两半，规模减小为原来的二分之一
  + **调用自身**：将两半分别调用自身排序，然后将分别排好序的两半进行归并，得到排序好的数据表

![img.png](img.png)
## 归并排序：代码
```python
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

```