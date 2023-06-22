# Traverse Layer by Layer in Spiral Form
# Time: O(s+t)
# Space: O((s+t)*s)
# 2023.06.20: yes
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right = 0, 0
        valid = 0
        start, length = 0, float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float('inf') else s[start:start + length]

# Optimized Sliding Window
# Time: O(s+t)
# Space: O(s+t)
# notes: 非常聪明的方法， 只需要记录含有字母的位置就可以了，变成一个简短的list，减少运算复杂度
class Solution2:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

test = Solution2()
test.minWindow(s = 'aabcdcba', t = 'abc')
test.minWindow(s = "ADOBECODEBANC", t = "ABC")
test.minWindow(s = 'ab', t = 'a')