# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: 用的是^的方法，a^a = 0, a^0 = a，这道题其他方法都是常规方法，加加减减，sum等去除
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

# Tests:
test = Solution()
test.singleNumber([4,1,2,1,2])
