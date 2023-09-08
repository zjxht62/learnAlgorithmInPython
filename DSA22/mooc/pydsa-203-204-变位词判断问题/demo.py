# 编写一个bool函数，以两个词作为参数，返回这两个词是否为变位词
# 举例：earth和heart就是一组变位词

# 解法1：逐字检查
# 自己的实现
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    char_list1 = list(word1)
    char_list2 = list(word2)

    for i in range(len(word1)):
        for j in range(len(word2)):
            if char_list1[i] == char_list2[j]:
                char_list2[j] = None
                break
    for char in char_list2:
        if char != None:
            return False
    else:
        return True

# 课件示例
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK: # 循环s1的每个字符
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found: #在s2中逐个对比
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None # 找到，打钩
        else:
            stillOK = False # 未找到，直接失败
        pos1 += 1
    return stillOK

# 解法2：排序比较
# 自己实现
def is_anagram2(word1, word2):
    char_list1 = list(word1)
    char_list2 = list(word2)

    char_list1.sort()
    char_list2.sort()

    for i in range(len(char_list1)):
        if char_list1[i] != char_list2[i]:
            return False
    else:
        return True

# 课件示例
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches

# 解法3：暴力法
# 自己实现

# 解法4：计数比较
# 自己实现
def is_aragram4(w1, w2):
    dict_w1 = {}
    for c in w1:
        if c not in dict_w1.keys():
            dict_w1[c]=1
        else:
            dict_w1[c] += 1
    print(dict_w1)

    dict_w2 = {}
    for c in w2:
        if c not in dict_w2.keys():
            dict_w2[c]=1
        else:
            dict_w2[c] += 1
    print(dict_w2)

    return dict_w2 == dict_w1

def aragramSolution4(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1

    j = 0
    still_match = True
    while j < 26 and still_match:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_match = False
    return still_match


if __name__ == '__main__':
    print(anagramSolution2("typhon", 'pythno'))
    print(aragramSolution4("typhonn", 'pythnoo'))
