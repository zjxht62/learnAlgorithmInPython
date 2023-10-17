def partition(alist, left,right):
    privot = alist[left]
    left_mark = left+1
    right_mark = right

    done = False
    while not done:
        while left_mark<=right_mark and alist[left_mark]<=privot:
            left_mark+=1
        while right_mark >= left_mark and alist[right_mark]>=privot:
            right_mark -=1

        if left_mark>right_mark:
            done = True
            alist[left],alist[right_mark] = alist[right_mark],alist[left]
        else:
            alist[left_mark],alist[right_mark] = alist[right_mark],alist[left_mark]

    return right_mark

def quick_sort(alist):
    quick_sort_helper(alist,0,len(alist)-1)

def quick_sort_helper(alist, first, last):
    if first<last:
        privot_point = partition(alist, first, last)
        quick_sort_helper(alist,first, privot_point-1)
        quick_sort_helper(alist,privot_point+1,last)


if __name__ == '__main__':
    alist = [6,1,4,3,2,7,9,5,8,23,5646,234,342,7,234234,46,1,234,5454]
    quick_sort(alist)
    print(alist)