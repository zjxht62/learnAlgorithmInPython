def selection_sort(alist):
    # 比较n-1趟
    for passnum in range(len(alist) - 1, 0, -1):
        max_index = 0
        # 找出本趟中最大项的下标，其中passnum+1是为了判断到最后一项
        # 如果不这样的话，当最大项在最后一项时，那就会把最后一项之前的最大项和最后一项交换，就会导致错误
        for i in range(passnum+1):
            if alist[i] > alist[max_index]:
                max_index = i

        alist[passnum],alist[max_index]= alist[max_index],alist[passnum]



if __name__ == '__main__':
    alist = [6,1,45,2,7,99,12,3,111]
    selection_sort(alist)
    print(alist)