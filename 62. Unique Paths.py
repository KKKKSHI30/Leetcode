# Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.31: yes
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

# Dynamic Programming
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1, n):
                dp[j] = dp[j-1]+dp[j]
        return dp[n-1]

# Dynamic Programming
# Time: O((M+N)(log(M+N)loglog(M+N))^2)
# Space: O(1)
# 2023.07.31: no
# notes: 纯数跳过
from math import factorial
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
# Tests:
test = Solution2()
test.uniquePaths(3,7)