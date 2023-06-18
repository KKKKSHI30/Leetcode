import math
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        windowsum, maxsum = 0, float("-inf")
        while right < len(nums):
            windowsum += nums[right]
            right += 1

            if windowsum > maxsum:
                maxsum = windowsum

            while windowsum < 0:
                windowsum -= nums[left]
                left += 1
        return maxsum

test = Solution()
test.maxSubArray([-2,1,-3,4,-1,2,1,-5,-5])
test.maxSubArray([-3,-4,-1,-5])

class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [nums[0]]
        for i in range(1,n):
            # maximum that end with nums[i]
            dp.append(max(dp[i-1]+nums[i], nums[i]))
        return max(dp)

test = Solution2()
test.maxSubArray([5,1,-3,4,5,2,1,-5,-5])
test.maxSubArray([-3,-4,-1,-5])

class Solution3(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp_0 = nums[0]
        dp_1, res = 0, dp_0
        for i in range(1,n):
            # maximum that end with nums[i]
            dp_1 = max(nums[i], nums[i]+dp_0)
            dp_0 = dp_1
            res = max(res,dp_0)
        return res

test = Solution3()
test.maxSubArray([5,1,-3,4,5,2,1,-5,-5])
test.maxSubArray([-3,-4,-1,-5])


class Solution4:
    # brute force, not recommended
    def maxSubArray(self, nums):
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray


class Solution5:
    def maxSubArray(self, nums):
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

test = Solution5()
test.maxSubArray([5,1,-3,4,5,2,1,-5,-5])
test.maxSubArray([-3,-4,-1,-5])
