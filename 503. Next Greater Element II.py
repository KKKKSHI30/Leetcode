# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# notes: 记录序号，环的话，一般用%来解决
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(2*n-1, -1, -1):
            while s and s[-1] <= nums[i%n]:
                s.pop()
            res[i%n] = -1 if not s else s[-1]
            s.append(nums[i%n])
        return res

# Tests:
test = Solution()
test.nextGreaterElements([1,2,1])

