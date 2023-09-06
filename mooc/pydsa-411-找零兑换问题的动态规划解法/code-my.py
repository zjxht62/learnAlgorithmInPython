# 动态规划求解找零问题
def doChangeInDP(coin_value_list, change, min_coins_list):
    for i in range(1, change+1):
        return_coins = i
        for c in [j for j in coin_value_list if j <= change]:
            if min_coins_list[change-c] +1 < return_coins:
                min_coins_list[change] = min_coins_list[change-c]+1
        min_coins_list[change] = return_coins

    return min_coins_list[change]



print(doChangeInDP([1, 5, 10, 25], 63, [0] * 64))
