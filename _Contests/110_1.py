class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        last_digit = purchaseAmount%10
        if last_digit < 5:
            return 100 - purchaseAmount//10*10
        else:
            return 100 - (purchaseAmount//10+1)*10

# Tests:
test = Solution()
test.accountBalanceAfterPurchase(9)
test.accountBalanceAfterPurchase(15)
test.accountBalanceAfterPurchase(29)
