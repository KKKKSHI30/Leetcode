# Linear Search Approach
# Time: O(n)
# Space: O(1)
# 2023.06.24: yes
# notes: 先把new interval放进去排列，然后再合并
from bisect import bisect


class Solution(object):
    def temp_insert(self, intervals, newInterval):
        inserted = False
        results = []
        for interval in intervals:
            if newInterval[0] < interval[0] and not inserted:
                results.append(newInterval)
                results.append(interval)
                inserted = True
            else:
                results.append(interval)
        if inserted == False:
            results.append(newInterval)
        return results

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if intervals == [[]] or intervals == []:
            return [newInterval]
        new_array = self.temp_insert(intervals, newInterval)
        results = [new_array[0]]
        new_array.pop(0)
        while new_array:
            if new_array[0][0] <= results[-1][1]:
                results[-1][1] = max(new_array[0][1], results[-1][1])
                new_array.pop(0)
            else:
                results.append(new_array[0])
                new_array.pop(0)
        return results

# Binary Search Approach
# Time: O(n)
# Space: O(1)
# 2023.06.24: no
# notes: 说是bisect其实只是插入的时候用binary search，后面合并还是O(n)啊，意义何在。。。
class Solution2:
    def insert(self, intervals, newInterval):
        # O(logN)
        position = bisect.bisect(intervals, newInterval)
        # O(N)
        intervals.insert(position, newInterval)

        answer = []
        # O(N)
        for i in range(len(intervals)):
            if not answer or intervals[i][0] > answer[-1][1]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])

        return answer


# Tests:
test = Solution()
# test.temp_insert([[1,5]], [6,8])
test.insert(intervals=[[1,5]], newInterval=[6,8])
test.insert(intervals=[], newInterval=[5,7])
test.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
test.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [3,8])
test.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,5])








