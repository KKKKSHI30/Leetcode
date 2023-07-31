# Dynamic Programming
# Time: O(nlogn)
# Space: O(nlogn)
# 2023.07.29: yes
# notes: 贪心算法，根本想不到，先根据end的时间进行排序，如果当前节点的开始早于前一个的结束时间，代表需要移除
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(lambda x: x[1])
        ans = 0
        k = float('-inf')
        for start, end in intervals:
            if start >= k:
                k = end
            else:
                ans += 1
        return ans

