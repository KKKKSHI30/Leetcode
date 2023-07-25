# Improved Memoization - Top down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: 用cache或者用memo table存效果一样，两个情况，第一，这个字符匹配，p1, p2都往右一格
# 第二情况，不匹配，p1往右一格，或者p2往右一格，或者都不存在（该情况可以被前两个情况覆盖，不用考虑）
# max(最长子串即可)
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)

# Bottom Up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: 同步上一个方法，只是用的iteration的方法，更清晰一点
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Make a grid of 0's with len(text2) + 1 columns
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]


# Dynamic Programming with Space Optimization
# Time: O(min(m,n))
# Space: O(min(m,n))
# 2023.07.24: no
# notes: 更新最近两行足以，不需要追踪整个2d表
class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous and current column starts with all 0's and like
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous

        # The original problem's answer is in previous[0]. Return it.
        return previous[0]