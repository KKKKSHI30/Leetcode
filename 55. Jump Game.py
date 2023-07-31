# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
# notes: for loop找最大，太简单了，无特别
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_length = nums[0]
        n = len(nums)
        for i in range(n):
            if max_length < i:
                return False
            if nums[i] + i > max_length:
                max_length = nums[i] + i
        return max_length >= n-1

# Dynamic Programming Top-down
# Time: O(n^2)
# Space: O(n)
# 2023.07.29: no
# notes: 超时，但是思路可以借鉴，遇到一个点就找到他最远的点，把路径上的所有点都递归一次，找到更远的
# 如果遇到了更远的返回的时候一路标记good，不然的话就是bad了，因为不需要这些点也可以返回最远的距离
from enum import Enum

class Index(Enum):
    GOOD = 0
    BAD = 1
    UNKNOWN = 2

class Solution2:
    def canJumpFromPosition(self, position, nums, memo):
        if memo[position] != Index.UNKNOWN:
            return memo[position] == Index.GOOD

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums, memo):
                memo[position] = Index.GOOD
                return True

        memo[position] = Index.BAD
        return False

    def canJump(self, nums):
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD
        return self.canJumpFromPosition(0, nums, memo)

# Dynamic Programming Top-down
# Time: O(n)
# Space: O(1)
# 2023.07.29: no
# notes: 勉强不超时，recursion的dp写法，逆推
class Solution3:
    def canJump(self, nums):
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD

        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break
        return memo[0] == Index.GOOD


# Tests:
test = Solution3()
test.canJump([2,3,1,1,4])
test.canJump([3,2,1,0,4])
test.canJump([0])
test.canJump([2,0,0])


# Backtracking
# Time: O(2^n)
# Space: O(n)
# 2023.07.29: no
# notes: 2^n超大时
class Solution4:
    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums):
                return True

        return False

    def canJump(self, nums):
        return self.canJumpFromPosition(0, nums)





