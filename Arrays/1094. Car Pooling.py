class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        block = [0 for _ in range(1001)]
        for i in range(len(trips)):
            numPassengers, from_pos, to_pos = trips[i]
            for j in range(from_pos, to_pos):
                if block[j] + numPassengers > capacity:
                    return False
                else:
                    block[j] += numPassengers
        return True

class Solution2(object):
    def carPooling(self, trips, capacity):
        self.trips = trips
        difference_block = self.difference()
        ori_block = [0 for _ in range(1002)]
        for i in range(len(difference_block)):
            ori_block[i] = ori_block[i-1] + difference_block[i]
            if ori_block[i] > capacity:
                return False
        return True

    def difference(self):
        block = [0 for _ in range(1001)]
        for i in range(len(self.trips)):
            numPassengers, from_pos, to_pos = self.trips[i]
            block[from_pos] += numPassengers
            block[to_pos] -= numPassengers
        return block

class Solution3:
    # split the trips into a sublist and sort to check
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

class Solution4:
    # similar as my way, but very easy code
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

test = Solution3()
test.carPooling([[9,0,1],[3,3,7]], 4)
test.carPooling([[2,1,5],[3,3,7]], 4)
test.carPooling([[2,1,5],[3,3,7]], 5)
