# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: base case 需要-fee，转移方程也需要-fee即可
# 参考神中神六六归一算法
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case：
# dp[-1][0] = dp[...][0] = 0
# dp[-1][1] = dp[...][1] = -infinity
# 状态转移方程：
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]-fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]

# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
class Solution2(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, float('-inf')-fee
        for i in range(n):
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, dp_i_0 - prices[i] -fee)
        return dp_i_0

# Tests:
test = Solution2()
test.maxProfit(prices = [1,3,2,8,4,9], fee = 2)