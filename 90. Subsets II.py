class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(first, curr):
            output.append(curr[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        nums = sorted(nums)
        backtrack(0,[])
        return output

test = Solution()
test.subsetsWithDup([1,2,2,3])
test.subsetsWithDup([4,4,4,1,4])

class Solution2:
    def subsetsWithDup(self, nums):
        res, pos, nums = [[]], {}, sorted(nums)
        for n in nums:
            frm, ln = pos.get(n, 0), len(res)
            for ls in res[frm:]:
                res.append(ls + [n])
            pos[n] = ln
        return res

test = Solution2()
test.subsetsWithDup([1,2,2,2,3,3])