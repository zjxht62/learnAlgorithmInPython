def insertion_sort(alist):
    for times in range(1,len(alist)):
        current_item_value = alist[times]
        current_index = times
        # for i in range(current_index-1, -1, -1):
        #     if current_item_value<alist[i]:
        #         alist[i+1] = alist[i]
        #         if i == 0:
        #             alist[i] = current_item_value
        #     else:
        #         alist[i] = current_item_value
        #         break

        i = current_index-1
        while i >=0 and current_item_value<alist[i]:
            alist[i+1] = alist[i]
            i-=1
        alist[i+1] = current_item_value







if __name__ == '__main__':
    alist = [5,3,2,6,7,1,9]
    insertion_sort(alist)
    print(alist)

