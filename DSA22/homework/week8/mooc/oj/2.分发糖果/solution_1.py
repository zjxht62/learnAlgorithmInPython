# 分发糖果贪心算法

def candy(ratings):
    candy_list = [1]*len(ratings) # 糖果列表
    for i in range(1, len(ratings)):
        if ratings[i]>ratings[i-1]: # 后面小朋友分数更高，那么比前面多1颗糖
            candy_list[i]=candy_list[i-1]+1
        elif ratings[i]==ratings[i-1]: # 分数相同，给最低标准
            candy_list[i] =1
        else:
            candy_list[i] =1 # 分数低，给最低标准1颗糖
            if candy_list[i-1]==1: # 但是如果前面只有1颗糖，需要加糖
                # range是左闭右开，到不了-1
                for k in range(i-1, -1, -1):
                    candy_list[k]+=1
                    # 评分向前递增，而糖果数没有递增的话，才加糖
                    if k > 0 and ratings[k-1]<=ratings[k] or candy_list[k-1]>candy_list[k]:
                        break

    return sum(candy_list)



lst = eval(input())
print(candy(lst))