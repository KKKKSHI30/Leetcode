# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
# notes: recursion， 如果当前是0，直接返回0，因为0没法做开头，如果数字小于26，就index+2重新循环，否则就index+1循环
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
# notes: 这道题的关键是i-1和i-2要分两个case来判断，不能直接加起来，如果有i-1，那就+dp[i-1]，如果有i-2，那就+dp[i-2]
# 而不能单独+1, +2是有问题的
class Solution2:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.31: yes
# notes: 压缩空间方法
class Solution3:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back
# Tests:
test = Solution2()
test.numDecodings(s = "1201234")
test.numDecodings(s = "226")
test.numDecodings(s = "1123")
test.numDecodings(s = "2101")
test.numDecodings(s = '10')
test.numDecodings(s = "12")
test.numDecodings(s = "127")

test.numDecodings("06")

# 2 2 6
# 22 6
# 2 26

#
