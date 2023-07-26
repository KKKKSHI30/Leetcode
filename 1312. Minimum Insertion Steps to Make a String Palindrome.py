# Iterative Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.25: yes
# notes: 和516实在是太像了，基本就是秒了
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 0
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1])+1
        return dp[0][n-1]


# Dynamic Programming with Space Optimization
# Time: O(n^2)
# Space: O(n)
# 2023.07.25: yes
class Solution2(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp,dpPrev = [0 for _ in range(n)],[0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i] = 0
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j-1]
                else:
                    dp[j] = min(dpPrev[j], dp[j - 1])+1
            dpPrev = dp[:]
        return dp[n-1]

# Recursive Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.25: no
# notes: 谁现在还用recursion啊
class Solution3(object):
    def lcs(self, s1, s2, m, n, memo):
        if m == 0 or n == 0:
            return 0
        if memo[m][n] != -1:
            return memo[m][n]
        if s1[m - 1] == s2[n - 1]:
            memo[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
        else:
            memo[m][n] = max(self.lcs(s1, s2, m - 1, n, memo), self.lcs(s1, s2, m, n - 1, memo))
        return memo[m][n]

    def minInsertions(self, s):
        n = len(s)
        sReverse = s[::-1]
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        return n - self.lcs(s, sReverse, n, n, memo)


# Tests:
test = Solution2()
test.minInsertions(s = "zzazz")
test.minInsertions(s = "mbadm")