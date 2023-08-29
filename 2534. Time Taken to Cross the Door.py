# Queue
# Time: O(n)
# Space: O(1)
# 2023.08.18: yes
# notes: 有些情况可以合并，比如初始化可以为1，小于当前时间的都可以放进去，看上去是double loop，实际上O(n)
from collections import deque

class Solution:
    def timeTaken(self, arrival, state):
        enter_pool, exit_pool = deque(),deque()
        cur_time = 0
        prev_state = 1
        i = 0
        ans = [0 for _ in range(len(arrival))]
        while i < len(arrival) or enter_pool or exit_pool:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1
            if prev_state == 1:
                if exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                elif enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                    prev_state = 0
            else:
                if enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                elif exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                    prev_state = 1
                else:
                    prev_state = 1
            cur_time += 1
        return ans

# Tests:
test = Solution()
test.timeTaken(arrival = [0,1,1,2,4], state = [0,1,0,0,1])