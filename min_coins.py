import sys

def min_coins(arr, aim):
    return process(arr, 0, aim)

def process(arr, index, rest):
    if index == len(arr):
        return 0 if rest == 0 else -1
    res = -1
    for k in range(0, sys.maxsize):
        if k * arr[index] > rest:
            break
        next = process(arr, index+1, rest - k*arr[index])
        if next != -1:
            res = next+k if res == -1 else min(res, next+k)
    return res

min_coins([5,2,3], 20)
min_coins([5,2,3], 0)
min_coins([3,5], 2)

def min_coins2(arr, aim):
    N = len(arr)
    dp = [[-1 for i in range(aim + 1)] for j in range(N + 1)]
    dp[N][0] = 0
    for i in range(N-1, -1, -1):
        for rest in range(aim+1):
            dp[i][rest] = -1
            if dp[i+1][rest] != -1:
                dp[i][rest] = dp[i+1][rest]
            if (rest - arr[i] >= 0 and dp[i][rest-arr[i]] != -1):
                if dp[i][rest] == -1:
                    dp[i][rest] = dp[i][rest-arr[i]] + 1
                else:
                    dp[i][rest] = min(dp[i][rest], dp[i][rest-arr[i]]+1)
    return dp[0][aim]

min_coins2([5,2,3], 20)
min_coins2([5,2,3], 0)
min_coins2([3,5], 2)
