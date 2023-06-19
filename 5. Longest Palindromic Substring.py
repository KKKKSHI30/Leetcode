# Expand From Centers Approach (best approach):
# Time: O(n^2)
# Space: O(1)
# 2023.06.18: no
# notes:核心思路，找到以s[i]，s[i]（奇数长度）或者s[i], s[j]（偶数长度）为中心的最长子串
# 实时更新最长子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            s1 = self.parlindrome(s, i, i)
            s2 = self.parlindrome(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

    def parlindrome(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r]

# Check All Substrings
# Time: O(n^3)
# Space: O(1)
# 2023.06.18: yes
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""


# Dynamic Programming Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.18: no
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]


# Tests:
test = Solution()
test.longestPalindrome("babad")
test.longestPalindrome("cbbd")

