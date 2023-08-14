# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.03: yes
# notes: 同款剪枝方法
from collections import Counter


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

# Backtracking
# Time: O(n!)
# Space: O(n)
# 2023.08.03: yes
# notes: 同款counter方法去重
class Solution2:
    def permuteUnique(self, nums):
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return
            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return results