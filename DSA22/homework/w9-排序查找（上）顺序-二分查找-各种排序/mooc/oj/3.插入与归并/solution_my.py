def insertion_sort(alist):
    step_list = []
    for i in range(1, len(alist)):
        current_value = alist[i]
        current_index = i
        while current_index > 0 and alist[current_index - 1] > current_value:
            alist[current_index] = alist[current_index - 1]
            current_index -= 1
        alist[current_index] = current_value
        step_list.append(alist.copy())

    return step_list


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                alist[k] = right[j]
                j += 1
            else:
                alist[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1


# str1 = input()
# origin_num_list = [int(i) for i in str1.split()]
# print(origin_num_list)
# str2 = input()
# judge_num_list = [int(i) for i in str2.split()]
# print(judge_num_list)
#
# insertion_sort_steps = insertion_sort(origin_num_list)
# if judge_num_list in insertion_sort_steps:
#     print('Insertion Sort')
# else:
#     print('Merge Sort')

if __name__ == '__main__':
    alist = [1, 2, 7, 45, 3234, 75, 23, 42, 56, 2, 9, 43, 22, 64]
    merge_sort(alist)
    print(alist)
