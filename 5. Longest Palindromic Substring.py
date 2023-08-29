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
# notes: 08.15 update:
# 计算的是i到i位置上最长的回文串，如果是回文，就是True,否则False
# 两个base case， i-i，自己是回文； i-i+1，相邻两个是不是回文
# 之后都是根据这两个展开
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



# Manacher's Algorithm
# R拓宽的最远， C中心点
# 1. i的位置在R之外->暴力扩
# 2. a. i的回文位置在R之内，和i'一样，i'就是以C为中心i的对应点
# 2. b. i的回文位置在R之外，R-i就是长度，否则C就可以往外扩了
# 2. c. i的回文正好压在R，L的线上，不知道L的左边是什么了->暴力扩
class Solution4:
    def longestPalindrome(self, s: str) -> str:
        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        for i in range(n):
            mirror = 2 * center - i
            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])
            while (i + 1 + palindrome_radii[i] < n and
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1
            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]
        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]
        return longest_palindrome


# Tests:
test = Solution4()
test.longestPalindrome("babad")
test.longestPalindrome("cbbd")

