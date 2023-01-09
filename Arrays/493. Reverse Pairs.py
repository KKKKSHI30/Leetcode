class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        self.mergesort(nums)
        return self.ans

    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left, right = self.mergesort(nums[:mid]), self.mergesort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        m, n = len(left), len(right)
        while i < m:
            while j < n and left[i] > 2 * right[j]:
                j += 1
            self.ans += j
            i += 1

        i, j = 0, 0
        temp = []
        while i < m and j < n:
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1

        while i < m:
            temp.append(left[i])
            i += 1
        while j < n:
            temp.append(right[j])
            j += 1
        return temp


class Solution2(object):
    def reversePairs(self, nums):
        n = len(nums)
        def merge_sort(nums, low, high):
            if low>=high:
                return 0
            mid = (low+high)//2
            inv = merge_sort(nums, low, mid)
            inv += merge_sort(nums, mid+1, high)
            inv += merge(nums, low, mid, high)
            return inv
        def merge(nums, low, mid, high):
            count = 0
            j = mid+1
            for i in range(low, mid+1):
                while j<=high and nums[i]>2*nums[j]:
                    j += 1
                count += (j-(mid+1))
            temp = []
            left = low
            right = mid+1
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left<=mid:
                temp.append(nums[left])
                left += 1
            while right<=high:
                temp.append(nums[right])
                right += 1
            for i in range(low, high+1):
                nums[i] = temp[i-low]
            return count
        return merge_sort(nums, 0, n-1)

test = Solution2()
test.reversePairs(nums = [2,4,3,5,1])
test.reversePairs([1,3,2,3,1])
