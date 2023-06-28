# Binary Search Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: yes
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(i):
                right = mid-1
            else:
                left = mid + 1
        return left if isBadVersion(i) else left-1
