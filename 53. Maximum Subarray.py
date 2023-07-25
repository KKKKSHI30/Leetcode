# Sliding Window
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: 每次增加一个窗口，如果窗口值小于0，left+1，直到窗口为正，每次right+1的时候，更新窗口
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


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.24: no
# notes: dp[i]代表的是，与自己相连的最大值，所以有两个情况，
# 自成一派最大，和dp[i-1]连在一起最大，取两个中的max即可
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

# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: 因为只会用到dp[i-1]一个元素的值去构建下一个值，所以可以压缩空间到O(1m)
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


class Solution4(object):
    # brute force, not recommended
    def maxSubArray(self, nums):
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray


# Prefix Sum
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: 两个要点，第一，Presum是到这个节点位置的所有数的集合，第二，presum[i]-min(presum[0]-presum[i-1])是最大的子数组
# 我们可以先更新一遍presum再在每次循环的时候，更新min(presum)，同时更新res就可以了
class Solution5(object):
    # 前缀和技巧解题
    def maxSubArray(self, nums):
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0
        # 构造 nums 的前缀和数组
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        res = float('-inf')
        minVal = float('inf')
        for i in range(n):
            # 维护 minVal 是 preSum[0..i] 的最小值
            minVal = min(minVal, preSum[i])
            # 以 nums[i] 结尾的最大子数组和就是 preSum[i+1] - min(preSum[0..i])
            res = max(res, preSum[i + 1] - minVal)
        return res

# Divide and Conquer (Advanced)
# Time: O(nlogn)
# Space: O(logn)
# 2023.07.24: no
# notes: 核心思想是，找到左边最大的，找到右边最大的，找到带着中值最大的
# 左边和右边最大的，可以根据递归进行
# 找中间最大的，就找Mid-1这个点往左，最大值是多少，一定要包含mid-1
# 再找mid+1这个点往右，必须包含mid+1,加上中间点，就是含中间的最大值
# 左右递归完之后，max(左，中，右)即可
class Solution6:
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

test = Solution6()
test.maxSubArray([5,1,-3,4,5,2,1,-5,-5])
test.maxSubArray([-3,-4,-1,-5])
test.maxSubArray([-2,1,-3,4,-1,2,1,-5,-5])

