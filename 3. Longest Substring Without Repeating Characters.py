# Sliding Window with Hashmap Approach
# Time: O(n)
# Space: O(1)
# 2023.06.20: yes
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, maxlen = 0, 0, 0
        window = {}
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) +1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            maxlen = max(maxlen, right-left)
        return maxlen

# Sliding Window Optimized Approach
# Time: O(n)
# Space: O(1)
# 2023.06.20: no
# notes: 记录节点的位置，可以直接跳过left，不需要每个每个的循环
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans


# Tests:
test = Solution2()
test.lengthOfLongestSubstring("abcabcbb")
test.lengthOfLongestSubstring('bbbbb')


