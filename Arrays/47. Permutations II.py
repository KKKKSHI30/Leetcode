class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        saving = []
        self.dp(nums, [], saving)
        return saving

    def dp(self, nums, res, saving):
        if not nums:
            saving.append(res[:])
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums.pop(i)
            self.dp(nums, res+[n], saving)
            nums.insert(i, n)

test = Solution()
test.permuteUnique([1,2,2])


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        saving = []
        self.dp(nums,[], saving)
        return saving

    def dp(self, nums, res, saving):
        if not nums:
            saving.append(res)
        for i,n in enumerate(nums):
            nums.pop(i)
            self.dp(nums, res+[n], saving)
            nums.insert(i, n)

test = Solution2()
test.permute([1,2,3])