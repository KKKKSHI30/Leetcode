# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.07.15: yes
# notes: 记录序号
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res

# Monotonic Stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# 记录序号和值
class Solution2:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer

# Array, Optimized Space
# Time: O(n)
# Space: O(n)
# 2023.07.15: no
# 甚是复杂，不推荐吧
class Solution3:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        hottest = 0
        answer = [0] * n

        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue

            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer

# Tests:
test = Solution3()
test.dailyTemperatures([73,74,75,71,69,72,76,73])

