def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist


if __name__ == '__main__':
    print(bubble_sort([6,1,45,2,7,99,12,3,]))

