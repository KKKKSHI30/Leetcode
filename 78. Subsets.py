# Backtracking
# Time: O(n*2^n)
# Space: O(n)
# 2023.08.02: yes
# notes:不需要追踪进一个出一个，因为每进一种新状态，就可以加到res里面
class Solution:
    def subsets(self, nums):
        res = []
        track = []
        def backtrack(nums, start):
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1)
                track.pop()
        backtrack(nums, 0)
        return res

test = Solution()
test.subsets(nums = [1,2,3])

# Lexicographic (Binary Sorted) Subsets
# Time: O(n*2^n)
# Space: O(n)
# notes: 太聪明的方法，用bit mask一个个增加就可以了
class Solution2:
    def subsets(self, nums):
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output
