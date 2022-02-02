class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # save the maxCount for comparison
        count = maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount,count)
            else:
                count = 0
        return max(maxCount, count)

ob=Solution()
nums = [1, 1, 0, 1, 1, 1]
results = ob.findMaxConsecutiveOnes(nums)
print(results)












