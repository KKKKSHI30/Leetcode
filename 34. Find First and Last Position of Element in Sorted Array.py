# Find Lower bound Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: yes
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        return [left, right]

    def search_left(self, nums, target):
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

    def search_right(self, nums, target):
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
        # right == left -1
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1


# Tests:
test = Solution()
test.searchRange([5, 7, 7, 8, 8, 10], 8)  # [3,4]