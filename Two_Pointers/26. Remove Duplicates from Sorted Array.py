class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        change_pointer = 1
        i = 0
        while change_pointer < length:
            if nums[i] == nums[change_pointer]:
                change_pointer += 1
            else:
                i += 1
                nums[i] = nums[change_pointer]
                change_pointer += 1
        return i + 1

test = Solution()
a = test.removeDuplicates([0,0,1,1,2,3])




