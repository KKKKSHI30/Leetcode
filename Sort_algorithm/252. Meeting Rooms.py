class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals) -1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


intervals = [[7,10],[2,4]]
intervals2 = [[0,30],[5,10],[15,20]]
intervals3 = []
test = Solution()
test.canAttendMeetings(intervals)
test.canAttendMeetings(intervals2)
test.canAttendMeetings(intervals3)