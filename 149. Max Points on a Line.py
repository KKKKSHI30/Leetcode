# Math
# Time: O(n^2)
# Space: O(n)
# 2023.07.22: no
# notes: 利用arctan的方法，确认两个点之间的角度，角度相同即在一条线上
import collections
import math


class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result

# Tests:
test = Solution()
test.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])