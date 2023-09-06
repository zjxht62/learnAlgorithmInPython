# 递归求解找零问题，按照老师ppt思路编写
import time


def recMC(coin_value_list, change):
    # 最小规模问题，直接返回一个硬币
    if change in coin_value_list:
        return 1
    else:
        # 对于每种硬币，递归调用，找出最小找零数量
        return_coin_list = []
        for current_coin in [c for c in coin_value_list if c < change]:
            return_coin_list.append(recMC(coin_value_list, change - current_coin) + 1)
        return min(return_coin_list)


if __name__ == '__main__':
    t1 = time.process_time()
    print(recMC([1, 5, 10, 25], 63))
    t2 = time.process_time()
    print('time:', t2 - t1)
