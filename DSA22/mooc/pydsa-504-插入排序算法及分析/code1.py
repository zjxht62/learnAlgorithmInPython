def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue




if __name__ == '__main__':
    # alist = [5,3,2,6,7,1,9]
    alist = [1,2,3,4,5,6,7]
    insertionSort(alist)
    print(alist)

