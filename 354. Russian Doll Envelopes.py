# Sort + Longest Increasing Subsequence
# Time: O(nlogn)
# Space: O(n)
# 2023.06.21: no
# notes: 按照宽度排序之后，直接用LIS的方法排序高度就可以得出结果了
from bisect import bisect_left
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        return lis([i[1] for i in envelopes])


# Tests:
test = Solution()
test.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])


