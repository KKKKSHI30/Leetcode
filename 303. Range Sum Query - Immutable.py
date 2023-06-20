# Caching Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_nums = [0]
        for i in range(len(nums)):
            self.sum_nums.append(self.sum_nums[i] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sum_nums[right+1] - self.sum_nums[left]



# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)