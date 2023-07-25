# Dynamic programming - Top down
# Time: O(sn)
# Space: O(s)
# 2023.06.21: no
# notes: 状态转移方程：
# dp = 0, n = 0
#    = -1, n < 0
#    = min(dp(n-coin) + 1)
from functools import lru_cache
class Solution:
    def coinChange(self, coins, amount):
        memo = [-666] * (amount + 1)
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if memo[rem] != -666:
                return memo[rem]
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            memo[rem] = -1 if min_cost == float('inf') else min_cost
            return memo[rem]
        return dfs(amount)

# Dynamic programming - Bottom up
# Time: O(sn)
# Space: O(n)
# 2023.06.21: no
# notes: 都是bottom up, 第一个是根据先amount再分类金币，另一个是先金币再amount更新
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] == float("inf") else dp[amount]


class Solution3:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # Tests:
test = Solution2()
test.coinChange(coins = [2], amount = 3)
test.coinChange(coins = [1,2,5], amount = 11)

