# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s) -> list:
    # 请在此编写你的代码（可删除pass语句）
    # 初始化10个队列，在比较各个位的时候来存储对应元素
    queue_list = []
    for i in range(10):
        queue_list.append(Queue())
    # 初始化main_queue来存储排序结果
    main_queue = Queue()
    # 首先将num入队
    for num in s:
        main_queue.enqueue(num)
    # 找出最大数的位数，确定循环次数
    max_len = len(str(max(s)))
    for i in range(max_len):
        while not main_queue.isEmpty():
            # 从最低位开始比较
            base_index = -(1 + i)
            element = main_queue.dequeue()
            # 将元素补全到max_len的位数，前面补0
            formatter_str = f"0{max_len}"  # 模板的一部分
            formatted_ele_str = f"{element:{formatter_str}}"
            # 将对应元素入队到对应的队列
            queue_list[int(formatted_ele_str[base_index])].enqueue(element)

        # 再将每个队列的数合并排到main队列
        for q in queue_list:
            while not q.isEmpty():
                main_queue.enqueue(q.dequeue())

    # 按顺序输出，得到排序后的结果
    result = []
    while not main_queue.isEmpty():
        result.append(main_queue.dequeue())
    return result
    # 代码结束


def radix_sort2(s) -> list:
    # 全部入队main
    main = Queue()
    for n in s:
        main.enqueue(n)
    # 找最大数，以及它的位数
    d = len(str(max(s)))
    dstr = "%%0%dd" % d  # 前导零的模板，如“%05d”,这里的5就是最大数的位数
    # 准备10个队列
    # 当不需要关心循环次数这个变量时，可以用下划线来表示，
    nums = [Queue() for _ in range(10)]
    for i in range(-1, -d - 1, -1): # 下标从-1到-d，代表个位到最高位
        while not main.isEmpty():
            n = main.dequeue()
            dn = (dstr % n)[i] # 转换成类似"00345[-2]"这里是倒数第二位
            nums[int(dn)].enqueue(n)
        # 从10个队列挨个集中回main队列
        for k in range(10):
            while not nums[k].isEmpty():
                main.enqueue(nums[k].dequeue())
    result = []
    while not main.isEmpty():
        result.append(main.dequeue())
    return result

        # 调用检验


print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))
