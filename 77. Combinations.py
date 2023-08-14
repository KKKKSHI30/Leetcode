# Backtracking
# Time: O(n!/((k-1)!(n-k)!))
# Space: O(n)
# 2023.08.02: yes
# notes: 只需要加一个限制条件即可
class Solution:
    def combine(self, nums, k):
        res = []
        track = []
        def backtrack(start, nums):
            if len(track) == k:
                res.append(list(track))
            for i in range(start, nums+1):
                track.append(i)
                backtrack(i+1, nums)
                track.pop()
        backtrack(1, nums)
        return res

test = Solution()
test.combine(4, 2)
test.combine(1, 1)
test.combine(5, 1)