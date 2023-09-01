# https://smartkeyerror.com/dp(01)
import time
def recMC(coinValueList, change):
    # 先初始化mincoins=change，假设全用1块的找零，最多也就change个
    mincoins = change
    # 最小规模问题，如果找零整好等于某一种硬币的面额，那么就直接返回1
    if change in coinValueList:
        return 1
    else:
        # 减小问题规模，将每一种情况都实验完成，选择找零需要的最小硬币数
        for i in [c for c in coinValueList if c < change]:
            numcoins = 1 + recMC(coinValueList, change-i)
            if numcoins < mincoins:
                mincoins = numcoins

    return mincoins


t1 = time.process_time()
print(recMC([1, 5, 10, 25], 63))
t2=time.process_time()
print('time:',t2-t1)
