# Binary Search Approach
# Time: O(nlogm), n is len(pile), m is maximum banana in a single pile
# Space: O(1)
# 2023.06.22: no
# notes: 几个点，left, right的值，判断的的时候的大小于号，f function怎么写
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # left就是至少每次要送一箱
        # right的情况就是一次送完，所以就是所有的和
        left, right = 0, 0
        for w in weights:
            left = max(left, w)
            right += w

        while left <= right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid -1
            else:
                left = mid + 1
        return left

    def f(self, weights, capacity):
        days = 0
        pos = 0
        while pos < len(weights):
            cap = capacity
            while pos < len(weights):
                if cap < weights[pos]:
                    break
                else:
                    cap -= weights[pos]
                    pos += 1
            days += 1
        return days


# Tests:
test = Solution()
test.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)