# Dynamic Programming 2D recursion
# Time: O(mn^2)
# Space: O(mn)
# 2023.07.26: no
# notes: i是当前12:00方向值得数值，j是目前在第几个数值，通过遍历的方法，把所有一圈的可能性都过一遍，找到符合的
import collections
class Solution:
    def findRotateSteps(self, ring, key):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0
            ans = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[j]:
                    delta = abs(k - i)
                    steps = min(delta, len(ring) - delta)
                    ans = min(ans, steps + dp(k, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0) + len(key)


# Dynamic Programming 1D Iteration
# Time: O(mn)
# Space: O(n)
# 2023.07.26: no
# notes: 优化了几个点，用hash map记录节点，用1D table，核心的那句被压缩了，找到所有pre的节点(可能有很多位置)
# 的最少次数到每一个新字符(也可能有很多位置)的位置，update每个新字符即可，还要min(顺时针，逆时针)+1和加上按下去的时间
class Solution2:
    def findRotateSteps(self, ring, key):
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring):
            indexes[c].append(i)
        for i in indexes[key[0]]:
            dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = c
        return min(dp[i] for i in indexes[key[-1]])

# Tests:
test = Solution2()
test.findRotateSteps(ring = "godding", key = "gd")

