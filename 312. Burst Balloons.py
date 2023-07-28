# Bottom Up Dynamic Programming (超时)
# Time: O(n^3)
# Space: O(n^2)
# 2023.07.27: no
# notes: dp[left][right] = x 表示，戳破气球left和气球right之间(开区间，不包括left和right)的所有气球，可以获得的最高分数为 x
# // 最后戳破的气球是哪个最佳，在left和right中遍历找到最佳，下面两种就是一样的写法不同
# for (int k = i + 1; k < j; k++) {
#     // 择优做选择，使得 dp[i][j] 最大
#     dp[i][j] = Math.max(
#         dp[i][j],
#         dp[i][k] + dp[k][j] + points[i]*points[j]*points[k]
#     );
# }
# for i in range(left, right + 1):
#     gain = nums[left - 1] * nums[i] * nums[right + 1]
#     remaining = dp[left][i - 1] + dp[i + 1][right]
#     dp[left][right] = max(remaining + gain, dp[left][right])
from functools import lru_cache
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        # Add two virtual balloons on both ends
        points = [1] + nums + [1]
        # Initialize dp table with 0s
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        # Start state transition
        # i should go from bottom to top
        for i in range(n, -1, -1):
            # j should go from left to right
            for j in range(i + 1, n + 2):
                # Find the last balloon to burst in the range (i, j)
                for k in range(i + 1, j):
                    # Choose the optimal decision
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + points[i] * points[j] * points[k]
                    )
        return dp[0][n + 1]

# notes: 和上面一摸一样的方法，只是边界不同
# remaining是指，除了这个点，他的左右两边加起来和他一起的最大值才是当前气球的最大值
class Solution2:
    def maxCoins(self, nums):
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] represents
        # maximum if we burst all nums[left]...nums[right], inclusive
        dp = [[0] * n for _ in range(n)]

        # do not include the first one and the last one
        # since they are both fake balloons added by ourselves and we can not
        # burst them
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                # find the last burst one in nums[left]...nums[right]
                for i in range(left, right + 1):
                    # nums[i] is the last burst one
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    # recursively call left side and right side
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    # update
                    dp[left][right] = max(remaining + gain, dp[left][right])
        # burst nums[1]...nums[n-2], excluding the first one and the last one
        return dp[1][n - 2]


# Dynamic Programming (Top-Down)
# Time: O(n^3)
# Space: O(n^2)
# 2023.07.27: no
# notes: Top-down引出的solution2
class Solution3:
    def maxCoins(self, nums):
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        nums = [1] + nums + [1]

        @lru_cache(None)  # memoization
        def dp(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            return result

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)






# Tests:
test = Solution()
test.maxCoins(nums = [3,1,5,8])