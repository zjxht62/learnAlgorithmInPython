def insertion_sort(alist):
    step_list = []
    for i in range(1,len(alist)):
        current_value = alist[i]
        current_index = i
        while current_index >0 and alist[current_index-1]>current_value:
            alist[current_index] = alist[current_index-1]
            current_index-=1
        alist[current_index] = current_value
        step_list.append(alist.copy())

    return step_list



if __name__ == '__main__':


    steps = insertion_sort([5,3,2,6,7,1,9])
    print(steps)