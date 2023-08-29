# Iteration DP
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: 顺利，dp[i] = max(nums[i] + dp[i-2], dp[i-1])是动态转移方程
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]

# Recursion DP
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
class Solution2:
    def __init__(self):
        self.memo = {}
    def rob(self, nums):
        self.memo = {}
        return self.robFrom(0, nums)
    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0
        # Return cached value.
        if i in self.memo:
            return self.memo[i]
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        # Cache for future use.
        self.memo[i] = ans
        return ans

# Optimized Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: 以为O(n)不错了，忘记其实只需要两个variable了，可以压O(a)
class Solution3:
    def rob(self, nums):
        # Special handling for empty case.
        if not nums:
            return 0
        N = len(nums)
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
        return rob_next

# Tests:
test = Solution()
test.rob([1,2,3,1])
test.rob([2,7,9,3,1])
test.rob([5,30,99,60,5,10])
