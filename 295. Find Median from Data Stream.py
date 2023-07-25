# Monotonic Stack Approach (best approach)
# Time: O(logn)
# Space: O(n)
# 2023.07.17: yes
# notes: 有两个要点，第一，大小根堆，第二，大根堆的栈顶元素要小于小根堆的栈顶
from heapq import *
class MedianFinder(object):
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2
        else:
            return float(self.large[0])

# Sorting Approach (not good)
# Time: O(nlogn)
# Space: O(n)
# 2023.07.17: yes
# notes: 相当于brute force，尽量不要
import bisect

class MedianFinder2:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        bisect.insort(self.store, num)

    def findMedian(self):
        n = len(self.store)
        if n % 2 == 1:
            return self.store[n // 2]
        else:
            mid = n // 2
            return (self.store[mid - 1] + self.store[mid]) / 2.0

# Insertion Sort Approach (not good)
# Time: O(n)
# Space: O(n)
# 2023.07.17: no
import bisect
class MedianFinder3:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort_left(self.store, num)

    def findMedian(self):
        n = len(self.store)
        if n % 2 == 1:
            return self.store[n // 2]
        else:
            mid = n // 2
            return (self.store[mid - 1] + self.store[mid]) / 2.0

# Tests:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.findMedian()