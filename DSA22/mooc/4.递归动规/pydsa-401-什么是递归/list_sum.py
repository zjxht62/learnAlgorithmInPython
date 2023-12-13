def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum


print(list_sum([1, 2, 4, 5, 6, 3]))


def list_sum_recursion(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])

print(list_sum_recursion([1, 2, 4, 5, 6, 3]))