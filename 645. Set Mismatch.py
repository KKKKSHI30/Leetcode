# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: 根据index来计数，遇到这个Index就*-1，如果重复遇到了负数的数，就说明是duplicate，如果是正数，说明是没出现的数
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        dup = -1
        for i in range(n):
            # 现在的元素是从 1 开始的
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                # 将索引转换成元素
                missing = i + 1

        return [dup, missing]

# Tests:
test = Solution()
test.findErrorNums([1,2,2,4])