# Given two integers N and B, the task is to print the maximum index in an array that can be reached,
# starting from the 0th index, in N steps without placing itself at index B at any point, where
# in every ith step, pointer can move i indices to the right.
# notes: 注意观察，只可能是sum和sum-1两个结果
def maximumIndex(N, B):
    i, j = 0, 1
    sum = N * (N + 1) // 2
    flag = False
    while (j <= N):
        i += j
        j += 1
        if (i == B):
            flag = True
            break
    if (not flag):
        return sum
    else:
        return sum - 1

maximumIndex(4,6)