# Binary Search Approach (best approach)
# Time: O(logn)
# Space: O(1)
# 2023.06.25: yes
# notes: 因为解一定存在，然后注意的点事left = mid和right = mid
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return nums[0]



# Tests:
test = Solution()
test.findMin([3,1,2])
test.findMin([1])
test.findMin([11,13,15,17])
test.findMin(nums = [3,4,5,1,2])
test.findMin([4,5,6,7,0,1,2])
