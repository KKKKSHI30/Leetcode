# Dynamic Programming 1D recursion
# Time: O(mn)
# Space: O(m)
# 2023.07.27: no
from functools import lru_cache
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True

# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: 有max和min的原因是因为dp的值是差值，如果是first player她想让Pile results最大化
# second player 想让pile results最小化
# dp是差值
class Solution2:
    def stoneGame(self, piles):
        N = len(piles)
        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0


# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: https://www.youtube.com/watch?v=WxpIHvsu1RI
# 讲的非常好，如果选择一边，他就只能选择剩下的second place，然后最大化左或者右
class Solution3:
    def stoneGame(self, piles):
        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return (0, 0)
            pickLeft = dp(left + 1, right)
            pickRight = dp(left, right - 1)
            if piles[left] + pickLeft[1] > piles[right] + pickRight[1]:
                # If the left choice has higher score than the right choice
                return piles[left] + pickLeft[1], pickLeft[0]  # then pick left
            return piles[right] + pickRight[1], pickRight[0]  # else pick right

        alexScore, leeScore = dp(0, len(piles) - 1)
        return alexScore > leeScore

# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: 根据solution3改编，斜向遍历
class Solution4():
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0

# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n)
# 2023.07.27: no
# notes: 根据solution4进行压缩空间
class Solution5:
    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0

# Tests:
test = Solution3()
test.stoneGame([5,3,4,5])