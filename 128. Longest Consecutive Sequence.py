# HashSet and Intelligent Sequence Building Approach (best solution)
# Time: O(n)
# Space: O(n)
# 2023.06.23: no
# notes: 题目要求O(n)，所以sort方法是不行的，但是也能通过，无语
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak







# Tests:
nums = [100,4,200,1,3,2]
test = Solution()
test.longestConsecutive(nums)