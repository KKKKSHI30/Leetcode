class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])

# tips: saving the existed results and find the other parts
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dp = {}
        for i, n in enumerate(nums):
            if target - n in dp:
                return [dp[target - n], i]
            else:
                dp[n] = i
                print(f"dp is {dp}")
        return [-1, -1]


a = Solution2()
a.twoSum([2,7,11,15,3,6],9)
a.twoSum([3,2,4],6)
a.twoSum([3,3],6)