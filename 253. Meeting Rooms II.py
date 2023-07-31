# Chronological Ordering
# Time: O(nlogn)
# Space: O(n)
# 2023.07.29: no
# notes: 这道题的重点是把start和end区分开来排序，把start和end投影到一个线段上，如果遇到start,
# count+=1，遇到end，count-=1，每次只会有一个情况，start/end
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        n = len(intervals)
        begin = [meeting[0] for meeting in intervals]
        end = [meeting[1] for meeting in intervals]
        begin.sort()
        end.sort()
        # Scanning process counter
        count = 0
        # Double pointer technique
        res = 0
        i, j = 0, 0
        while i < n and j < n:
            if begin[i] < end[j]:
                # Scanning to a red point
                count += 1
                i += 1
            else:
                # Scanning to a green point
                count -= 1
                j += 1
            # Record the maximum value during scanning
            res = max(res, count)
        return res


# Chronological Ordering
# Time: O(nlogn)
# Space: O(n)
# 2023.07.29: no
# notes: 思路和上一道题差不多，但是这次每次start都会往前一步，这样就不用考虑res = max(res, count)这句了
# 保证了used_room永远在增加或者平衡，不可能出现减少的情况，就同步了最大值，但是挺难理解的
class Solution2:
    def minMeetingRooms(self, intervals):
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0
        used_rooms = 0
        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0
        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1
            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1
        return used_rooms

# Priority Queues
# Time: O(nlogn)
# Space: O(n)
# 2023.07.29: no
# notes: 思路不同，但是free_room也永远会增多，不会减少，因为每次增加一个，要不不减少，不可能出现减少的情况
# 思路是，根据start排序，然后把end time放到heap中，就可以根据heap的情况考虑要不要增加一个room
class Solution3:
    def minMeetingRooms(self, intervals):

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

# Tests:
test = Solution3()
test.minMeetingRooms([[1,10],[2,7],[3,19],[4,18],[5,16],[6,10],[8,12],[10,20],[11,30]])