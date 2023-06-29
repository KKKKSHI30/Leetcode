# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: double loop + recursion在prefix sum上
class Solution:
    def countRangeSum(self, nums, lower, upper):
        self.lower = lower
        self.upper = upper
        preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            preSum[i + 1] = nums[i] + preSum[i]
        self.count = 0
        self.sort(preSum)
        return self.count

    def sort(self, nums):
        self.temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.mergeSort(nums, lo, mid)
        self.mergeSort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        start = mid + 1
        end = mid + 1
        for i in range(lo, mid + 1):
            while start <= hi and nums[start] - nums[i] < self.lower:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.upper:
                end += 1
            self.count += end - start

        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1

# Tests:
test = Solution()
test.countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2)