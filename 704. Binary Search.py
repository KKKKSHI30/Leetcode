# Find the Exact Value Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: yes
from bisect import bisect_right

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right: # <= is because right = len(nums) -1 , is closed interval
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid-1
        return -1

# Find Lower bound Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
# notes: 重点是考虑结束的情况，边界情况
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid-1
            elif nums[mid] < target:
                left = mid +1
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1

# Find Upper bound Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] <= target:
                left = mid +1
        # right = left -1
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1


# Use built-in tools Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
class Solution4:
    def search(self, nums, target):
        idx = bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1

# Tests:
test = Solution4()
test.search([-1,0,3,3,3,5,9,12], 3)
test.search([-1,0,3,5,9,12], 9)
