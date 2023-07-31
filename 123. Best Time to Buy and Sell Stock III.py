# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# 参考神中神六六归一算法
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case：
# dp[-1][...][0] = dp[...][k][0] = 0
# dp[-1][...][1] = dp[...][k][1] = -infinity
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
class Solution:
    def maxProfit(self, prices):
        max_k = 2
        n = len(prices)
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    # 处理 base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 穷举了 n × max_k × 2 个状态，正确。
        return dp[n - 1][max_k][0]

# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: 世界线收束
# 状态转移方程：
# dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
# dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
# dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
# dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
class Solution2:
    def maxProfit(self, prices):
        dp_i10 = 0
        dp_i11 = float('-inf')
        dp_i20 = 0
        dp_i21 = float('-inf')
        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)
        return dp_i20

# Bidirectional Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: divide and conquer方法，找到左边最大profit，右边profit，合并中间的profit
class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit
