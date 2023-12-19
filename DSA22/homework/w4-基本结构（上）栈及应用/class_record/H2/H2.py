#uuid_share#  4e746bfe-8d2d-42ca-af59-cb654a86adee  #
# PKUDSA课程上机作业
# 【H2】栈与队列编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的*函数体内*编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
#

# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def calculate(s) -> float:
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))

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
    pass
    # 代码结束


# 调用检验
print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))

# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False


def HTMLMatch(s) -> bool:
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))


class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class LinkStack():
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


class LinkQueue():
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False


# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__
class DoublyLinkedList():
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束


# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[3:8:2])  # ['10', 10, 14]