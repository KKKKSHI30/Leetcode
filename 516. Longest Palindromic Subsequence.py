# Recursive Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}
        def lps(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                memo[(l, r)] = lps(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(lps(l, r - 1), lps(l + 1, r))
            return memo[(l, r)]

        return lps(0, n - 1)

# Iterative Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
# notes: 找到状态转移方程式重中之重，dp[i][j]是从i到j的最长回文串长度
# j < i的部分不存在，初始化为0
class Solution2(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]


# Dynamic Programming with Space Optimization
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
class Solution3(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp, dpPrev = [0 for _ in range(n)],[0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j-1]+2
                else:
                    dp[j] = max(dpPrev[j], dp[j-1])
            dpPrev = dp[:]
        return dp[n-1]

# Tests:
test = Solution3()
test.longestPalindromeSubseq("bbbab")
test.longestPalindromeSubseq("cbbd")
