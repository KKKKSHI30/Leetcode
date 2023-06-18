import sys
def coin_ways(arr, aim):
    return process(arr, 0, aim)

def process(arr, index, rest):
    if index == len(arr):
        return 1 if rest == 0 else 0
    ways = 0
    for zhang in range(sys.maxsize):
        if arr[index] * zhang > rest:
            break
        ways += process(arr, index+1, rest - arr[index]*zhang)
    return ways

coin_ways([5,2,3], 10)  # 4
coin_ways([5,2,3], 0)  # 1
coin_ways([3,5], 2)  # 0

def coin_ways2(arr, aim):
    if arr == None or len(arr) == 0:
        return 0
    N = len(arr)
    dp = [[0 for i in range(aim+1)] for j in range(N+1)]
    dp[N][0] = 1
    for index in range(N-1, -1, -1):
        for rest in range(0, aim+1):
            ways = 0
            for zhang in range(sys.maxsize):
                if arr[index] * zhang > rest:
                    break
                ways += dp[index+1][rest - arr[index] * zhang]
                dp[index][rest] = ways
    return dp[0][aim]

coin_ways2([5,2,3], 10)  # 4
coin_ways2([5,2,3], 0)  # 1
coin_ways2([3,5], 2)  # 0

def coin_ways3(arr, aim):
    if arr == None or len(arr) == 0:
        return 0
    N = len(arr)
    dp = [[0 for i in range(aim + 1)] for j in range(N + 1)]
    dp[N][0] = 1
    for index in range(N - 1, -1, -1):
        for rest in range(0, aim + 1):
            dp[index][rest] = dp[index+1][rest]
            if (rest - arr[index] >= 0):
                dp[index][rest] += dp[index][rest - arr[index]]
    return dp[0][aim]
coin_ways3([5,2,3], 10)  # 4
coin_ways3([5,2,3], 0)  # 1
coin_ways3([3,5], 2)






















