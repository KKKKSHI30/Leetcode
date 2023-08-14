# Dynamic Programming (其实是brute force fck)
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
# notes: 感觉是dp，实际上brute froce，n^2
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf")
        num_len = len(nums)
        dp = [[0 for _ in range(num_len)] for _ in range(num_len)]
        for i in range(num_len):
            dp[i][i] = nums[i]
            res = max(res, dp[i][i])
        for i in range(num_len):
            for j in range(i+1, num_len):
                dp[i][j] = dp[i][j-1]* nums[j]
                res = max(res, dp[i][j])
        return res

# Dynamic Programming (其实是brute force fck)
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
# notes: 人傻了，这个dp的定义应该是，包括自己为止，到自己节点的最大值是多少，而且负数的话，要记录正负
# 因为一个负号就可以改变大小
class Solution2:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            result = max(max_so_far, result)
        return result

# Tests:
test = Solution()
test.maxProduct([-2])
test.maxProduct([2,3,-2,4])
test.maxProduct([-2,0,-1])

