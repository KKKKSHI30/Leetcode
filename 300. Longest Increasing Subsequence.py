# Dynamic programming
# Time: O(n^2)
# Space: O(n)
# 2023.06.21: no
from bisect import bisect_left


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# Intelligently Build a Subsequence
# Time: O(n^2)
# Space: O(n)
# 2023.06.21: no
# notes: 建议看https://labuladong.github.io/algo/di-er-zhan-a01c6/dong-tai-g-a223e/dong-tai-g-6ea57/
# 没有证明，但是写的非常清楚，一个array, 从左到右遍历array, 如果新的数比前面的数大，就append到后面，如果比前面的数小
# 就把前面那个数的位置替换掉，最后数组的长度就是最长的array，替换掉的理由是，能用小的，大的也可以用，但是小的不能用大的
# 后续只需要取一个就可以了
class Solution2:
    def lengthOfLIS(self, nums):
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

# Improve With Binary Search
# Time: O(nlgon)
# Space: O(n)
# 2023.06.21: no
# notes: update上面，只是用binary search的方法插入
class Solution3:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


# Tests:
test = Solution()
test.lengthOfLIS([10,9,2,5,3,7,101,18])