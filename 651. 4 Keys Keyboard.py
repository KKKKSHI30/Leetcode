# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: 标答这个方法我感觉用了数学方法，不是纯正dp，dp的定义是到dp[j]为止，最多几个A,其中
# 发现了两个规律，dp[i] = i是【0-3）的时候, dp[j]=(j−i−1)⋅dp[i], where i+3≤j≤i+6，
# 超过i+6的时候就需要chon更新考虑CA-CC-CV了，所以每次i遍历的时候，j只需要i+3到i+6中间
class Solution:
    def maxA(self, n):
        dp = list(range(n + 1))
        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])
        return dp[n]

# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: 暴力动规，没有用上多余的技巧
class Solution2:
    def maxA(self,N):
        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(1, N+1):
            # 按 A 键
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
                # 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        # N 次按键之后最多有几个 A？
        return dp[N]

# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: 这个方法确实绝，不过还是用了一些数学基础，因为max只有可能出现cv复制两次，三次，四次的情况，超过的话肯定可以翻倍了
class Solution3(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = range(N+1)
        for i in range(7, N+1):
            f[i] = max(f[i-3]*2, f[i-4]*3, f[i-5]*4)

        return f[N]
# Tests:
test = Solution2()
test.maxA(10)