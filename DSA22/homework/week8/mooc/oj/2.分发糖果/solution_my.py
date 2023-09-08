def candy(ratings):
    # code here
    next_candy = 1
    total = 0
    for i in range(len(ratings)):
        total += next_candy
        current_score = ratings[i]
        if i != len(ratings)-1:
            next_score = ratings[i+1]
            if next_score>current_score:
                next_candy+=1
            else:
                next_candy =1
    return total

lst = eval(input())
print(candy(lst))