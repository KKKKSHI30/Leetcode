# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
# notes: 每次找最远的子节点即可
class Solution:
    def jump(self, nums):
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer

# Tests:
test = Solution()
test.jump([2,3,0,1,4])
test.jump([2,3,1,4,4])