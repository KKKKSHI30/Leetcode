class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.block = self.sum_all()

    def sum_all(self):
        total = 0
        block = []
        for i in range(len(self.nums)):
            total += self.nums[i]
            block.append(total)
        return block


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.block[right]
        else:
            return self.block[right] - self.block[left-1]

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)