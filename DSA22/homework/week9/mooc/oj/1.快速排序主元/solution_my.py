unjudged_input = input()
unjudged_list = unjudged_input.split()
unjudged_num_list = [int(s) for s in unjudged_list]

def privot_judge(alist: list):
    privot_count = 0
    privot_list = []
    for i in range(len(alist)):
        current_value = alist[i]
        is_privot = True
        back_index = i - 1
        while back_index >= 0:
            if not alist[back_index] < current_value:
                is_privot = False
                break
            back_index -= 1
        forward_index = i + 1
        while forward_index < len(alist):
            if not alist[forward_index] > current_value:
                is_privot = False
                break
            forward_index += 1

        if is_privot:
            privot_count += 1
            privot_list.append(current_value)

    return privot_count,privot_list


privot_count,privot_num_list = privot_judge(unjudged_num_list)
print(privot_count)
print(' '.join([str(i) for i in privot_num_list]))