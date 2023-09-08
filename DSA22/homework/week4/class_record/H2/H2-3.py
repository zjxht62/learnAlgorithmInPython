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


import re


def HTML_2_tag_list(s: str) -> list[str]:
    # 取出每个标签左右尖括号内的内容，包括闭标签内的/
    regex = re.compile('<(.*?)>')
    return regex.findall(s)


def is_match(open: str, close: str) -> bool:
    return True if open == close[1:] else False


def HTMLMatch(s) -> bool:
    # 请在此编写你的代码（可删除pass语句）
    # 创建stack
    tag_stack = Stack()
    # 使用正则，将文本转换成tag的列表 ['html', 'head', 'title', '/title', '/head', 'body', 'h1', '/h1', '/body', '/html']
    tag_list = HTML_2_tag_list(s)
    index = 0
    balanced = True
    # 按顺序遍历列表
    while index < len(tag_list) and balanced:
        current_tag = tag_list[index]
        # 如果是开标记，则入栈
        if not current_tag[0] == '/':
            tag_stack.push(current_tag)
        else:
            # 若栈不为空，弹出栈顶元素，判断是否匹配
            if not tag_stack.isEmpty():
                top_tag = tag_stack.pop()
                if not is_match(top_tag, current_tag):
                    balanced = False
            # 若栈为空，说明闭标记多了，标签不匹配
            else:
                balanced = False
        index += 1
    # 若循环结束，栈不为空，说明开标记多了，标签不匹配
    if not tag_stack.isEmpty():
        balanced = False
    # 返回是否匹配
    return balanced
    # 代码结束


def HTMLMatch2(s) -> bool:
    def isOpenTag(tag: str) -> bool:  # 判断是否是开标记
        return tag[1] != '/'

    def matches(open: str, close: str) -> bool:  # 判断两个是否配对
        return open == close.replace("/", "")

    def getTag(s: str, i: int) -> tuple[str, int]:  # 从i位置"<"开始找到一个标记，<tag>或者</tag>
        t = ''
        while s[i] != '>':
            t += s[i]
            i += 1
        t += '>'
        return t, i  # 返回标记和结束位置

    st = Stack()
    balanced = True
    index = 0
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == "<":
            tag, index = getTag(s, index)
        if isOpenTag(tag):
            st.push(tag)
        else:
            if st.isEmpty():
                balanced = False
            else:
                top = st.pop()
                if not matches(top, tag):
                    balanced = False
        # 忽略所有非标记内容
        while index <len(s) and s[index] != "<":
            index += 1
    if balanced and st.isEmpty():
        return True
    else:
        return False


# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch2(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch2(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))
