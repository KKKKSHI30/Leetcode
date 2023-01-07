class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                return True
        return False







nums = [1, 2, 3, 1]
test = Solution()
test.containsDuplicate(nums)