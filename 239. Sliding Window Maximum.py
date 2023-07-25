# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# notes: 构建一个单调栈从大到小，如果当前值和单调栈第一个一样，那就压出，后续往单调栈里压的时候，如果比最后一个值大，
# 就弹出最后一个值，直到当前值比最后一个值小才能压入，以此类推
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        res = []
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i-k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        return res

# Tests:
test = Solution()
test.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
