# brute force Approach
# Time: O(n^2)
# Space: O(1)
# 2023.06.23: yes
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# one pass Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: no
class Solution2:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: 六六归一，记得看
# 太强了，真的，我愿称为神
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case：
# dp[-1][0] = 0
# dp[-1][1] = -infinity
# 状态转移方程：
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], - prices[i])
class Solution4(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i-1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]

# Dynamic Programming Space Optimized
# Time: O(n)
# Space: O(1)
# 2023.07.28: no
class Solution5(object):
    def maxProfit_k_1(self, prices):
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, -prices[i])
        return dp_i_0


# Tests:
test = Solution4()
prices = [7,1,5,3,6,4]
prices2 = [4,2,7,3,8,1,9]
prices3 = [7,6,4,3,1]
test.maxProfit(prices)
test.maxProfit(prices2)
test.maxProfit(prices3)













