# Approach 1: Find the Exact Value
from bisect import bisect_right, bisect


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:   # <= is because right = len(nums) -1 , is closed interval
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

test = Solution()
test.search([-1,0,3,5,9,12], 9)
test.search([-1,0,3,5,9,12], 2)

# Approach 2: Find Upper bound 左闭右开
class Solution2:
    def search(self, nums, target):
        # Set the left and right boundaries
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1
test = Solution2()
test.search([-1,0,3,5,9,12], -1)
test.search([-1,0,3,5,9,12], 2)

# Approach 3: Find Lower bound 左闭右开
class Solution3:
    def search(self, nums, target):
        # Set the left and right boundaries
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1
test = Solution3()
test.search([-1,0,3,5,9,12], 3)
test.search([-1,0,3,5,9,12], 12)

# Approach 4: Use built-in tools.
class Solution4:
    def search(self, nums, target):
        # Find the insertion position `idx`.
        idx = bisect_right(nums, target)

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1

test = Solution4()
test.search([-1,0,3,5,9,12], 3)
test.search([-1,0,3,5,9,12], 12)