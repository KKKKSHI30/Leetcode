import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = sys.maxsize
        for i in range(len(coins)):
            subproblem = self.dp(coins, amount - coins[i])
            if subproblem == -1:
                continue
            res = min(res, subproblem+1)
        if res == sys.maxsize:
            return -1
        else:
            return res

test = Solution()
test.coinChange([2,5], 11)

class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.saving = [-30] * (amount+1)
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if self.saving[amount] != -30:
            return self.saving[amount]
        res = sys.maxsize
        for i in range(len(coins)):
            subproblem = self.dp(coins, amount - coins[i])
            if subproblem == -1:
                continue
            res = min(res, subproblem + 1)
        if res == sys.maxsize:
            self.saving[amount] = -1
        else:
            self.saving[amount] = res
        return self.saving[amount]

test = Solution2()
test.coinChange([2,5], 11)

class Solution3(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        saving = [amount+1] * (amount + 1)
        saving[0] = 0
        for i in range(len(saving)):
            for j in range(len(coins)):
                if i - coins[j] < 0:
                    continue
                saving[i] = min(saving[i], 1 + saving[i-coins[j]])
        if saving[amount] == amount +1:
            return -1
        else:
            return saving[amount]

test = Solution3()
test.coinChange([2,5], 11)