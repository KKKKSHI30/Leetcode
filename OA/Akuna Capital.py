import copy
from heapq import heappush


def getMincost(n, k, plans):
    result = 0
    plans = sorted(plans, key=lambda x: x[-1], reverse=True)
    original_plan = copy.deepcopy(plans)
    for i in range(1, n+1):
        cur_k = k
        heap = copy.deepcopy(original_plan)
        while cur_k > 0:
            cur_plan = heap.pop()
            if i >= cur_plan[0] and i <= cur_plan[1]:
                if cur_plan[2] >= cur_k:
                    result += cur_k * cur_plan[3]
                    cur_k = 0
                else:
                    cur_k -= cur_plan[2]
                    result += cur_plan[2]* cur_plan[3]
    return result



n = 5
k = 7
plans = [[1,3,5,2], [1,4,5,3], [2,5,10,1]]
getMincost(n, k, plans)