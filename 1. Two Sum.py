class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        for i, n in enumerate(nums):
            if (target - n) not in results:
                results[n] = i
            else:
                return [i, results[target -n]]

nums = [2,7,11,15]
target = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
tests = Solution()
tests.twoSum(nums, target)
tests.twoSum(nums2, target2)
tests.twoSum(nums3, target3)
