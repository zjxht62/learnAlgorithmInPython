def ordered_sequential_search(alist, item):
    for i in range(len(alist)):
        if alist[i] == item:
            return True
        elif alist[i] > item:
            return False
    else:
        return False

if __name__ == '__main__':
    print(ordered_sequential_search([1,3,5,7,9], 4))