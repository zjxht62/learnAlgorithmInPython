# https://smartkeyerror.com/dp(01)
# 记忆化搜索
import time
def recMC(coinValueList, change, mem):
    mincoins = change
    if change in coinValueList:
        # 记录最优解
        mem[change] = 1
        return 1
    # 先查表，成功的话直接用最优解
    elif mem[change] >0:
        return mem[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            numcoins = 1 + recMC(coinValueList, change-i, mem)
            if numcoins < mincoins:
                mincoins = numcoins
                # 记录最优解
                mem[change] = mincoins

    return mincoins


t1 = time.process_time()
print(recMC([1, 5, 10, 25], 63, [0]*64))
t2=time.process_time()
print('time:',t2-t1)
