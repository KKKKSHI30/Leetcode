# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res

# Sum up
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
class Solution2:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Tests:
test = Solution()
test.missingNumber([3,0,1])