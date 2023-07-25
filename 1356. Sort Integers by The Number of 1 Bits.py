# Array Approach
# Time: O(1)
# Space: O(1)
# 2023.07.18: yes
import heapq


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))

class Solution2(object):
    def sortByBits(self, arr):
        res = []
        for num in arr:
            ones = self.countBits(num)
            res.append((ones, num))
        heapq.heapify(res)
        finalres = []
        while len(res) > 0:
            finalres.append(heapq.heappop(res)[1])
        return finalres

    def countBits(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

# Tests:
test = Solution2()
test.sortByBits([0,1,2,3,4,5,6,7,8])