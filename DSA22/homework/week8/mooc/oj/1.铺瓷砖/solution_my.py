
# n = int(input())
def tiling(ceramic_tile_list, N, memo):
    if N == 0:
        return 1
    elif memo[N]:
        return memo[N]
    res = 0
    for ceramic_tile_size in [c for c in ceramic_tile_list if c <= N]:
        res += tiling(ceramic_tile_list, N - ceramic_tile_size, memo)
        memo[N] = res
    return res


if __name__ == '__main__':
    n = 5
    print(tiling([1, 2, 3, 4], n, [0]*(n+1)))


# print(tiling([1, 2, 3, 4], n, [0]*(n+1)))