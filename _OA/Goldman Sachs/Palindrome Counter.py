# Same as lc647
class Solution:
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
# Test:
test = Solution()
test.countSubstrings("aaa")
