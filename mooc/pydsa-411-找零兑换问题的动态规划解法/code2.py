# 动态规划求解找零问题
def doChangeInDP(coin_value_list, change, min_coins_list, coin_used):
    for cents in range(1, change + 1):
        coin_count = cents
        # 初始化一下新加硬币
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins_list[cents - j] + 1 < coin_count:
                coin_count = min_coins_list[cents - j] + 1
                new_coin = j  # 对应最小数量，所减的硬币
        coin_used[cents] = new_coin  # 记录本步骤加的一个硬币
        min_coins_list[cents] = coin_count

    return min_coins_list[change]


def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        this_coin = coin_used[coin]
        print(this_coin)
        coin = coin - this_coin


if __name__ == '__main__':
    amnt=63
    clist=[1, 5, 10, 21, 25]
    coin_used = [0]*(amnt+1)
    coin_count = [0]*(amnt+1)
    print(f"Making change for {amnt} requires")
    print(f"{doChangeInDP(clist, amnt, coin_count, coin_used)} coins")
    print("They are:")
    print_coins(coin_used, amnt)
    print("The used list is as follows:")
    print(coin_used)