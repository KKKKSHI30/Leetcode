# One-pass Hash Table Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.23: yes
# notes: 其他两种，一个brute force ，一个two pass hash table没必要，不放了，太蠢了
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        for i in range(len(nums)):
            if target-nums[i] not in results:
                results[nums[i]] = i
            else:
                return [results[target-nums[i]], i]


# Tests:
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
