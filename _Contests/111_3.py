class Solution:
    def minimumOperations(self, nums):
        def change(first, second):
            c = 0
            for i in range(first):
                if nums[i] != 1:
                    c += 1
            for j in range(first, second):
                if nums[j] != 2:
                    c += 1
            for k in range(second, n):
                if nums[k] != 3:
                    c += 1
            return c
        n = len(nums)
        min_change = float("inf")
        for i in range(n+1):
            for j in range(i,n+1):
                min_change = min(change(i, j), min_change)
        return min_change

# DP
# notes: 遇到一个就在当前位置-1因为当前位置就会少一个operation
# dp[2]就是1和2中小的，dp[3]就是2和3中小的，因为子串都可以更小，当前也可
# 也可以用max来做，方法差不多
class Solution2:
    def minimumOperations(self, A):
        dp = [len(A)] * 4
        for a in A:
            dp[a] -= 1
            dp[2] = min(dp[2], dp[1])
            dp[3] = min(dp[3], dp[2])
        return dp[3]

# Longest Increasing Subsequence
# notes: 找到LIS，剩下的就是需要排序的
class Solution3:
    def minimumOperations(self, v):
        n = len(v)
        dp = [1] * n
        m = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if v[i] >= v[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    m = max(m, dp[i])
        return n - m
# Tests:
test = Solution2()
test.minimumOperations([2,1,3,2,1]) # 3
test.minimumOperations([2,2,2,2,3,3]) # 0
test.minimumOperations([1,3,2,1,3,3]) # 2

test.minimumOperations([1]) # 0
