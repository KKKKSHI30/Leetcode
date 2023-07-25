# Dynamic Programming Approach
# Time: O(n^3)
# Space: O(n)
# 2023.07.22: yes
# notes: 有一道dp被我做出来了！采用的方法是到dp[i]为止，效率很低
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [0] * (length + 1)
        for i in range(length):
            for j in range(0, i + 1):
                left, right = j, i
                while left < right:
                    if s[left] != s[right]:
                        break
                    else:
                        left += 1
                        right -= 1
                if left >= right:
                    dp[i + 1] += 1
            dp[i + 1] += dp[i]
        return dp[length]


# Dynamic Programming Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.22: no
# notes: 这才是更好的dp，base case是长度为1和2，然后开始往两边扩展，如果可以的话，就继续扩展，不可以的话，就停，之后也不用测
class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        dp = [[False for _ in range(n)] for _ in range(n)]

        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case: double letter substrings
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += 1 if dp[i][i + 1] else 0

        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += 1 if dp[i][j] else 0
        return ans


# Expand Around Possible Centers
# Time: O(n^2)
# Space: O(1)
# 2023.07.22: no
# notes: 最简单的一个方法，也好理解，从任何一个节点开始，i为中心，或者i，i+1为中心作为base case，往两边扩展
class Solution3:
    def countSubstrings(self, s):
        ans = 0
        for i in range(len(s)):
            # odd-length palindromes, single character center
            ans += self.countPalindromesAroundCenter(s, i, i)
            # even-length palindromes, consecutive characters center
            ans += self.countPalindromesAroundCenter(s, i, i + 1)
        return ans

    def countPalindromesAroundCenter(self, ss, lo, hi):
        ans = 0
        while lo >= 0 and hi < len(ss):
            if ss[lo] != ss[hi]:
                break  # the first and last characters don't match!
            # expand around the center
            lo -= 1
            hi += 1
            ans += 1
        return ans


# Tests:
test = Solution3()
test.countSubstrings("abcdcb")
