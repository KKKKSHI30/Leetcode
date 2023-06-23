# Binary Search Approach (best approach)
# Time: O(NlogS)
# Space: O(1)
# 2023.06.22: yes
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # left: 一次必须至少包含最大值
        # right: 一次必须包含所有值
        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num
        while left <= right:
            mid = left + (right - left)//2
            if self.f(nums, mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, nums, largest_sum_limit):
        num_arrays = 0
        pos = 0
        while pos < len(nums):
            limit = largest_sum_limit
            while pos < len(nums):
                if limit < nums[pos]:
                    break
                else:
                    limit -= nums[pos]
                    pos += 1
            num_arrays += 1
        return num_arrays



# Top-Down Dynamic Programming
# Time: O(n^2*m)
# Space: O(mn)
# 2023.06.22: no
import functools
import itertools

class Solution2:
    def splitArray(self, nums, m):
        n = len(nums)

        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))

        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]

            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum,
                                        get_min_largest_split_sum(i + 1, subarray_count - 1))

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                if first_split_sum >= minimum_largest_split_sum:
                    break

            return minimum_largest_split_sum

        return get_min_largest_split_sum(0, m)


# Bottom-Up Dynamic Programming
# Time: O(n^2*m)
# Space: O(mn)
# 2023.06.22: no
class Solution3:
    def splitArray(self, nums, m):
        n = len(nums)
        memo = [[0] * (m + 1) for _ in range(n)]

        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))

        for subarray_count in range(1, m + 1):
            for curr_index in range(n):
                # Base Case: If there is only one subarray left, then all of the remaining numbers
                # must go in the current subarray. So return the sum of the remaining numbers.
                if subarray_count == 1:
                    memo[curr_index][subarray_count] = prefix_sum[n] - prefix_sum[curr_index]
                    continue

                # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
                # between curr_index and the end of the array with subarray_count subarrays remaining.
                minimum_largest_split_sum = prefix_sum[n]
                for i in range(curr_index, n - subarray_count + 1):
                    # Store the sum of the first subarray.
                    first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                    # Find the maximum subarray sum for the current first split.
                    largest_split_sum = max(first_split_sum, memo[i + 1][subarray_count - 1])

                    # Find the minimum among all possible combinations.
                    minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                    if first_split_sum >= minimum_largest_split_sum:
                        break

                memo[curr_index][subarray_count] = minimum_largest_split_sum

        return memo[0][m]

# Tests:
test = Solution3()
test.splitArray(nums = [7,2,5,10,8], m = 2)
test.splitArray(nums = [1,2,3,4,5], m = 2)
