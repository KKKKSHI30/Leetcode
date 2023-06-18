class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.left_bound(nums, target)
        right = self.right_bound(nums, target)
        return [left, right]

    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        if left == len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1

    def right_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left == 0:
            return -1
        if nums[right] == target:
            return right
        else:
            return -1


test = Solution()
test.searchRange([5, 7, 7, 8, 8, 10], 8)  # [3,4]
