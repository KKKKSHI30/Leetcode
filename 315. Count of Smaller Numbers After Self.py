class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # record the value and the index
        arr = [[v,i] for i, v in enumerate(nums)]
        results = [0] * n
        # since in merge sort, we use [left, mid), and [mid, right)
        self.merge_sort(arr, 0, n, results)
        return results

    def merge_sort(self, arr, left, right, results):
        # right is not included, so right - left <= 1, closed interval will be right = left
        if right - left <= 1:
            return
        mid = (left+right)//2
        # [left, mid)
        self.merge_sort(arr, left, mid, results)
        # [mid, right), right is not included
        self.merge_sort(arr, mid, right, results)
        self.merge(arr, left, mid, right, results)

    def merge(self, arr, left, mid, right, results):
        i, j = left, mid
        temp = []
        while i < mid and j < right:
            if arr[i][0] <= arr[j][0]:
                results[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i < mid:
            results[arr[i][1]] += j-mid
            temp.append(arr[i])
            i += 1
        while j < right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right):
            arr[i] = temp[i-left]

test = Solution()
test.countSmaller([2,0,1])