def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    while last >= first:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid-1
        else:
            first = mid+1
    return False


if __name__ == '__main__':
    result = binary_search([1,3,5,7,10,14,16,22],1)
    print(result)