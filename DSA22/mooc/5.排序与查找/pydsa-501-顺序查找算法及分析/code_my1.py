def sequential_Search(alist, item):
    for i in range(len(alist)):
        if item == alist[i]:
            return True
    # 当for循环正常执行完成，没有break时执行
    else:
        return False


if __name__ == '__main__':
    result = sequential_Search([1,2,3,4,5], 7)
    print(result)