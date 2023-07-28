# notes at top: Same as Q877 dp solution, not the math solution ：）
# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: 有max和min的原因是因为dp的值是差值，如果是first player她想让Pile results最大化
# second player 想让pile results最小化
import collections
from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        memo = collections.defaultdict(int)
        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]
        return maxDiff(0, n - 1) >= 0

# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: 2D iteration的转移方程
# nums[left] - dp[left + 1][right]
# nums[right] - dp[left][right - 1]
class Solution2:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])
        return dp[0][n - 1] >= 0

# Bottom Up 1D Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
class Solution3:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = nums[:]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
        return dp[0] >= 0



# DIFFERENT DYNAMIC PROGRAMMING SOLUTION - 2D REUCRSION - 1D ITERATION
# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: https://www.youtube.com/watch?v=WxpIHvsu1RI
# 讲的非常好，如果选择一边，他就只能选择剩下的second place，然后最大化左或者右
class Solution4:
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
class Solution5():
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
class Solution6():
    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0

