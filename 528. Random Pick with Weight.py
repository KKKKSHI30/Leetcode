# Prefix Sums with Linear Search Approach
# Time: construction: O(n), pickIndex: O(logn)
# Space: construction: O(n), pickIndex: O(1)
# 2023.06.21: no
import random

class Solution:
    def __init__(self, w):
        n = len(w)
        self.preSum = [0] * (n + 1)
        self.rand = random.Random()
        for i in range(1, n+1):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]

    def pickIndex(self):
        n = len(self.preSum)
        target = self.rand.randint(1, self.preSum[n - 1])
        return self.left_bound(self.preSum, target) - 1

    def left_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid-1
            elif nums[mid] < target:
                left = mid +1
        return left


# Prefix Sums with Linear Search Approach
# Time: construction: O(n), pickIndex: O(n)
# Space: construction: O(n), pickIndex: O(1)
# 2023.06.21: no
class Solution2:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i


obj = Solution([1,3])
a = obj.pickIndex()
obj.pickIndex()
obj.pickIndex()