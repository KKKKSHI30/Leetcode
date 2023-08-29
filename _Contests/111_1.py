class Solution:
    def countPairs(self, nums, target):
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    result+=1
        return result

# Tests:
test = Solution()
test.countPairs(nums = [-1,1,2,3,1], target = 2)
test.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)
