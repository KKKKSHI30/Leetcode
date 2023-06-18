def bob_die(N, M, i, j, k):
    all = 4 ** k
    live = process(N, M, i, j, k)
    gcd = gcd_func(all, live)
    return print(f"The possibility that bob will die is {live/gcd}/{all/gcd}")

def process(N, M, row, col, rest):
    if (row < 0 or row == N or col < 0 or col == M):
        return 0
    if rest == 0:
        return 1
    live = process(N, M, row - 1, col, rest - 1) +\
           process(N, M, row + 1, col, rest - 1) +\
           process(N, M, row, col - 1, rest - 1) +\
           process(N, M, row, col + 1, rest - 1)
    return live

def gcd_func(m, n):
    return m if n == 0 else gcd_func(n, m % n)

def bob_die2(N, M, i, j, k):
    dp = [[[0 for _ in range(k + 1)] for _ in range(M+2)] for _ in range(N+2)]
    for row in range(1, N+1):
        for col in range(1, M+1):
            dp[row][col][0] = 1
    for rest in range(1, k+1):
        for row in range(1, N+1):
            for col in range(1, M+1):
                dp[row][col][rest] = dp[row - 1][col][rest - 1]
                dp[row][col][rest] += dp[row + 1][col][rest - 1]
                dp[row][col][rest] += dp[row][col - 1][rest - 1]
                dp[row][col][rest] += dp[row][col + 1][rest - 1]
    all = 4 ** k
    live = process(N, M, i, j, k)
    gcd = gcd_func(all, live)
    return print(f"The possibility that bob will die is {live/gcd}/{all/gcd}")

bob_die(10, 10, 3, 2, 5)  # 945/1024
bob_die2(10, 10, 3, 2, 5)  # 945/1024
