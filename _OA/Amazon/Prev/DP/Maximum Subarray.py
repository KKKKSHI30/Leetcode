import math
class Solution:
    def maxSubArray(self, nums) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray


class Solution2:
    def maxSubArray(self, nums) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray
# Greedy method
# divide and conquer
class Solution3:
    def maxSubArray(self, nums) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return -math.inf
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            return max(best_combined_sum, left_half, right_half)
        return findBestSubarray(nums, 0, len(nums) - 1)
