# Binary Search Approach
# Time: O(nlogm), n is len(pile), m is maximum banana in a single pile
# Space: O(1)
# 2023.06.21: no
# notes: Binary Search也需要一个变通，而不是直接就可以用，但是大纲是一样的
import math


class Solution:
    def minEatingSpeed(self, piles, H):
        left = 1
        # right is a closed interval, so set it to the maximum value
        right = max(piles)

        # right is a closed interval, so use <= here
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= H:
                # right is a closed interval, so use mid - 1
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, piles, x):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/x)
        return hours








