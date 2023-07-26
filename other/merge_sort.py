class MergeSort:
    def __init__(self):
        self.data = []

    def merge_sort(self, start, end):
        if start == end: return
        # 将列表拆分为两半
        mid = (start + end) // 2
        # 递归地处理拆分后的列表，直到只有一个元素
        self.merge_sort(start, mid)
        self.merge_sort(mid + 1, end)
        # 在归的过程中，合并并排序
        self.merge_data(start, mid, end)

    def merge_data(self, start, mid, end):
        # 合并两个列表
        temp = []
        # 指针初始化到两个部分的头一个元素
        i = start
        j = mid + 1
        # 比较两个元素，将较小者添加到temp，指针+1
        while i <= mid and j <= end:
            if self.data[i] < self.data[j]:
                temp.append(self.data[i])
                i += 1
            else:
                temp.append(self.data[j])
                j += 1
        # 处理剩余元素
        while i <= mid:
            temp.append(self.data[i])
            i += 1
        while j <= end:
            temp.append(self.data[j])
            j += 1

        # 将temp赋值回data中
        for i in temp:
            self.data[start] = i
            start += 1


if __name__ == '__main__':
    ms = MergeSort()
    ms.data = [34, 51, 78, 88, 9, 11, 32, 37]
    ms.merge_sort(0, 7)
    print(ms.data)
