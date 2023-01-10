class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        slow, fast = 0, 0
        for i in range(length):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for j in range(slow, length):
            nums[j] = 0
        return nums

test = Solution()
a = test.moveZeroes([1,2,0,3,2,0])
b = test.moveZeroes([0,0,1])
c = test.moveZeroes([0])