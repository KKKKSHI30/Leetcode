# Double-ended Queue
# Time: O(1)
# Space: O(n)
# 2023.07.07: no
from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.window = deque()
        self.window_sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) >= self.size:
            temp = self.window.popleft()
            self.window_sum -= temp

        self.window.append(val)
        self.window_sum += val
        return self.window_sum/len(self.window)

# Circular Queue with Array
# Time: O(1)
# Space: O(n)
# 2023.07.07: no
class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage2(3)
param_1 = obj.next(1)
param_2 = obj.next(10)
param_3 = obj.next(3)
param_4 = obj.next(5)
param_5 = obj.next(5)