def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            return True
        else:
            # 如果当前比对的元素已经比要查找的大了，那么后面肯定都比它大，就不用比了
            if alist[pos] > item:
                stop = True
                # 提前退出
            else:
                pos += 1
    return found


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(ordered_sequential_search(testlist,3))
    print(ordered_sequential_search(testlist,13))
