class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        minimum = prices[0]
        maximum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
                maximum = prices[i]
            if prices[i] > maximum:
                maximum = prices[i]
                result = max(result, maximum - minimum)
        return result

test = Solution()
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

