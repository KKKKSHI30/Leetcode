import heapq
import random

# Min Heap Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
class Solution(object):
    def findKthLargest(self, nums, k):
        pq = []
        for e in nums:
            heapq.heappush(pq, e)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]

# Sort Approach
# Time: O(nlogn)
# Space: O(logn)
# 2023.06.30: yes
class Solution2:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]

# Quickselect Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: no
class Solution3:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quick_select(left, k)
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            return pivot
        return quick_select(nums, k)

# Counting Sort Approach
# Time: O(n+m)
# Space: O(n)
# 2023.06.30: no
class Solution4:
    def findKthLargest(self, nums, k):
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1

# Tests:
test = Solution3()
test.findKthLargest([1,5,16,12,7,55,27], 4)