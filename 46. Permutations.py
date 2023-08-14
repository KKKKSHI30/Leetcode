# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: yes
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        num_length = len(nums)
        def rec(nums, cur):
            if len(cur) == num_length:
                results.append(cur[:])
                return
            for i in range(len(nums)):
                tmp = nums.pop(i)
                cur.append(tmp)
                rec(nums, cur)
                cur.pop()
                nums.insert(i, tmp)
        rec(nums,[])
        return results

test = Solution()
test.permute([1,2,3])