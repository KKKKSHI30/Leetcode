class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            s1 = self.helper(s, i, i)
            s2 = self.helper(s, i, i+1)
            if len(s1) > len(result):
                result = s1
            if len(s2) > len(result):
                result = s2
        return result

    def helper(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r]

test = Solution()
test.longestPalindrome("babad")
test.longestPalindrome("cbbd")

