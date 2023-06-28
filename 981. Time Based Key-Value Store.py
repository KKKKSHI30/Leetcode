# Hashmap + Linear Search Approach
# Time: O(m*l),O(l) is the time to hash the string, O(m) is is number of cells
# Space: O(n*timestamp*l)
# 2023.06.25: no
# notes: 以key作为一个新的dictionary的名字，然后value和timestamp作为value和新key,获取的时候，现看有没有元素，
# 有的话从大到小遍历就可以，因为一定会降到最小
class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = {}

        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""

        # Iterate on time from 'timestamp' to '1'.
        for curr_time in reversed(range(1, timestamp + 1)):
            # If a value for current time is stored in key's bucket we return the value.
            if curr_time in self.key_time_map[key]:
                return self.key_time_map[key][curr_time]

        # Otherwise no time <= timestamp was stored in key's bucket.
        return ""


# Sorted Map + Binary Search Approach
# Time: O(m*l*logm),O(l) is the time to hash the string, O(m) is is number of cells
# Space: O(m*l)
# 2023.06.25: no
# notes: 两个built in，SortedDict和bisect.bisect_right
from sortedcontainers import SortedDict
class TimeMap2:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = SortedDict()

        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""

        it = self.key_time_map[key].bisect_right(timestamp)
        # If iterator points to first element it means, no time <= timestamp exists.
        if it == 0:
            return ""

        # Return value stored at previous position of current iterator.
        return self.key_time_map[key].peekitem(it - 1)[1]

# Array + Binary Search Approach
# Time: O(m*l*logm),O(l) is the time to hash the string, O(m) is is number of cells
# Space: O(m*l)
# 2023.06.25: no
# notes: 重点是"All the timestamps of set are strictly increasing"，所以放进去的顺序一定是sorted，可以直接binary search
class TimeMap3:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = []

        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""

        if timestamp < self.key_time_map[key][0][0]:
            return ""

        left = 0
        right = len(self.key_time_map[key])

        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.key_time_map[key][right - 1][1]



# Tests:
timeMap = TimeMap3()
timeMap.set("foo", "bar", 3)
timeMap.get("foo", 2)
timeMap.get("foo", 3)
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)
timeMap.get("foo", 5)