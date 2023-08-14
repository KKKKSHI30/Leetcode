class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = ""
        for i in s:
            if i == "i":
                new_s = new_s[::-1]
            else:
                new_s += i
        return new_s

# Tests:
test = Solution()
test.finalString("abcicbb")