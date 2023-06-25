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


# Tests:
test = Solution2()
prices = [7,1,5,3,6,4]
prices2 = [4,2,7,3,8,1,9]
prices3 = [7,6,4,3,1]
test.maxProfit(prices)
test.maxProfit(prices2)
test.maxProfit(prices3)


# 官方答案
# 优化版，没必要设置max的
class Solutio2n:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

