from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        total_needs = Counter(t)
        window = {}
        left, right = 0, 0
        valid, required = 0, len(total_needs)
        ans = float("inf"), None, None
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            if c in total_needs and window[c] == total_needs[c]:
                valid += 1
            while left <= right and valid == required:
                c = s[left]
                if right - left < ans[0]:
                    ans = (right - left, left, right)
                window[c] -= 1
                if c in total_needs and window[c] < total_needs[c]:
                    valid -= 1
                left += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2]]

test = Solution()
test.minWindow(s = "ADOBECODEBANC", t = "ABC")
test.minWindow(s = 'ab', t = 'a')

class Solution2(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = filtered_s[l][1]
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
test.minWindow(s = "ADOBECODEBANC", t = "ABC")
test.minWindow(s = 'ab', t = 'a')