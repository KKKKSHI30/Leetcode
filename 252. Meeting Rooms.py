# Sorting
# Time: O(nlogn)
# Space: O(1)
# 2023.07.31: yes
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


intervals = [[7,10],[2,4]]
intervals2 = [[0,30],[5,10],[15,20]]
intervals3 = []
test = Solution()
test.canAttendMeetings(intervals)
test.canAttendMeetings(intervals2)
test.canAttendMeetings(intervals3)