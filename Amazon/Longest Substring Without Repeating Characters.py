class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {}
        start = 0
        maxlength = 0
        s = list(s)
        if s == []:
            return 0
        for i, n in enumerate(s):
            if n not in dp or (n in dp and dp[n] < start):
                dp[n] = i
            else:
                end = i
                length = end - start
                maxlength = max(maxlength, length)
                start = dp[n] + 1
                dp[n] = i

        end = dp[n]
        length = end - start + 1
        maxlength = max(maxlength, length)
        return maxlength


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        l, r, longest = 0, 1, 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                l += 1
            longest = max(longest, r - l)
        return longest


test = Solution2()
test.lengthOfLongestSubstring("abba")
test.lengthOfLongestSubstring(" ")
test.lengthOfLongestSubstring("abcabcbb")
test.lengthOfLongestSubstring("bbbbb")
test.lengthOfLongestSubstring("pwwkew")
test.lengthOfLongestSubstring("dvdf")
test.lengthOfLongestSubstring("bb")
test.lengthOfLongestSubstring("")
