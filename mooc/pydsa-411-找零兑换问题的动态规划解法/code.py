# 动态规划求解找零问题
def doChangeInDP(coin_value_list, change, min_coins_list):
    for cents in range(1, change + 1):
        coin_count = cents
        for c in [d for d in coin_value_list if d <= cents]:
            if min_coins_list[cents - c] + 1 < coin_count:
                coin_count = min_coins_list[cents - c] + 1
        min_coins_list[cents] = coin_count

    return min_coins_list[change]


print(doChangeInDP([1, 5, 10, 25], 63, [0] * 64))
