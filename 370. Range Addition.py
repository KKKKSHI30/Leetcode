# Range Caching Approach (best approach):
# Time: O(1)
# Space: O(mn)
# 2023.06.19: yes
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0]*length
        for update in updates:
            start, end, inc = update
            arr[start] += inc
            if end+1  < len(arr):
                arr[end+1] -= inc
        return_arr = [0]*length
        for i in range(len(arr)):
            return_arr[i] = return_arr[i-1] + arr[i]
        return return_arr

test = Solution()
test.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
test.getModifiedArray(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])
