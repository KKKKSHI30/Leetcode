# Time Stamp Approach:
# Time: O(nlogn)
# Space: O(n)
# 2023.06.19: yes
class Solution2:
    def carPooling(self, trips, capacity):
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

# Bucket Sort Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
# notes: 只需要检查变化中的内容就可以了，不需要整个1000个都检查
class Solution3:
    def carPooling(self, trips, capacity):
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff_arr = [0] * 1001
        result_arr = [0] * 1001
        for trip in trips:
            passenger, start, end = trip
            diff_arr[start] += passenger
            if end < len(diff_arr):
                diff_arr[end] -= passenger
            for i in range(len(diff_arr)):
                result_arr[i] = result_arr[i-1] + diff_arr[i]
                if result_arr[i] > capacity:
                    return False
        return True

test = Solution()
test.carPooling([[2,1,5],[3,3,7]], 4)
test.carPooling([[2,1,5],[3,3,7]], 5)
test.carPooling([[9,0,1],[3,3,7]], 4)
