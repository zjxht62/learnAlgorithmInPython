def shell_sort(alist):
    sublist_num = len(alist)//2
    while sublist_num > 0:
        for start_position in range(sublist_num):
            insertion_sort_with_gap(alist, start_position, sublist_num)
        sublist_num = sublist_num //2


def insertion_sort_with_gap(alist, start, gap):
    for index in range(start+gap, len(alist), gap):
        current_value = alist[index]
        position = index
        while position>=gap and current_value<alist[position-gap]:
            alist[position] = alist[position-gap]
            position = position -gap
        alist[position] = current_value


if __name__ == '__main__':
    alist = [5,3,2,6,7,1,9]
    shell_sort(alist)
    print(alist)