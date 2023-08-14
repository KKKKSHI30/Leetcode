# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.31: yes
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_0, dp_1 = 1, 1
        for i in range(2, n+1):
            dp_2 = dp_0 + dp_1
            dp_0, dp_1 = dp_1, dp_2
        return dp_1

# Fibonacci Number
# Time: O(logn)
# Space: O(1)
# 2023.07.31: no
# notes: 数学公式暂时跳过
import math
class Solution3(object):
    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int((math.pow(phi, n + 1) - math.pow(psi, n + 1)) / sqrt5)



# Tests:
test = Solution2()
test.climbStairs(2)
test.climbStairs(3)
test.climbStairs(4)




