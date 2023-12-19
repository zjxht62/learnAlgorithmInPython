# 分发糖果，两趟循环算法

def candy(ratings):
    candy_list_left = [1]*len(ratings) # 糖果列表-从左到右
    candy_list_right = [1]*len(ratings) # 糖果列表-从右到左
    for i in range(1, len(ratings)):
        if ratings[i]>ratings[i-1]:
            candy_list_left[i]=candy_list_left[i-1]+1

    for j in range(len(ratings)-1, 0, -1):
        if ratings[j]<ratings[j-1]:
            candy_list_right[j-1]=candy_list_right[j]+1

    candy_list = []
    for i in range(len(ratings)):
        candy_list.append(max(candy_list_left[i], candy_list_right[i]))
    return sum(candy_list)



lst = eval(input())
print(candy(lst))