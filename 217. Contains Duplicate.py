# Sorting Approach
# Time: O(nlogn)
# Space: O(1)
# 2023.06.23: yes
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False

# Hash Table Approach
# Time: O(n)
# Space: O(n)
# 2023.06.23: yes
class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        contains = set()
        for i in range(len(nums)):
            if nums[i] not in contains:
                contains.add(nums[i])
            else:
                return True
        return False

# Tests:
nums = [1, 2, 3, 1]
test = Solution2()
test.containsDuplicate(nums)