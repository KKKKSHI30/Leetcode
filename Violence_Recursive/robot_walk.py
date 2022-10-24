def robot_walk(N, M, P, K):
    return process(N, M, P, K)

def process(N, M, P, K):
    # k steps     rest steps
    # P final position   end position
    # N length   total length
    # M start point  cur position
    if K == 0:
        if P == M:
            return 1
        else:
            return 0
    if M == 1:
        return process(N, 2, P, K-1)
    if M == N:
        return process(N, N-1, P, K-1)
    return process(N, M+1, P, K-1) + process(N, M-1, P, K-1)

robot_walk(5,2,3,3) # 3
robot_walk(3,1,3,3) # 0

def robot_walk2(N, M, P, K):
    # N is column, K is rows  N * K = 6 * 4
    dp = [[None for i in range(N+1)] for j in range(K+1)]
    return process2(N, M, P, K, dp)

def process2(N, M, P, K, dp):
    if dp[K][M] != None:
        return dp[K][M]
    if K == 0:
        if P == M:
            dp[K][M] = 1
            return dp[K][M]
        else:
            dp[K][M] = 0
            return dp[K][M]
    if M == 1:
        dp[K][M] = process2(N, 2, P, K-1, dp)
        return dp[K][M]
    elif M == N:
        dp[K][M] = process2(N, N-1, P, K-1, dp)
    else:
        dp[K][M] = process2(N, M+1, P, K-1, dp) + process2(N, M-1, P, K-1, dp)
    return dp[K][M]

robot_walk2(5,2,3,3) # 3
robot_walk2(3,1,3,3) # 0

def robot_walk3(N, M, P, K):
    dp = [[0 for i in range(N + 1)] for j in range(K + 1)]
    dp[0][P] = 1
    for k in range(1, K+1):
        for m in range(1, N+1):
            if m == 1:
                dp[k][m] = dp[k-1][2]
            elif m == N:
                dp[k][m] = dp[k-1][N-1]
            else:
                dp[k][m] = dp[k-1][m-1] + dp[k-1][m+1]
    return dp[K][M]

robot_walk3(5,2,3,3) # 3
robot_walk3(3,1,3,3) # 0