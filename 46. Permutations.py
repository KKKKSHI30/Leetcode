class Solution(object):
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

test = Solution()
test.permute([1,2,3])