# 动态规划求解找零问题
def doChangeInDP(coin_value_list, change, min_coins_list, current_coin_size):
    for i in range(1, change+1):
        return_coins = i
        for c in [j for j in coin_value_list if j <= i]:
            if min_coins_list[i-c] +1 < return_coins:
                return_coins = min_coins_list[i-c]+1
                # 记录每一次最优解选择的面值
                current_coin_size[i]=c
        min_coins_list[i] = return_coins

    # 回溯结果，从change开始，每次减去当前change所选面额，直到change小于0
    while change >0:
        print(current_coin_size[change])
        change = change - current_coin_size[change]

    # return min_coins_list[change]



doChangeInDP([1, 5, 10, 25], 63, [0] * 64, [0]*64)
