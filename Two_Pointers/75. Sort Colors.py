class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        cur = 0
        while i < j and cur <= j:
            if nums[cur] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                i += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[j] = nums[j], nums[cur]
                j -= 1
        return nums


nums = [2,0,2,1,1,0]
nums2 = [2,0,1]
nums3 = [1,1,0,0,2,2]
test = Solution()
test.sortColors(nums)
test.sortColors(nums2)
test.sortColors(nums3)





class Solution:
    def sortColors(self, nums):
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


