def f(n, k, memo={}):
    if k == 0 and n == 0:
        return 1
    if n <= 0 or k <= 0:
        return 0
    key = str([n, k])
    if key in memo:
        return memo[key]
    memo[key] = f(n - k, k, memo) + f(n - 1, k - 1, memo)
    return memo[key]

def f2(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - j][j] + dp[i - 1][j - 1]

    return dp[n][k]


result = f(8,4)
result2 = f2(8,4)
