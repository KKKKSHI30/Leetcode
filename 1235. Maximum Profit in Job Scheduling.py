# Top-Down Dynamic Programming + Binary Search Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: 根据sort 和bianry search确定下一个最近的点是什么， 通过top-down dp来确定要不要选择这个点
from bisect import bisect_left
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = []
        memo = [-1] * (len(profit) + 1)

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()
        start = [job[0] for job in jobs]

        def findMaxProfit(position):
            if position == len(profit):
                return 0
            if memo[position] != -1:
                return memo[position]

            nextIndex = bisect_left(start, jobs[position][1])

            maxProfit = max(findMaxProfit(position + 1),
                            jobs[position][2] + findMaxProfit(nextIndex))

            memo[position] = maxProfit
            return maxProfit

        return findMaxProfit(0)



# Bottom-Up Dynamic Programming + Binary Search Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: 和前面略有不同，从右往左，实时更新到这个节点的最高profit继续往左即可
class Solution2:
    def findMaxProfit(self, startTime, jobs):
        length = len(startTime)
        memo = [0] * (length + 1)

        for position in range(length - 1, -1, -1):
            currProfit = 0

            nextIndex = bisect_left(startTime, jobs[position][1])

            if nextIndex != length:
                currProfit = jobs[position][2] + memo[nextIndex]
            else:
                currProfit = jobs[position][2]

            if position == length - 1:
                memo[position] = currProfit
            else:
                memo[position] = max(currProfit, memo[position + 1])

        return memo[0]

    def jobScheduling(self, startTime, endTime, profit):
        jobs = []

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()

        startTime = [job[0] for job in jobs]

        return self.findMaxProfit(startTime, jobs)


# Sorting + Priority Queue Approach (best approach)
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: 太聪明的方法，利用heap考虑到到这个节点前所有可能性的最大利益，直接加上去考虑最大值，最后结尾也一样，把所有节点结合就可
import heapq

class Solution3:
    def findMaxProfit(self, jobs):
        n = len(jobs)
        maxProfit = 0
        pq = []  # min heap having [endTime, profit]

        for i in range(n):
            start, end, profit = jobs[i][0], jobs[i][1], jobs[i][2]

            # keep popping while the heap is not empty and
            # jobs are not conflicting
            # update the value of maxProfit
            while pq and start >= pq[0][0]:
                maxProfit = max(maxProfit, pq[0][1])
                heapq.heappop(pq)

            # push the job with combined profit
            # if no non-conflicting job is present maxProfit will be 0
            heapq.heappush(pq, [end, profit + maxProfit])

        # update the value of maxProfit by comparing with
        # profit of jobs that exist in the heap
        while pq:
            maxProfit = max(maxProfit, pq[0][1])
            heapq.heappop(pq)

        return maxProfit

    def jobScheduling(self, startTime, endTime, profit):
        jobs = []

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()
        return self.findMaxProfit(jobs)



# Tests:
test = Solution3()
test.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])
test.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])