# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: 核心思想是把线段放到heap中，每次pop最大的半个线段，如果加人，就把当前线段pop出来，再加两个子线段
# 如果是leave，就把这两个边界的线段合并
import heapq
class ExamRoom:

    def dist(self, x, y):  # length of the interval (x, y)
        if x == -1:  # note here we negate the value to make it maxheap
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x - y) // 2)

    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap

    def seat(self):
        _, x, y = heapq.heappop(self.pq)  # current max interval
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p):
        head = tail = None
        for interval in self.pq:  # interval is in the form of (d, x, y)
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(n)
param_1 = obj.seat()
obj.leave(p)