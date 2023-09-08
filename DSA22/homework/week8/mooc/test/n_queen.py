# n皇后问题
def solve_queen(N):
    # 记录每行放在第几列，pool[0]=1表示第0行放在了第1列
    pool = [None]*N
    def queen(cur=0):
        # 基本结束条件，遍历到了最后一行，表示发现一种解法
        if cur == len(pool):
            return 1 # 返回解的数量
            # return list(pool) # 返回所有解
        res =0 # 返回解的数量
        # res =[]   # 返回所有解
        # 遍历每一列
        for col in range(len(pool)):
            # 假设当前行，col列可放
            pool[cur], flag = col, True
            # 检查之前的row行是否有冲突
            for row in range(cur):
                if pool[row] == col or abs(col - pool[row]) == cur - row:
                    # 结束当前循环，继续上层循环，看看cur行下一个col能放不
                    flag = False
                    break
            # 如果有能
            if flag:
                res += queen(cur+1)
        return res

    return queen(0)
print(solve_queen(8))