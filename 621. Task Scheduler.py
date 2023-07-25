# Math
# Time: O(n)
# Space: O(1)
# 2023.07.20: yes
# notes: 两种情况，第一，most_frequency_element太大， 要确认有几个最大frequency,因为要排到后面，用
# (most_common_frequency-1) * (n+1) + most_common_elements， 或者就是长度更大，取max这两个中的一个
# 最重要的是确认有几个最大frequency
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        element_counts = Counter(tasks)
        most_common_frequency = element_counts.most_common(1)[0][1]
        most_common_elements = len([element for element, frequency in element_counts.items() if
                                frequency == most_common_frequency])
        if len(tasks) > (most_common_frequency-1) * (n+1) + most_common_elements:
            return len(tasks)
        else:
            return (most_common_frequency-1) * (n+1) + most_common_elements

# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.20: yes
# notes: 看消耗了多少idle time，每次只能消耗max_frequencies-1个
class Solution2:
    def leastInterval(self, tasks, n):
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

# Tests:
test = Solution2()
test.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
