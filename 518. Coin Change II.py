# Bottom Up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: 这个dp设置真的非常难理解，i代表只用前i中金币到达j金额可以有多少种方法组成方法
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin_len = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(coin_len+1)]
        # dp[i][j] 只使用前i中coins，有j种方法达到金额
        for i in range(1, coin_len+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                # 如果选择拿这个金币
                elif j - coins[i-1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                # 如果选择不拿这个金币，也就是继承上一行的数据
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[coin_len][amount]

# Dynamic Programming with Space Optimization
# Time: O(n)
# Space: O(n)
# 2023.07.25: no
# notes: 继承上一行就是不用变化了
class Solution2:
    def change(self, amount, coins):
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]


# Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: 继承上一行就是不用变化了
class Solution3:
    def change(self, amount, coins):
        def numberOfWays(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)

            return memo[i][amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return numberOfWays(0, amount)

# Tests:
test = Solution()
test.change(amount = 5, coins = [1,2,5])